from __future__ import annotations

import abc, inspect
from typing import TYPE_CHECKING, Any, Type, Generator, List

from . import core

from guilded.ext.commands import Command
from guilded.ext.commands.cog import CogMeta, Cog, _BaseCommand

if TYPE_CHECKING:
    from typing import ClassVar

    from .context import Context as ConsoleContext
    from .core import ConsoleCommand


class CogABCMeta(CogMeta, abc.ABCMeta):
    __cog_console_commands__: List["ConsoleCommand"]

    def __new__(cls: Type[CogMeta], *args: Any, **kwargs: Any) -> CogMeta:
        name, bases, attrs = args
        attrs["__cog_name__"] = kwargs.pop("name", name)
        attrs["__cog_settings__"] = kwargs.pop("command_attrs", {})

        description = kwargs.pop("description", None)
        if description is None:
            description = inspect.cleandoc(attrs.get("__doc__", ""))
        attrs["__cog_description__"] = description

        commands = {}
        console_commands = {}
        listeners = {}

        new_cls = super().__new__(cls, name, bases, attrs, **kwargs)
        for base in reversed(new_cls.__mro__):
            for elem, value in base.__dict__.items():
                if elem in commands:
                    del commands[elem]
                if elem in console_commands:
                    del console_commands[elem]
                if elem in listeners:
                    del listeners[elem]

                is_static_method = isinstance(value, staticmethod)
                if is_static_method:
                    value = value.__func__
                if isinstance(value, _BaseCommand):
                    if is_static_method:
                        raise TypeError(
                            f"Command in method {base}.{elem!r} must not be staticmethod."
                        )

                    if isinstance(value, Command):
                        commands[elem] = value
                    elif isinstance(value, core.ConsoleCommand):
                        console_commands[elem] = value
                elif inspect.iscoroutinefunction(value):
                    try:
                        getattr(value, "__cog_listener__")
                    except AttributeError:
                        continue
                    else:
                        listeners[elem] = value

        new_cls.__cog_commands__ = list(
            commands.values()
        )  # this will be copied in Cog.__new__
        new_cls.__cog_console_commands__ = list(console_commands.values())

        listeners_as_list = []
        for listener in listeners.values():
            for listener_name in listener.__cog_listener_names__:
                # I use __name__ instead of just storing the value so I can inject
                # the self attribute when the time comes to add them to the bot
                listeners_as_list.append((listener_name, listener.__name__))

        new_cls.__cog_listeners__ = listeners_as_list
        return new_cls

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args)

    @classmethod
    def qualified_name(cls) -> str:
        return cls.__cog_name__


def _cog_special_method(func):
    func.__cog_special_method__ = None
    return func


