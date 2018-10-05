import discord
import random
import asyncio
import time
import datetime
import sys
import io
import os
import re
import json
import base64

client = discord.Client()

@client.event
async def on_ready():
    print("Iniciado com sucesso!")
    while True:
        await client.change_presence(game=discord.Game(name="Online com mais de {} membros!".format(str(len(set(client.get_all_members())))), url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)
        await client.change_presence(game=discord.Game(name="PerfectNetwork!\nCriado por Johnn#0001", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)
        await client.change_presence(game=discord.Game(name="mc-perfect.com.br", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)

client.run(os.environ.get("BOT_TOKEN"))
