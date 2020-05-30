from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
 

@bot.command()
async def ?command(ctx):
    await ctx.send('ここにコマンド一覧かurlを')


@bot.command()
async def ?help(ctx):
    await ctx.send('ここにコマンド一覧かurlを')


@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))


bot.run(token)
