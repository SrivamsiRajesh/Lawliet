import  nextcord
from  nextcord.ext  import commands
import  nextcord
from  nextcord.ext  import  commands
from  nextcord  import  Embed
from nextcord import slash_command, Interaction
import os

bot  =  commands.Bot()
intents  =  nextcord.Intents.default()
intents.members  =  True
intents.message_content  =  True
bot  =  commands.Bot(command_prefix="+",  intents=intents)
bot.remove_command('help')

@bot.event
async  def  on_ready():
        await  bot.change_presence(activity=nextcord.Activity(
                type=nextcord.ActivityType.playing,  name='as a mod'))
print("Bot  is  online  and  ready  sir  ")

@bot.slash_command(
        description="Hello",  )
async  def  hello(interaction:  nextcord.Interaction):
        await  interaction.send("Hey  I  am  Lawliet!!  :blush:  ")
  
@bot.command()
async  def  clear(ctx,  amount=30):
        await  ctx.channel.purge(limit=amount  +  1)

@bot.command()
async  def  inv(ctx):
        embed  =  nextcord.Embed(
                title="Invite  this  bot  your  server  ",
                url="https://dsc.gg/llawliet",
                description=
                "The  nextcord  id  of  the  developer  :-  <s.r.i.2.0.0.8  >#8718",
                color=0xFF5733)
        await  ctx.send(embed=embed)


@bot.command()
async def spam(ctx, amount : int, *, message=None):
    limit = 1000
    if amount > limit:
        await ctx.send("exceeds spam limit")
        return
    else:
        for _ in range(amount): 
            await ctx.send(message)

#-----Cogs-----
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for extention in initial_extensions:
        bot.load_extension(extention)


bot.run('TOKEN')
