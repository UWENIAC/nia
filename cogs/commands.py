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
        embed.add_field(name="삭제", value="메시지를 삭제합니다.\n사용 예시 : 니아야 삭제 10(삭제할 메시지 개수)", inline=False)
        embed.add_field(name="킥", value="사용자를 추방합니다.\n사용 예시 : 니아야 킥 @니아", inline=False)
        embed.add_field(name="밴", value="사용자를 차단합니다.\n사용 예시 : 니아야 밴 @니아", inline=False)
        embed.add_field(name="뮤트", value="사용자를 뮤트합니다.\n사용 예시 : 니아야 뮤트 @니아", inline=False)
        embed.add_field(name="언뮤트", value="사용자를 언뮤트합니다.\n사용 예시 : 니아야 언뮤트 @니아", inline=False)
        embed.add_field(name="뉴스", value="오늘의 네이버 뉴스 3가지를 호출합니다.\n분야 : IT", inline=False)
        embed.add_field(name="한강", value="한강 수온을 알려드립니다.", inline=False)

        embed.set_footer(text="Copyright (c) 2021-2021 UWENIAC All rights reserved.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(commands(bot))
    bot.remove_command('help')
