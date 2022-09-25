#-----Imports-----
import nextcord
import random
import asyncio
import aiohttp
import time
import os
import datetime

from nextcord.ext import commands
from nextcord import Interaction
from nextcord.ext import application_checks

from datetime import datetime
from datetime import timedelta




#-----Commands----- 
class moderation(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot


	#Clear
	@nextcord.slash_command(name = 'clear', description = '❌Clear messages (Exaple: /clear 10) (Only for admins)')
	@application_checks.has_permissions(administrator=True)
	async def clear(self, ctx: Interaction, amount: int):

		if amount > 1000:
			embed = nextcord.Embed(
				title = '❌Error',
				description = "I'm sorry, but that's too big for me. Try something smaller.",
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:
			 
			await ctx.channel.purge(limit = amount)

			embed = nextcord.Embed(
				title = '❌Clear',
				description = f'Successfully deleted {amount} messages',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

	#Ban
	@nextcord.slash_command(name = 'ban', description = '❌Ban the user (Exaple: /ban lawliet')
	@application_checks.has_permissions(administrator=True)
	async def ban(self, ctx: Interaction, user: nextcord.Member, reason: str = None):

		if reason is None:

			await user.ban()

			embed = nextcord.Embed(
				title = '❌Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:

			await user.ban(reason = reason)

			embed = nextcord.Embed(
				title = '❌Ban',
				description = f'{user.name} has been banned from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

	#Kick
	@nextcord.slash_command(name = 'kick', description = '❌Kick the user (Exaple: /kick @lawliet')
	@application_checks.has_permissions(administrator=True)
	async def kick(self, ctx: Interaction, user: nextcord.Member, reason: str = None):

		if reason is None:

			await user.kick()

			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has kicked from {ctx.guild.name}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)

		else:

			await user.kick(reason = reason)

			embed = nextcord.Embed(
				title = '❌Kick',
				description = f'{user.name} has been kicked from {ctx.guild.name}. Reason: {reason}.',
				color = nextcord.Color.red()
				)

			await ctx.send(embed = embed)


#-----Run-----
def setup(bot):
	bot.add_cog(moderation(bot))
