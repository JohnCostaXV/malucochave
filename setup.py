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

COR = 0x3498DB

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

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Sem registro")
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!registrar"):
            cargos = [
                # IDs dos cargos:
                "412708220021506058", #Master
            ]
            for r in message.author.roles:
                if r.id in cargos:
                    await asyncio.sleep(1)
                    await client.delete_message(message)
                    await asyncio.sleep(1)
                    entrada = client.get_channel("497231408792862770")
                    msg = "Olá, seja bem vindo ao Perfect Network!\nAntes que prossiga para nosso servidor do Discord, primeiro temos uma etapa de ´Verificação´ para uma melhor experiência dentro de nossa rede.\n\n**Como posso me verificar?**\nÉ muito simples! Você deve clicar na reação(✅) abaixo."

                    react = await client.send_message(entrada, msg)
                    await client.add_reaction(react, "✅")


                    global msg_id
                    msg_id = react.id

                    global msg_user
                    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "✅" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "Sem registro":
             await client.remove_reaction(msg, "✅", user)

     role1 = discord.utils.get(user.server.roles, name="Sem registro")
     await client.remove_roles(user, role1)
     
     await asyncio.sleep(1)
     role = discord.utils.get(user.server.roles, name="👨🏻‍🚀 JOGADOR")
     await client.add_roles(user, role)


client.run(os.environ.get("BOT_TOKEN"))
