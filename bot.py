import os
from discord.ext import commands, tasks
import discord

TOKEN = os.getenv("TOKEN")  # musi zgadzać się z nazwą w Railway, wielkie litery!

intents = discord.Intents.default()  # wymagane dla discord.py 2.x
intents.message_content = True  # jeśli chcesz czytać wiadomości

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    wysylaj_analizy.start()

@tasks.loop(minutes=60)
async def wysylaj_analizy():
    channel = bot.get_channel(1448439389955948544)
    if channel:
        await channel.send("NBA: Lakers vs Celtics → zwycięzca: Lakers, Over/Under: 210, BTTS: Tak")

bot.run(TOKEN)
