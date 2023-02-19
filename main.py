import  nextcord
from nextcord.ext import commands, menus
from nextcord import slash_command, Interaction , Embed
import os
import textwrap
import urllib
import aiohttp
import datetime
from compile import runCode
from datetime import datetime
import random 

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
                color=0xFF5733)
        await  ctx.send(embed=embed)

@bot.command(aliases = ['l', 'lyrc', 'lyric'])
async def lyrics(ctx, *, search = None):
    if not search: 
        embed = nextcord.Embed(
            title = "No search argument!",
            description = "You havent entered anything, so i couldnt find lyrics!"
        )
        return await ctx.reply(embed = embed)
    
    song = urllib.parse.quote(search) 
    
    async with aiohttp.ClientSession() as lyricsSession:
        async with lyricsSession.get(f'https://some-random-api.ml/lyrics?title={song}') as jsondata: 
            if not 300 > jsondata.status >= 200: 
                return await ctx.send(f'Recieved poor status code of {jsondata.status}')

            lyricsData = await jsondata.json()

    error = lyricsData.get('error')
    if error: 
        return await ctx.send(f'Recieved unexpected error: {error}')

    songLyrics = lyricsData['lyrics'] 
    songArtist = lyricsData['author'] 
    songTitle = lyricsData['title'] 
    songThumbnail = lyricsData['thumbnail']['genius']

   
    for chunk in textwrap.wrap(songLyrics, 4096, replace_whitespace = False):
        embed = nextcord.Embed(
            title = songTitle,
            description = chunk,
            color = nextcord.Color.blurple(),
        )
        embed.set_thumbnail(url = songThumbnail)
        await ctx.send(embed = embed)


#-----Cogs-----
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append('cogs.' + filename[:-3])

if __name__ == '__main__':
    for extention in initial_extensions:
        bot.load_extension(extention)

#CODE
global currentLanguage
currentLanguage = 'python'

@bot.command()
async def language(ctx):
    global currentLanguage
    languages = ["python", "javascript"]

    code = ctx.message.content.split()

    if len(code) == 1:
        out = nextcord.Embed(title=f"Current language:", color=0x00b3ff)
        out.add_field(
            name="---", value=f"```{currentLanguage}```", inline=False)

    else:
        code[1] = code[1].lower()
        if code[1] == "list":
            out = nextcord.Embed(
                title=f"Supported languages include:", color=0x00b3ff)
            out.add_field(name="---", value="Python, Javascript", inline=False)

        elif code[1] in languages:

            currentLanguage = code[1]
            out = nextcord.Embed(title=f"Language set to: ", color=0x00b3ff)
            out.add_field(name="---", value=f"```{code[1]}```", inline=False)

        else:
            out = nextcord.Embed(title=f"Language not Found: ", color=0x00b3ff)
            out.add_field(
                name="---", value=f"language '{code[1]}' does not exist.\nUse ```.language list``` for a list of supported languages", inline=False)


    await ctx.send(embed=out)


