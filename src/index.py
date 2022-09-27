import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=':v', description="Bot oficial de chompajas")

@bot.command()
def ping(ctx):
    ctx.send('pong')