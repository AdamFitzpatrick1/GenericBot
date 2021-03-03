import discord
from discord.ext import commands
import random
import datetime

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
      print(f'{member} has left the server.')

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

@client.command()
async def creator(ctx):
    await ctx.send('Adam (owner)')

@client.command()
async def bellpepper(ctx):
    await ctx.send('https://www.youtube.com/watch?v=Y85W5UnOSGo')

@client.command()
async def gatdayum(ctx):
    await ctx.send('https://www.youtube.com/watch?v=tp5uQEXlY-o')


@client.command()
async def commands(ctx):
    await ctx.send('```Commmands: \n\n .hello: Displays a Hello message \n .creator: Displays the creator of the bot\n .8ball: Play a game of magic 8 ball\n .gif: displays a random gif```')

@client.command()
async def funnyjoke(ctx):
    await ctx.send('Leyton')



@client.command(aliases = ['8ball'])
async def _8ball(ctx, * ,question):
    responses = [ "It is certain.",

    "It is decidedly so.",

    "Without a doubt.",

    "Yes - definitely.",

    "You may rely on it.",

    "As I see it, yes.",

    "Most likely.",

    "Outlook good.",

    "Yes.",

    "Signs point to yes.",

    "Reply hazy, try again.",

    "Ask again later.",

    "Better not tell you now.",

    "Cannot predict now.",

    "Concentrate and ask again.",

    "Don't count on it.",

    "My reply is no.",

    "My sources say no.",

    "Outlook not so good.",

    "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@client.command()
async def gif(ctx):
    randomGif= ['https://media.giphy.com/media/Aff4ryYiacUO4/giphy.gif', 'https://media.giphy.com/media/8VrtCswiLDNnO/giphy.gif', 'https://media.giphy.com/media/j6SbREYp7TtE90T9cl/giphy.gif', 'https://media.giphy.com/media/MdGUUTVHk7s1BA5Pyk/giphy.gif', 'https://media.giphy.com/media/3o6ZtpRoYe9wbyfcBi/giphy.gif', 'https://gfycat.com/blackandwhitebonyindusriverdolphin']

    await ctx.send(random.choice(randomGif))


client.run('')