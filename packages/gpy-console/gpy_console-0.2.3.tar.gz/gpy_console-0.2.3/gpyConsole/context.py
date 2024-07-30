from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Sequence, Union

from . import abc

from guilded.ext.commands.core import Cog

if TYPE_CHECKING:
    from .core import ConsoleCommand
    from . import ConsoleBot, ConsoleClient
    from guilded.ext.commands.view import StringView


class Context(abc.ConsoleMessageable):
    def __init__(self, **attrs):
        self.message: str = attrs.pop("message", None)
        self.bot: Union[ConsoleBot, ConsoleClient] = attrs.pop("bot", None)
        self.client = self.bot
        self.args: List[Any] = attrs.pop("args", [])
        self.kwargs: Dict[str, Any] = attrs.pop("kwargs", {})
        self.command: Optional[ConsoleCommand] = attrs.pop("command", None)
        self.view: Optional[StringView] = attrs.pop("view", None)
        self.invoked_with: Optional[str] = attrs.pop("invoked_with", None)
        self.invoked_parents: List[str] = attrs.pop("invoked_parents", [])
        self.invoked_subcommand: Optional[ConsoleCommand] = attrs.pop(
            "invoked_subcommand", None
        )
        self.subcommand_passed: Optional[str] = attrs.pop("subcommand_passed", None)
        self.command_failed: bool = attrs.pop("command_failed", False)

        self.server: None = None
        self.channel: None = None

    def __repr__(self) -> str:
        return f"<Context message={self.message}>"

    @property
    def valid(self) -> bool:
        return self.command is not None

    @property
    def cog(self) -> Optional[Cog]:
        if self.command is None:
            return None
        return self.command.cog

    async def reply(
        self,
        content: str,
    ) -> str:
        """|coro|

        Reply to the invoking console message.

        This is identical to :meth:`abc.ConsoleMessageable.send`.
        """

        return await self.send(content)
