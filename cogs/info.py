#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp

import datetime
import time

from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks



#-----Commands----- 
class info(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	#User Info
	@nextcord.slash_command(name = 'user', description = '🎃Shows information about User (Exaple: /user @Cuber)')
	async def user(self, ctx: Interaction, user: nextcord.Member):

		embed = nextcord.Embed(
			color = 0xc6c6f5
			)

		embed.set_author(
			name = f'Information about {user.name}',
			icon_url = user.avatar.url
			)
		embed.add_field(
			name = 'Common Information',
			value = f'**Username:** {user.name}#{user.discriminator}\n**User ID:** {user.id}\n**Highest Role:** {user.top_role.mention}\n**Joined Server:** {user.joined_at.strftime("%a, %#d, %B, %Y, I:%M %p")}\n**Created Account:** {user.created_at.strftime("%a, %#d, %B, %Y, I:%M %p")}'
			)
		embed.set_thumbnail(
			url= user.avatar.url
			)
		

		await ctx.send(embed = embed)


	#Server info
	@nextcord.slash_command(name = 'server', description = '🥊Shows information about Server (Exaple: /server)')
	async def server(self, ctx: Interaction):

		name = str(ctx.guild.name)
		description = str(ctx.guild.description)
		owner = str(ctx.guild.owner)
		Id = str(ctx.guild.id)
		memberCount = str(ctx.guild.member_count)
		channelamount = str(len(ctx.guild.channels))
		vcamounts = str(len(ctx.guild.voice_channels))
		roleamount = str(len(ctx.guild.roles))
		emoji_amount = str(len(ctx.guild.emojis))
		verificationlevel = str(ctx.guild.verification_level)

		embed = nextcord.Embed(
			title = name + ' server information',
			description = description,
			color = 0xc6c6f5
			)

		embed.set_thumbnail(url = ctx.guild.icon.url)

		embed.add_field(name = 'Owner', value = owner, inline = True)
		embed.add_field(name = 'Server ID', value = Id, inline = True)
		embed.add_field(name = 'Created', value = f"<t:{int(time.mktime(ctx.guild.created_at.timetuple()))}>", inline = True)
		embed.add_field(name = 'Member Count', value = memberCount, inline = True)
		embed.add_field(name = 'Channel Count', value = channelamount, inline = True)
		embed.add_field(name = 'Voice Channel Count', value = vcamounts, inline = True)
		embed.add_field(name = 'Role Count', value = roleamount, inline = True)
		embed.add_field(name = 'Emoji Count', value = emoji_amount, inline = True)
		embed.add_field(name = 'Verification Level', value = verificationlevel, inline = True)
		
		await ctx.send(embed = embed)
	
	#Bot Info
	#Comming Soon


#-----Run-----
def setup(bot):
	bot.add_cog(info(bot))