#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time
import os


from nextcord.ext import commands
from nextcord import Interaction

#-----Commands----- 
class images(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#Dog
	@nextcord.slash_command(name = 'dog', description = '🐶Random Dog image (Exaple: /dog)')
	async def dog(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/dog')
			dogjson = await request.json()

		embed = nextcord.Embed(
			title = '🐶 Pictures | Dog',
			color = 0xc6c6f5
			).set_image(url=dogjson['link'])

		await ctx.send(embed = embed)

	#Cat
	@nextcord.slash_command(name = 'cat', description = '🐱Random Cat image (Exaple: /cat)')
	async def cat(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/img/cat')
			catjson = await request.json()

		embed = nextcord.Embed(
			title = '🐱 Pictures | Cat', 
			color=0xc6c6f5 
			).set_image(url = catjson['link'])
		await ctx.send(embed = embed)

	#Bird
	@nextcord.slash_command(name = 'bird', description = '🦜Random Bird image (Exaple: /bird)')
	async def bird(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/birb')
			birdjson = await request.json()

		embed = nextcord.Embed(
			title = '🦜 Pictures | Bird',
			color = 0xc6c6f5
			).set_image(url = birdjson['image'])

		await ctx.send(embed = embed)

	#Fox
	@nextcord.slash_command(name = 'fox', description = '🦊Random Fox image (Exaple: /fox)')
	async def bird(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/fox')
			foxjson = await request.json()

		embed = nextcord.Embed(
			title = '🦊 Pictures | Fox',
			color = 0xc6c6f5
			).set_image(url = foxjson['image'])

		await ctx.send(embed = embed)	

	#Koala
	@nextcord.slash_command(name = 'koala', description = '🐨Random Koala image (Exaple: /koala)')
	async def koala(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/koala')
			koalajson = await request.json()

		embed = nextcord.Embed(
			title = '🐨 Pictures | Koala',
			color = 0xc6c6f5
			).set_image(url = koalajson['image'])

		await ctx.send(embed = embed)

	#Panda
	@nextcord.slash_command(name = 'panda', description = '🐼Random Panda image (Exaple: /panda)')
	async def panda(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://some-random-api.ml/animal/panda')
			pandajson = await request.json()

		embed = nextcord.Embed(
			title = '🐼 Pictures | Panda',
			color = 0xc6c6f5
			).set_image(url = pandajson['image'])

		await ctx.send(embed = embed)		


		

	#Car
	@nextcord.slash_command(name = 'car', description = '🚗Random Car (Exaple: /car)')
	async def car(self, ctx: Interaction):

		async with aiohttp.ClientSession() as session:
			request = await session.get('https://api.popcat.xyz/car')
			car = await request.json()

		embed = nextcord.Embed(
			title = '🚗Random Car',
			description = car['title'],
			color = 0xc6c6f5
			).set_image(url = car['image'])

		await ctx.send(embed = embed)


	#Web Screen
	@nextcord.slash_command(name = 'webscreen', description = '🖼Send a Web site screenshot (Exaple: /webscreen https://google.com/)')
	async def webscreen(self, ctx: Interaction, url):

		embed = nextcord.Embed(
			title = f'🖼Web Site Screenshot',
			url = url,
			color = 0xc6c6f5
			).set_image(url = f'https://api.popcat.xyz/screenshot?url={url}')

		await ctx.send(embed = embed)	


	#Wasted
	@nextcord.slash_command(name = 'wasted', description = '❌Waste Avatar (Exaple: /wasted @user)')
	async def wasted(self, ctx: Interaction, user: nextcord.Member):

		url = f'https://some-random-api.ml/canvas/wasted?avatar={user.avatar.url}'

		embed = nextcord.Embed(color = 0xc6c6f5)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		await ctx.send(embed = embed)

	

	#Pixel art
	@nextcord.slash_command(name = 'pixelart', description = '🎮Pixel Avatar(Exaple: /pixelart @user)')
	async def pixelart(self, ctx: Interaction, user: nextcord.Member):

		url = f"https://some-random-api.ml/canvas/pixelate?avatar={user.avatar.url}"

		embed = nextcord.Embed(color = 0xc6c6f5)
		embed.set_image(url = url)
		embed.set_author(name = user.name, icon_url = user.avatar.url)

		await ctx.send(embed = embed)

	

	

	#Pat
	
#-----Run-----
def setup(bot):
	bot.add_cog(images(bot))