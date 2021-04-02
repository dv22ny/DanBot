import discord
import random

from discord.raw_models import RawBulkMessageDeleteEvent
from discord.ext import commands
from discord.utils import get
from discord.ext import tasks

TOKEN = ("NzU3NjQ5NTkwMjg2ODExMTc2.X2jeKg.wDDGh9Nuz4i7vYQl9cu4TyWe1PQ")
client = commands.Bot(command_prefix='_')
@client.event
async def on_message(message):  # bulk of command handling
        if message.author == client.user:  # prevents bot from replying to itself
            return
        if message.content.startswith('!hello'):  
            msg = 'Hello {0.author.mention}'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('dan'):
            msg = 'Dan? Dantheman? Oh yeah, I know him! Literal embodiment of a skill issue'.format(message)
            #msg = 'Dan is mad hot {0.author.mention}, I agree with you'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('dhelp'):
            msg = '```dhelp for help,. dan for a bio of Dan, !hello for help, !game to change status, !name to change name```'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('!game'):  # change game presence of bot
            split = message.content.split(' ')
            msg = " ".join(split[1:])
            await client.change_presence(activity=discord.Game(name=msg))
            await message.add_reaction('\U0001F44D')
        if message.content.startswith('!name'):  # change nickname of bot on server
            split = message.content.split(' ')
            name = " ".join(split[1:])
            await message.guild.get_member(client.user.id).edit(nick=name)
            await message.add_reaction('\U0001F44D')
        #if message.content.startswith('!eric'): #shows rando pic of eric lol

        if message.content.startswith('duhoh'):
            msg = 'uhhhh ohhhhh'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('deric'):
            msg = 'eric moment'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('LOL Dan'):
            msg = 'LOL'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('Raindrops on roses'):
            msg = 'And whiskers on kittens.'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('Good night Dan'):
            msg = 'Good night {0.author.mention}! Sleep tight and dont let the danbugs bite 😊'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('Good morning Dan'):
            msg = 'Good morning {0.author.mention}! Hope ya slept well 😊'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('pognatalie'):
            msg = 'Natalie is an eh qb player, I can confirm {0.author.mention}, get shrekt'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('Pog'):
            msg = 'Poggem stoggers'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('skill issue'):
            msg = 'Skill Issue moment'.format(message)
            await message.channel.send(msg)
        if message.content.startswith('nat'):
            msg = 'In the world of qb nat is the one to beat'.format(message)
            await message.channel.send(msg)
       
        await client.process_commands(message)
        if message.content.startswith('socials'):
            msg = 'Website: https://www.twisttutors.tk/, Twitter: https://twitter.com/TwistTutors, Instagram: https://www.instagram.com/Twist_Tutors/, Facebook: https://www.facebook.com/twist.tutors/'.format(message)
            await message.channel.send(msg)
@client.command()
async def spam(ctx, member : discord.Member):
    spam_embed = discord.Embed(
        title="Get shrekt",
        colour=discord.Colour.dark_theme(),
        description=None
        )
    spam_embed.set_image(url="https://cdn.discordapp.com/attachments/815780780365578271/817959532118540288/rick_roll.gif")
    for x in range(0,3):
        await ctx.send(member.mention)
    await ctx.send(embed=spam_embed)
        
@client.command()
async def eric(ctx, arg):
    await ctx.send(arg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    msg = "!help"
    await client.change_presence(activity=discord.Game(name=msg))
    corner = client.get_channel(817911098681720854)
    await corner.connect()
client.run("NzU3NjQ5NTkwMjg2ODExMTc2.X2jeKg.wDDGh9Nuz4i7vYQl9cu4TyWe1PQ")
