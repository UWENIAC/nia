# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2021-2021 UWENIAC All rights reserved.
"""
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='도움말')
    async def help(self, ctx):
        embed = discord.Embed(title="니아 명령어", colour=0x5C7EBB)
        embed.add_field(name="도움말", value="도움말을 호출합니다.", inline=False)
        embed.add_field(name="개발자", value="개발자를 불러냅니다.", inline=False)
        embed.set_footer(text="Copyright (c) 2021-2021 UWENIAC All rights reserved.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(commands(bot))
    bot.remove_command('help')
