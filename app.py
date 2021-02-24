# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2021-2021 UWENIAC All rights reserved.
"""
import discord
import json
import logging
import os
from discord.ext import commands

# Json Part
with open('./config/setting.json', encoding='UTF8') as json_file:
    json_data = json.load(json_file)

    token = json_data["token"]
    prefix = json_data["prefix"]
    ver = json_data["ver"]


# Bot Part
client = commands.Bot(command_prefix=prefix)
bot = discord.Client()


@client.event
async def on_ready():
    print("\n봇을 실행해주셔서 감사합니다! 현재 니아의 버전은 %s 입니다. github에서 최신 버전이 있는지 확인해 주세요.\ngithub link : https://github.com/UWENIAC/nia\n" % ver)
    print(client.user.name)
    print(client.user.id)

    game = discord.Game("%s 도움말" % prefix + " | " + "v.%s" % ver)
    await client.change_presence(status=discord.Status.online, activity=game)

# Cogs Part
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