@bot.command()
async def compile(ctx):
    global currentLanguage
    code = ctx.message.content

    # splitting the string into a list for each line
    lines = code.split('\n')

    parsedLines = []

    # want to exclude the .compile and the ```
    # might be a simpler way to do this
    for i in range(2, len(lines) - 1):
        parsedLines.append(lines[i])

    # parses the lines for the language --> probably an easier way to send parameters from the nextcord bot
    # language = lines[0].split(' ')[1]
    if currentLanguage == 'python':
        # w allows for overwriting the text file each time
        f = open("compile.txt", "w")
        # joins the parsed list of lines with a new line at the end of each and writes that to the text file
        f.write('\n'.join(parsedLines))

        f.close()

        code_output = runCode('python', 'compile.txt')

        embed = nextcord.Embed(title="Code Output", color=0x00b3ff)
        embed.add_field(
            name="---", value=f"```\n{code_output}\n```", inline=False)
        await ctx.send(embed=embed)

    elif currentLanguage == 'javascript':
        f = open('compile.txt', 'w')
        f.write('\n'.join(parsedLines))
        f.close()

        code_output = runCode('javascript', 'compile.txt')
        embed = nextcord.Embed(title="Code Output", color=0x00b3ff)
        embed.add_field(
            name="---", value=f"```\n{code_output}\n```", inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embedvar = nextcord.Embed(title="Lawliet | All Commands", description="``+clear`` - clears number of messages specified by user\n``+inv`` - invite bot to server\n+``l <song name>`` - gets the lyrics of any song\n``+language python`` - changes language to be compiled to python\n``+compile (code)`` - compiles code and prints output\n\n``**IMAGE**\n\n /dog/cat/bird/fox/koala/panda`` - get image of any animal specified\n\n``/car/webscreen`` - Send a Web site screenshot/wasted\n\n``/pixelart <@user>`` - gets pixelart\n\nMODERATION\n\n``/clear`` - clears specified number of messages\n ``/ban`` - bans specifed user from guild\n``/kick`` - kicks specifed user from guild\n",color=0x5865F2)
    await ctx.reply(embed=embedvar)



truth_norm = ["When was the last time you told a lie?",
"What is your biggest fear?",
"What is your guilty pleasure?",
"Who do you have a crush on?",
"If you had to date someone in this room who would it be?",
"Have you ever been cheated on someone?",
"Have you ever been cheated on?",
"What is the meanest thing that you have done?",
"What was your first kiss like?",
"Who is the last person that you stalked on social media?",
"What is the craziest event that you have ever been to?",
"When was the last time you peed yourself?",
"What is the worst dream that you have had?",
"Why did your last relationship end?",
"What is the most embarrassing thing that has happened to you this year?",
"What habit can’t you seem to quit?",
"Who is your celebrity crush?",
"What is your least favorite thing about your best friend?",
"What don’t you like about your boyfriend or girlfriend?",
"Have you ever hooked up with the same sex?",
"What is a secret that you have never told anyone before?",
"How many people have you kissed?",
"How many people have you been with?",
"Has anyone ever accidentally seen you naked? Who?",
"Have you ever gone out without wearing a bra and underwear?",
"Who is your crush in this server?",
"Who was your first love?"
"Would you stop talking to all of your friends for a million dollars?",
"Have you ever committed a crime? If so what was it?",
"Have you ever been to jail?",
"Who was your first crush?",
"Would you ever cheat on your significant other if they said it was okay?",
"Would you ever be polygamous?",
"Have you ever had a crush on your teacher/professor?",
"Have you ever had a crush on your best friend’s mom or someone generally much older that you?",
"If you were the opposite gender for the day? What do you think you would wear? What would you do?",
"What is the most embarrassing music that you like to listen to?",
"If you and one person in this room could be the last people on Earth left alive who would that person be?",
"Would you ever donate an organ to someone in this room?",
"Who in this room do you think would be the worst date?",
"Who in this room do you think would be the best date?",
"What is your secret talent if you have one?",
"What is the worst intimate experience that you have had?",
"What is the worst thing about being your gender?",
"If you were a superhero what would your power be?",
"Have you ever performed a striptease for anyone before?",
"Have you ever eaten food from the floor?",
"Have you ever cheated on an exam?",
"Have you ever been suspended from school?",
"What is the most trouble that you ever got into in school?",
"What is the most trouble that you ever got into at home / with your parents?",
"When was a time that someone really betrayed your trust?",
"Talk about a time that you failed in life.",
"Tell us about a time that you were really drunk.",
"Have you ever spread a rumor?",
"Have you ever been intimate in a public place?",
"What is something you used to do that makes you cringe now?",
"Do you sing in the shower?",
"When is the last time you threw up?",
"When is the last time you cried?",
"Have you ever laughed so hard that you cried?",
"Have you ever cried from watching a TV show or a movie?",
"What is the most embarrassing thing that you have ever done in front of a crush?",
"What do you look for in a potential love interest?",
"Would you rather be rich or famous? You cannot be both.",
"What would you do with a million dollars?",
"Could you survive without any phone or internet for a month?",
"What is the most that you have ever had to drink?",
"What is the longest amount of time that you have ever been awake?",
"If you could do it what would you change your name to?",
"Name a famous person that you would like to be friends with.",
"Who are 5 famous people that you would like to have dinner with? They can either be dead or alive.",
"What is your biggest pet peeve?",
"When was the worst time that you threw up?",
"If you could only save one person in this room from a fire who would it be?",
"Who is the most attractive person in the room?",
"Who is the most annoying person in the room?",
"Which person in the room do you think gossips the most?",
"What is your biggest insecurity?",
"What is the most expensive thing you bought that wasn’t a house or a car?",
"What is a common misconception about you?",
"What is something that you would do that people would assume you would never do?",
"Where is the weirdest place that you have gone to the bathroom?",
"What is the most embarrassing thing that your parents have caught you doing?",
"When was the most embarrassing time that you passed gas?",
"What was the most disgusting thing to ever come out of your body?",
"What is the most disgusting thing that you have ever had in your mouth?",
"How old do you think you will live to be?",
"What do you want to do when you are retired?",
"If you could live anywhere in the world where would it be?",
"What do you think is your best physical quality?",
"Have you ever had a run-in with the law?",
"What can you sometimes be prejudiced about?",
"When is the last time you talked about someone behind their back?",
"Who is your least favorite friend?",
"Would you kiss the person on your left?",
"Who is the sexiest person in the room?",
"Do you shower every day?",
"Do you brush teeth every day?",
"Do you floss your teeth every day?",
"Have you ever gotten a DUI?",
"What would you do if you could retire at 40?",
"Have you ever been tempted to cheat on someone?",
"Have you ever had a one night stand?",
"Would you ever get a tattoo? What kind of tattoo would it be?",
"What is your least favorite thing about your best friend?",
"Have you ever wanted to kill someone?",
"Have you ever gotten into a physical altercation with anyone?",
"If you could only eat one food every day for the rest of your life what would it be?",
"Have you ever had feelings for a friend or family member’s significant other?",
"What is the worst thing that anyone has ever said about you?",
"What is the worst thing that somebody ever said to you?",
"What is your biggest fantasy?",
"Have you ever gone to the bathroom in the pool?",
"How many grand-kids do you think you will have?",
"Who in the group do you think is the wildest in bed?",
"For guys: have you ever worn lingerie?",
"Do you have any fetishes?",
"What is your idea of good s..x?",
"Do you masturbate?",
"How many times do you take care of yourself a week?",
"What is the most s..x that you have had in a day?",
"What is the longest amount of time that you have gone without intercourse?",
"What is your favorite position?",
"Have you ever given oral s..x?",
"Have you ever received oral s..x?",
"Have you ever been in a threesome? Would you ever?",
"How about an orgy?",
"Would you ever swap partners with anyone?",
"Have you ever stolen money from your parents?",
"For girls: what bra size do you wear?",
"For girls: what is your worst period story?",
"Do you watch “adult movies”?",
"Have you ever taken nude photos or videos of yourself?",
"If you watch x-rated movies what type is your favorite?",
"Do you have a favorite “adult” store?",
"Could you live without watching “adult movies”?",
"Could you live without having s..x for the rest of your life?",
"Have you ever tried to get out of a speeding ticket?",
"Who is the craziest person that you know (in person?)",
"When was a time that you completely lost it?",
"What kind of pajamas do you wear?",
"Have you ever stolen something for a store?",
"Have you ever met a celebrity?",
"What is an unpopular opinion that you have?",
"If you weren’t here in this room right now what would you probably be doing?",
"What kind of person would you want to marry one day?",
"What do you think happens after we die?",
"Are you afraid of dying?",
"What is the best thing that you have ever had to eat?",
"What is your favorite movie and why?",
"What is the silliest thing that you have ever done?",
"What is your favorite thing about the opposite gender (or the gender that you are attracted to?)",
"Who would play you in a movie about your life?",
"If you ever wrote a memoir what would the title be?",
"What is your favorite kind of music to listen to?",
"Name one thing on your bucket list.",
"If you could have someone else’s life for one day who would it be?",
"If you could kiss one celebrity who would it be?",
"If you could say anything to one person in your life without any consequences what would it be?",
"If you had to pick one person in your immediate family to survive who would it be?",
"If you could choose a way to die what would it be?",
"How many romantic interests do you think you will have for the rest of your life?",
"Talk about the craziest thing that you overheard.",
"Was there ever a time in your life that you thought you were going to die?",
"What was one of the best moments of your life?",
"What is your best childhood memory?",
"What is your worst childhood memory?",
"What kind of parent do you think you will be?",
"What is the most romantic thing that you have ever done?",
"What is the most romantic thing that has ever been done for you?",
"What was your worst workplace experience?",
"What is the most amount of time that you have ever spent in a hospital?",
"Where is the furthest place that you have ever traveled to?",
"Have you ever broken a bone?",
"Have you ever gotten stitches?",
"What is the longest amount of time that you have ever been away from home?",
"What is your most embarrassing puberty-related story?",
"Where did you used to think babies come from?",
"How did you find out that Santa Claus is not real?",
"What is your religion or spirituality?",
"What is the coolest thing that you have ever done at a job?",
"What is one thing that you have always wanted to do but have not gotten around to it yet?",
"Do you have any irrational fears?",
"What is the sweetest thing that someone could do for you?",
"Have you ever had a crush on a co-worker?",
"Have you ever let someone take the blame for something you did? What happened?",
"Tell us about something really crazy that you were able to get away with."]

# Below are Dares, you can add/remove as many you want! Just put a comma after setting each question.

dare_norm = ["Do a free-style rap for the next minute.",
"Let another person post a status on your behalf.",
"Hand over your phone to another player who can send a single text saying anything they want to anyone they want.",
"Let the other players go through your phone for one minute.",
"Smell another player's armpit.",
"Smell another player's bare foot.",
"Eat a bite of a banana peel.",
"Do an impression of another player until someone can figure out who it is.",
"Say pickles at the end of every sentence you say until it's your turn again.",
"Imitate a YouTube star until another player guesses who you're portraying.",
"Act like a chicken until your next turn.",
"Talk in a British accent until your next turn.",
"Call a friend, pretend it's their birthday, and sing them Happy Birthday to You.",
"Name a famous person that looks like each player in the room.",
"Show us your best dance moves.",
"Eat a packet of hot sauce straight.",
"Let another person draw a tattoo on your back with a permanent marker.",
"Put on a blindfold and touch the other players' faces until you can figure out who's who.",
"Serenade the person to your right for a full minute.",
"Do 20 squats.",
"Let the other players redo your hairstyle.",
"Gulp down a raw egg.",
"Dump out your purse, backpack, or pockets and do a show and tell of what's inside.",
"Let the player to your right redo your makeup.",
"Do a prank call on one of your family members.",
"Let another player create a hat out of toilet paper — and you've got to wear it for the rest of the game.",
"Do a plank for a full minute.",
"Let someone give you a wedgie.",
"Put five cubes in your mouth (you can't chew them, you just have to let them melt—brrr).",
"Bark like a dog.",
"Draw your favorite movie and have the other person guess it (Pictionary-style).",
"Repeat everything the person to your right says until your next turn.",
"Demonstrate how you style your hair in the mirror (without actually using the mirror).",
"Play air guitar for one minute.",
"Empty a glass of cold water onto your head outside.",
"Lay on the floor and act like a sizzling piece of bacon.",
"In the next ten minutes, find a way to scare another player and make it a surprise.",
"Lick a bar of soap.",
"Eat a teaspoon of mustard.",
"Put an ice cube in your pocket until it melts.",
"Try to chug a bottle of beer in less than 20 seconds.",
"Take a shot of barbecue sauce.",
"Eat half a teaspoon of wasabi.",
"Go to the nearest fridge, pour a little bit of all the liquids found (not including medication) into a glass, stir it, and drink it all up.",
"Pledge your undying love to the person directly across from you for a minute.",
"Make an unflattering picture of yourself your Facebook profile picture for at least a day.",
"Let someone spoon-feed you with both of you blindfolded for 2 minutes. Make it something messy like yogurt, applesauce, etc.",
"Turn off your phone for the rest of the game.",
"Let everyone in the room, dress you up, do your makeup, and your hair. Take a picture and make that your new social media profile picture for at least one day.",
"Pick your nose in front of everyone.",
"Let someone in the room write whatever they want from your Facebook account.",
"Do the worm.",
"Slap the person on the left.",
"Spank the person on your right.",
"Smell the foot of the person on your left.",
"Use a pickup line on the person on your right.",
"Serenade someone in the room.",
"Wear someone else’s worn socks on your head for the rest of the game.",
"Wear someone else’s shoes as mittens for the next 10 minutes.",
"Put your toe in your mouth. If you cannot do that then you have to put someone else’s toe in your mouth.",
"Do the robot",
"Do 50 sit ups.",
"Jog in place very slowly for the next 3 minutes.",
"Say something very dirty to the person on your left.",
"Speak in an accent for the rest of the game (examples of accents include British, Southern American, Caribbean, German, and Italian.)",
"Pick up the person next to you.",
"Carry the person next to you across the room.",
"Swallow a tablespoon of ketchup, mustard, or something similar.",
"Talk for 5 minutes without stopping.",
"Put your underwear on top of your head.",
"Lick the side of someone’s face.",
"Perform a rap for everyone in the room.",
"Try to put your foot behind your head.",
"Speak in pig Latin for the rest of the game.",
"Switch clothes with someone of the opposite gender for the rest of the game.",
"Pretend to spin an imaginary hula hoop around your waist for the next 2 minutes.",
"Send a love letter to someone on Facebook.",
"Send someone a message that says, “I know what you did last summer.”",
"Wear your underwear outside of your clothes.",
"Streak across the room.",
"Crack a raw egg on your head.",
"Post a video of you singing and share it on your social media account.",
"Ask the neighbors next door for a cup of sugar. If they do not have sugar or do not answer, try until you get someone.",
"Say the alphabet backwards.",
"Lay on the floor and pretend that you are swimming for two minutes.",
"Speak in rhymes for the rest of the game.",
"Instead of speaking, you have to sing everything that you want to say for the rest of the game.",
"Blow a raspberry on the stomach of the person to your right.",
"Prank call the number of someone that you do not know.",
"Give an insult to every person in the room.",
"Try to woo the person to your right.",
"Chew gum that someone else has already chewed.",
"Switch outfits with the person on your right.",
"Do the moonwalk across the room.",
"Go outside and try to hug the next person that walks by.",
"may also like to check out these 19 boyfriend and girlfriend games.",
"Go outside and sing Twinkle, Twinkle Little Star loudly.",
"Call someone on your phone and talk to them for 5 minutes without telling them that you are playing Truth or Dare.",
"Snort like a pig at the end of each sentence you say for the rest of the game.",
"Sing a song for 2 minutes, but meow instead of singing the words.",
"Strip down to your underwear and make an outfit for yourself using no more than 2 rolls of toilet paper.",
"Sit on someone’s lap for 10 minutes.",
"Slow dance with the person on your left for the duration of one song.",
"Give a kiss to each player in the room. A peck on the lips is okay.",
"Let everyone in the room give you a makeup makeover. Everyone gets to contribute.",
"Let each person in the room paint your nails.",
"Eat a piece of food off of someone’s face without using your hands.",
"Do a belly dance for one minute for everyone in the room.",
"Give a foot massage to the person on your left.",
"Go outside and wrap a toilet paper around your neighbors tree.",
"Let the person next to you give you a hair cut using only his/hers left hand.",
"Go outside and do a chicken dance for  5 minutes.",
"Cut 5 onions into little pieces.",
"Eat couple cloves of raw garlic.",
"Go outside and pretend that you are an airplane for 10 minutes.",
"Go to your neighbors house and say you are sorry for hitting his/her dog.",
"Go to your neighbors house and pretend to be Adele and sing “Hello” behind his/her door.",
"Go and fart in front of your teacher or boss.",
"Spit on someone.",
"Take a coin out of your wallet and lick it.",
"Do a crazy dance outside in a busy intersection.",
"Touch your friends nose with your tongue only.",
"Prank call someone and pretend she/he is your girlfriend/boyfriend and propose to him/her.",
"Bark like a dog for 10 minutes.",
"Wax your arms in front of everyone.",
"Kiss the person in the room who is the same gender. Do it passionately.",
"Stand or jump on one foot for 5 minutes.",
"Go to your neighbors house and tell him/her a joke.",
"Cry loudly in front of everyone.",
"Try to do a stand up comedy in front of the other players.",
"Imitate any animal of your choice for several minutes.",
"Let the person on your left draw a mustache on your skin with a lipstick only.",
"Let the person on your right put a make up on you blind folded.",
"Show your whole browsing history to the players in the room.",
"Disclose your girlfriend’s/boyfriend’s name online.",
"Call your best friend and make him/her believe that you are a gay.",
"Try to be a ballerina and dance for 5 minutes.",
"Say “I love you” for 50 times.",
"Take a shower with all your clothes on.",
"Call your best friend make her believe that you hate her.",
"Propose to the person on your left.",
"Call your mom and cry on the phone telling her that you just got dumped.",
"Pretend that you are an enemy with the person on your right.",
"Don’t talk for the rest of the game.",
"Don’t talk to anyone for 30 minutes.",
"Do a seductive dance in front of everyone.",
"Use a poetry form of talking for the rest of the game.",
"Call your dad and tell him that you are going to elope in Vegas.",
"Go on the street and wear your underwear over your pants for 10 minutes and yell to everyone who passes by that you are a superman.",
"Go outside and bed for money.",
"Prank call someone and make them believe that they have won the lottery.",
"French kiss the person on your left.",
"Prank call someone and tell them that you are horny.",
"Be rude to your girlfriend/boyfriend for a day.",
"Go outside and propose to the first person who passes by.",
"Get your back hair waxed in front of the other players.",
"Behave like a lesbian for the rest of the game.",
"Repeat “I will do it” for 100 times.",
"Try to drink 3 glasses of milk in 1 minute.",
"Call your mom and ask her to cook the food that you hate the most.",
"Try to laugh continuously for the rest of the game.",
"Remove any of your 4 articles of clothing.",
"Have a 5 minute conversation of any topic.",
"Go to your neighbor and ask if they could give you a condom.",
"Remove your pants/skirt for the rest of the game.",
"Give a 20 minute lecture of safe sex.",
"Try to touch your nose with your tongue.",
"Do a belly dance.",
"Join the Discord server https://discord.gg/mwaPKHypGF and ask for 5$."
"Mimic the joker from a Batman movie.",
"Call your closest friend and invite him/her for a threesome."]

@bot.command()
async def truth(ctx):
  embed = nextcord.Embed(title=f"{ctx.author.name}, {random.choice(truth_norm)}", colour=nextcord.Colour.green())

  await ctx.send(embed=embed)

@bot.command()
async def dare(ctx):
  embed = nextcord.Embed(title=f"{ctx.author.name}, {random.choice(dare_norm)}", colour=nextcord.Colour.red())

  await ctx.send(embed=embed)  

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        msg = f"Welcome {member.mention} to {guild.name}"
        await guild.system_channel.send(msg)



bot.run('-')
