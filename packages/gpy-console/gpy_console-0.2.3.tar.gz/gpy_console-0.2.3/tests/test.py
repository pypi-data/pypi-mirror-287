import guilded
from gpyConsole import console_commands
from guilded.ext import commands

bot = console_commands.ConsoleBot(
    command_prefix="!",
    features=guilded.ClientFeatures(official_markdown=True),
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.load_extension("example_cog")
    if not bot._console_running:
        bot.start_console()


@bot.event
async def on_console_message(message: str):
    print(f"Received console message: {message}")
    await bot.process_console_commands(message)


@bot.event
async def on_command_error(
    ctx: commands.Context, error: guilded.ClientException
):  # Library still supports normal command errors
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        raise error


@bot.event
async def on_console_command_error(
    ctx: console_commands.Context, error: guilded.ClientException
):  # Library also supports console command errors
    if isinstance(error, console_commands.ConsoleCommandNotFound):
        return
    else:
        raise error


@bot.console_command()
async def hey(
    ctx: console_commands.Context,  # Modified Console Context with less features (.reply and .send are the same)
    channel: guilded.ChatChannel,
    user: guilded.User,
):  # Library automatically converts type annotations, just like in guilded.py
    # Missing converters: guilded.Role, guilded.Member, guilded.ChatMessage, guilded.Attachment
    await ctx.reply(f"Sending message to {user.name} (id: {user.id})")
    await channel.send(
        f"Hello from Console! I'm `{bot.user.name}`, and you are {user.mention}"
    )


@bot.command()
async def start(ctx: commands.Context):
    if not bot._console_running:
        bot.start_console()


@bot.console_command()
async def stop(ctx: console_commands.Context):
    # Let's stop the console. This can't be reversed, unless you make a command in Guilded to start it, or until on_ready is called again.
    bot.stop_console()


@bot.console_command()
async def ls(ctx: console_commands.Context):
    print(bot.all_console_commands)


@bot.command()
async def hi(ctx: commands.Context):
    print("hi used")
    await ctx.send(f"Hello {ctx.author.mention}!")


bot.run("gapi_token")
