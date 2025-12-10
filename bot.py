import os
import discord
from discord.ext import commands, tasks

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1448439389955948544  # ID kanału na Discordzie

# Ustaw intents
intents = discord.Intents.default()
intents.message_content = True  # potrzebne do czytania treści wiadomości

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    wysylaj_analizy.start()

@tasks.loop(minutes=60)  # co godzinę
async def wysylaj_analizy():
    channel = bot.get_channel(CHANNEL_ID)
    if channel is not None:
        analiza = "NBA: Lakers vs Celtics → winner: Lakers, Over/Under: 210, BTTS: Yes"
        await channel.send(analiza)

bot.run(TOKEN)
