import os
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1448439389955948544  # ID kanału na Discordzie

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    wysylaj_analizy.start()

@tasks.loop(minutes=60)  # co godzinę
async def wysylaj_analizy():
    channel = bot.get_channel(CHANNEL_ID)
    analiza = "NBA: Lakers vs Celtics → zwycięzca: Lakers, Over/Under: 210, BTTS: Tak"
    await channel.send(analiza)

bot.run(TOKEN)