class ConsoleMixin(metaclass=abc.ABCMeta):
    __cog_console_commands__: ClassVar[List["ConsoleCommand"]]

    def __new__(cls, *args: Any, **kwargs: Any):
        # For issue Rapptz/discord.py#426, we need to store a copy of the
        # command objects since we modify them to inject `self` to them.
        # To do this, we need to interfere with the Cog creation process.
        self = super().__new__(cls)
        cmd_attrs = cls.__cog_settings__

        # Either update the command with the cog provided defaults or copy it.
        # r.e type ignore, type-checker complains about overriding a ClassVar
        self.__cog_commands__ = tuple(
            c._update_copy(cmd_attrs) for c in cls.__cog_commands__
        )
        self.__cog_console_commands__ = tuple(
            c._update_copy(cmd_attrs) for c in cls.__cog_console_commands__
        )

        lookup = {cmd.qualified_name: cmd for cmd in self.__cog_commands__}
        console_lookup = {
            cmd.qualified_name: cmd for cmd in self.__cog_console_commands__
        }

        # Update the Command instances dynamically as well
        for command in self.__cog_commands__:
            setattr(self, command.callback.__name__, command)
            parent = command.parent
            if parent is not None:
                # Get the latest parent reference
                parent = lookup[parent.qualified_name]

                # Update our parent's reference to our self
                parent.remove_command(command.name)
                parent.add_command(command)

        for command in self.__cog_console_commands__:
            setattr(self, command.callback.__name__, command)
            parent = command.parent
            if parent is not None:
                # Get the latest parent reference
                parent = lookup[parent.qualified_name]

                # Update our parent's reference to our self
                parent.remove_console_command(command.name)
                parent.add_console_command(command)

        return self

    def get_console_commands(self) -> List["ConsoleCommand"]:
        r"""
        Returns
        --------
        List[:class:`.ConsoleCommand`]
            A :class:`list` of :class:`.ConsoleCommand`\s that are
            defined inside this cog.

            .. note::

                This does not include subcommands.
        """
        return [c for c in self.__cog_console_commands__ if c.parent is None]

    def walk_console_commands(self) -> Generator["ConsoleCommand", None, None]:
        """An iterator that recursively walks through this cog's console commands and subcommands.

        Yields
        ------
        Union[:class:`.ConsoleCommand`, :class:`.ConsoleGroup`]
            A command or group from the cog.
        """
        from .core import ConsoleGroup

        for command in self.__cog_console_commands__:
            if command.parent is None:
                yield command
                if isinstance(command, ConsoleGroup):
                    yield from command.walk_console_commands()

    def has_console_error_handler(self) -> bool:
        """:class:`bool`: Checks whether the cog has an error handler."""
        return not hasattr(
            self.cog_console_command_error.__func__, "__cog_special_method__"
        )

    @_cog_special_method
    async def cog_console_command_error(
        self, ctx: ConsoleContext, error: Exception
    ) -> None:
        """A special method that is called whenever a console error
        is dispatched inside this cog.

        This is similar to :func:`.on_console_command_error` except only applying
        to the console commands inside this cog.

        This **must** be a coroutine.

        Parameters
        -----------
        ctx: :class:`.Context`
            The invocation console context where the error happened.
        error: :class:`ConsoleCommandError`
            The error that happened.
        """
        pass

    def _inject(self, bot):
        cls = self.__class__

        # realistically, the only thing that can cause loading errors
        # is essentially just the command loading, which raises if there are
        # duplicates. When this condition is met, we want to undo all what
        # we've added so far for some form of atomic loading.
        for index, command in enumerate(self.__cog_commands__):
            command.cog = self
            if command.parent is None:
                try:
                    bot.add_command(command)
                except Exception as e:
                    # undo our additions
                    for to_undo in self.__cog_commands__[:index]:
                        if to_undo.parent is None:
                            bot.remove_command(to_undo.name)
                    raise e

        for index, command in enumerate(self.__cog_console_commands__):
            command.cog = self
            if command.parent is None:
                try:
                    bot.add_console_command(command)
                except Exception as e:
                    # undo our additions
                    for to_undo in self.__cog_console_commands__[:index]:
                        if to_undo.parent is None:
                            bot.remove_console_command(to_undo.name)
                    raise e

        # check if we're overriding the default
        if cls.bot_check is not Cog.bot_check:
            bot.add_check(self.bot_check)

        if cls.bot_check_once is not Cog.bot_check_once:
            bot.add_check(self.bot_check_once, call_once=True)

        # while Bot.add_listener can raise if it's not a coroutine,
        # this precondition is already met by the listener decorator
        # already, thus this should never raise.
        # Outside of, memory errors and the like...
        for name, method_name in self.__cog_listeners__:
            bot.add_listener(getattr(self, method_name), name)

        return self

    def _eject(self, bot) -> None:
        cls = self.__class__

        try:
            for command in self.__cog_commands__:
                if command.parent is None:
                    bot.remove_command(command.name)

            for command in self.__cog_console_commands__:
                if command.parent is None:
                    bot.remove_console_command(command.name)

            for _, method_name in self.__cog_listeners__:
                bot.remove_listener(getattr(self, method_name))

            if cls.bot_check is not Cog.bot_check:
                bot.remove_check(self.bot_check)

            if cls.bot_check_once is not Cog.bot_check_once:
                bot.remove_check(self.bot_check_once, call_once=True)
        finally:
            try:
                self.cog_unload()
            except Exception:
                pass


class ConsoleCog(ConsoleMixin, Cog, metaclass=CogABCMeta):
    def __init__(self):
        ConsoleMixin.__init__(self)
        Cog.__init__(self)

        from guilded.ext.commands import Bot
