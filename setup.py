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
    if message.content.lower().startswith('!say'):
            try:
                cargos = [
                    # IDs dos cargos:
                    "412708220021506058", #Master
                    "412709280383500298", #Coordenador
                    "412710082321580043", #Gerente
                    "412710669746569216" #Administrador
                ]
                for r in message.author.roles:
                    if r.id in cargos:
                        args = message.content.split(" ")
                        await client.send_message(message.channel, (" ".join(args[1:])))
                        await client.delete_message(message)
            except IndexError:
                await client.delete_message(message)
                embedd = discord.Embed(
                    title='Comando incorreto!',
                    color=COR,
                    description='Use `!say [mensagem]`'
                )
                embedd.timestamp = datetime.datetime.utcnow()
                embedd.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embedd)
            except:
                await client.delete_message(message)
                embed2 = discord.Embed(
                    title='Permissão negada!',
                    color=COR,
                    description='Você não tem permissão para executar esse comando.'
                )
                embed2.timestamp = datetime.datetime.utcnow()
                embed2.set_footer(text=message.author.name, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=embed2)
            finally:
                pass

    if message.content.lower().startswith('!ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=COR, description='Meu tempo de resposta é {}ms!'.format(round((t2 - t1) * 1000)))
        ping_embed.timestamp = datetime.datetime.utcnow()
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)

    if message.content.lower().startswith('!avatar'):
            try:
                user = message.mentions[0]
                embed = discord.Embed(
                    title="",
                    color=COR,
                    description='Clique [aqui](' + user.avatar_url + ') para acessar o avatar do {}.'.format(user.name)
                )
                embed.set_author(
                    name=message.server.name,
                    icon_url="https://i.imgur.com/DCbWIa6.jpg"
                )
                embed.set_image(
                    url=user.avatar_url
                )
                await client.send_message(message.channel, embed=embed)
            except IndexError:
                err = discord.Embed(
                    color=COR,
                    description='Clique [aqui](' + message.author.avatar_url + ') para acessar o avatar do {}.'.format(message.author.name)
                )
                err.set_author(
                    name=message.server.name,
                    icon_url="https://i.imgur.com/DCbWIa6.jpg"
                )
                err.set_image(
                    url=message.author.avatar_url
                )
                await client.send_message(message.channel, embed=err)
            finally:
                pass

    if message.content.lower().startswith("!limpar"):
            cargos = [
                # IDs dos cargos:
                "412708220021506058", #Master
                "412709280383500298", #Coordenador
                "412710082321580043", #Gerente
                "412710669746569216" #Administrador
            ]    
            for r in message.author.roles:
                if r.id in cargos:
                    args = message.content.split(" ")
                    try:
                        ammount = int(args[1]) + 1 if len(args) > 0 else 2
                    except:
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Por gentileza, digite um valor para limpar!"))
                        return

                    cleared = 0
                    failed = 0

                    async for m in client.logs_from(message.channel, limit=ammount):
                        try:
                            await client.delete_message(m)
                            cleared += 1
                        except:
                            failed += 1
                            pass

                    failed_str = "\n\nFalha para limpar %s message(s)." % failed if failed > 0 else ""
                    returnmsg = await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.blue(), description="%s limpou %s message(s).%s" % (message.author.mention, cleared, failed_str)))
                    await asyncio.sleep(5)
                    await client.delete_message(returnmsg)

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
                    embed = discord.Embed(title="Procedimento:", color=COR, description="Antes que prossiga para nosso servidor do Discord, primeiro temos uma etapa de **verificação** para uma melhor experiência dentro de nossa rede.\n\n**Como posso me verificar?**\nÉ muito simples! Você deve clicar na reação abaixo.")
                    embed.set_author(name="Sistema de verificação", icon_url="https://i.imgur.com/DCbWIa6.jpg")
                    embed.set_footer(text="Equipe de desenvolvimento do discord", icon_url="https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif")
                    embed.timestamp = datetime.datetime.utcnow()
                    react = await client.send_message(entrada, embed=embed)
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
