# -- coding:utf-8 --
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2021-2021 UWENIAC All rights reserved.
"""
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='뉴스')
    async def news(self, ctx):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
        url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=732'
        webpage = requests.get(url, headers = headers)
        soup = BeautifulSoup(webpage.content, "html.parser")
        result = soup.find(attrs={"class":"list_body newsflash_body"})
        
        rank1 = result.li.a['href']
        rank2 = result.li.next_sibling.next_sibling.a['href']
        rank3 =result.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.a['href']


        embed = discord.Embed(title = '뉴스 기사', colour= 0xffff00)
        embed.add_field(name = '첫번째 기사', value = rank1)
        embed.add_field(name = '두번째 기사', value = rank2)
        embed.add_field(name = '세번째 기사', value = rank3)
        embed.set_footer(text="Copyright (c) 2021-2021 UWENIAC All rights reserved.")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(news(bot))