import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def adios(ctx):
    await ctx.send("Nos vemos en otra ocasión")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTUxODAwMTU1NDI3NDM4NTk4MA.GLsULR.TbrRQPyKxJ8y8sOtv5kOZhwVcyGKqT3W3ZBunE")
