# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2021-2021 UWENIAC All rights reserved.
"""
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests as r
import json

class hanriver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='한강')
    async def help(self, ctx):
        api = "https://api.qwer.pw/request/hangang_temp?apikey=guest"
        with open("./config/hanriver/api.json", "wb") as file:
            response = r.get(api)
            file.write(response.content)

        with open("./config/hanriver/api.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            temp = data[1]["respond"]["temp"]

        embed = discord.Embed(colour=0x5C7EBB)
        embed.add_field(name="한강 수온", value=temp + "도", inline=False)
        embed.add_field(name="자살예방상담전화", value="1393\n삶이 있는 한 희망은 있다 -키케로-", inline=False)
        embed.set_footer(text="Copyright (c) 2021-2021 UWENIAC All rights reserved.")
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(hanriver(bot))