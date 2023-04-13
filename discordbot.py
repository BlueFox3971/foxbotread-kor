from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX} 테스트':
        await message.channel.send("테스트 완료!")

    if message.content.startswith(f'{PREFIX} 안녕'):
        await message.channel.send('안녕하세요!')
        
    if message.content.startswith(f'{PREFIX} 사용설명서'):
        embed = discord.Embed(title="사용설명서", description="폭스봇 사용설명서", color=0x0048ba)
        embed.add_field(name="kr <명령어>", value='제 접두사는 "kr (명령어)" 예요. 사용설명서에 있는대로 움직일게요. \n"시키면 해야죠!" -건설로봇, 스타크래프트2', inline=False)
        embed.add_field(name="kr 소개", value="제 소개를 할게요. 그런데 쓸데없는 정보가 많답니다.", inline=False)
        embed.add_field(name="kr 질문", value="자주 물을만한 질문들을 모아봤어요.", inline=False)
        embed.add_field(name="난이도?", value="난이도는 1부터 10까지 있어요. (kr <장르> 단계1, 단계2, 단계3...) 그리고 진짜 어려운 'X' 단계도 있어요! (kr <장르> 단계X) 한번 도전해보시겠어요? :fire: :rooster: :ramen:", inline=False)
        embed.add_field(name="kr 소설 (난이도)", value="레벨에 맞는 소설 지문 일부를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
        embed.add_field(name="kr 시 (난이도)", value="레벨에 맞는 시를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
        embed.add_field(name="kr 대사 (난이도)", value="레벨에 맞는 영화, 드라마 등의 대사를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
        embed.add_field(name="kr (장르) 번호 (숫자)", value="지정한 글을 DM으로 보내드려요. DM으로 보내진 모든 글 하단에는 고유 번호가 있는데, 좋아하는 글을 다시 보고 싶으시다면 그 숫자를 기록해주셔도 좋아요!", inline=False)
        embed.add_field(name="kr 모든 (장르)", value="지정한 글 종류가 총 몇 개 수록되어있는 지 알려드려요!", inline=False)
        embed.add_field(name="kr 수필", value="폭스봇 주인이 자기 생각을 적은 노트가 있는데 그 중에서 아무거나 한 장을 뜯어서 뽑아 DM으로 보내드려요! ㅋㅋㅋㅋㅋㅋ", inline=False)
        embed.set_footer(text="다들 한국어 열심히 배워봐요! 화이팅!")
        await ctx.send(embed=embed)
        
    if message.content.startswith(f'{PREFIX} 예문'):
       await message.channel.send("{} 예문을 DM으로 보내드렸어요!".format(ctx.author.mention))
       await member.send(f'테스트 성공')


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
