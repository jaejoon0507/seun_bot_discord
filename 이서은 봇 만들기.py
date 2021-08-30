import discord
import asyncio
import re
import youtube_dl

client = discord.Client()



que = {}
playerlist = {}
playlist = list() #재생목록 리스트


token = "ODgxODUzNzA5NTAyNTM3NzY4.YSy4RA.rgmrT1p7tWoCbsZZaneCaXiNjjw"


def queue(id): #음악 재생용 큐
	if que[id] != []:
		player = que[id].pop(0)
		playerlist[id] = player
		del playlist[0]
		player.start()




@client.event
async def on_ready():

    print(client.user.name)
    print('가동완료')
    g = discord.Game('활동중 표시 될 이름')
    await client.change_presence(status=discord.Status.online, activity=g)






@client.event
async def on_message(message):
    if message.content ==  '서은':
        await message.channel.send('하이')
    if message.content ==  '이지훈은 뭐다?':
        await message.channel.send('개싸이코패쓰 !!')
    if message.content ==  '김규원은?':
        await message.channel.send('펔킹 규원')
    if message.content ==  '이안이는?':
        await message.channel.send('씹덕')
    if message.content.startswith("!음악"):
        msg = message.content.split(" ")
        try:
            url = msg[1]
            url1 = re.match('(https?://)?(www\.)?((youtube\.(com))/watch\?v=([-\w]+)|youtu\.be/([-\w]+))', url) #정규 표현식을 사용해 url 검사
            if url1 == None:
                await client.send_message(message.channel, embed=discord.Embed(title=":no_entry_sign: url을 제대로 입력해주세요.",colour = 0x2EFEF7))
                return
        except IndexError:
            await client.send_message(message.channel, embed=discord.Embed(title=":no_entry_sign: url을 입력해주세요.",colour = 0x2EFEF7))
            return


        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)




  


client.run(token)