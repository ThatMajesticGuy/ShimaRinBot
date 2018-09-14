import hypixel
import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random
import praw
import youtube_dl
import time
from weather import Weather, Unit
from fortnite_python import Fortnite
from fortnite_python.domain import Mode
from fortnite_python.domain import Platform
import os
import aiohttp
import json


#Bot Setup and APIs

client = commands.Bot("/")

startup_extensions = ["Music"]

HYPIXELAPI = os.environ.get('HYPIXEL_KEY')
API_KEYS = [HYPIXELAPI]
hypixel.setKeys(API_KEYS)

REDDITID = os.environ.get('REDDIT_ID')
REDDITSECRET = os.environ.get('REDDIT_SECRET')

post = praw.Reddit(client_id=REDDITID,
                   client_secret=REDDITSECRET,
                   user_agent='Shima Rin Bot v0.1 by DjDarkAssassin')

FORTNITEKEY = os.environ.get('FORTNITE_KEY')

fortnite = Fortnite(FORTNITEKEY)

@client.event
async def on_ready():
    print("Bot online")
    await client.change_presence(game=discord.Game(name="In Dj's Tent reading manga together ;)"))

class Main_Commands():
    def __init__(self, client):
        self.client = client

#Game
@client.command(pass_context=True)
async def coin(ctx):
    """Flips a coin"""
    choice = random.randint(1, 2)
    if choice == 1:
        await client.say("It landed on Tails!")
    if choice == 2:
        await client.say("It landed on Heads!")


#Responses

@client.command()
async def whatismilk():
    """Tells you what milk really is"""
    await client.say('Cereal Sauce')

@client.command(pass_context=True)
async def ping(ctx):
    return await ctx.send('Pong! {0}'.format(round(bot.latency, 1))
    """Pong"""



@client.command(pass_context=True)
async def hello():
    """Hello There!"""
    await client.say("Hi There! :wave:")

@client.command(pass_context=True)
async def idiot():
    """You're an idiot!"""
    await client.say("You're an idiot!")

@client.command(pass_context=True)
async def suwupreme():
    """Lyrics from the song 'Miraie - Suwupreme(Feat. Fluff Pink)'"""
    await client.say("Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme Supreme")

@client.command(pass_context=True)
async def baka():
    """BAKA!"""
    await client.say("no u")

@client.command(pass_context=True)
async def say(ctx,*args):
    """Makes the bot say whatever you want [Only for selected users]"""
    try:
        if ctx.message.author.id == 'USER1':
            mesg = ' '.join(args)
            await client.delete_message(ctx.message)
            return await client.say(mesg)

        elif ctx.message.author.id == 'USER2':
            mesg = ' '.join(args)
            await client.delete_message(ctx.message)
            return await client.say(mesg)

        elif ctx.message.author.id == 'USER3':
            mesg = ' '.join(args)
            await client.delete_message(ctx.message)
            return await client.say(mesg)
    except:
        await client.say("You do not have permission to use this command...")

@client.command()
async def todolist():
    """List of what I will do in the future :D"""
    await client.say("What to do:\n1. CoinMarketCap command\n2. Fortnite stats\n3. 4chan command")

#Reddit Posts

@client.command()
async def meirl():
    """Gets a post from r/meirl"""
    meirl = post.subreddit('me_irl').hot()
    pick_post = random.randint(1, 21)
    for i in range(0, pick_post):
        sub = next(x for x in meirl if not x.stickied)

    await client.say(sub.url)

@client.command()
async def reddit(arg):
    """Gets a post from any subreddit"""
    try:
        posts = post.subreddit(arg).hot()
        pick_post = random.randint(1, 21)
        for i in range (0, pick_post):
            sub = next(x for x in posts if not x.stickied)

        await client.say(sub.url)
    except:
        await client.say("This subreddit does not exist...")

    #Fortnite

@client.command(pass_context=True)
async def whereto():
    """Randomly select a place in Fortnite"""
    places = ["Hero House", "Villain House", "Risky Reels", "Lucky Landing", "China Motel", "New Factories", "Motel", "anywhere you want", "Football Ground", "Between Shifty and Flush", "Container", "Jail", "North of Wailing Woods", "Anarchy Acres", "Dusty Divot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", "Loot Lake", "Moisty Mire", "Pleasant Park", "Retail Row", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
    plc = random.choice(places)
    place = plc.lower()
    if plc == "anywhere you want":
        await client.say("Go " + place)
    else:
        await client.say("Go to " + place)

#Stats

@client.command()
async def hystats(arg):
    """Gets stats from Hypixel for a user"""
    try:
        player = hypixel.Player(arg)
        PlayerName = player.getName()
        PlayerLevel = player.getLevel()
        PlayerRank = player.getRank()

        embed = discord.Embed(
            title='Hypixel Stats',
            colour= discord.Colour.red()
            )

        embed.set_thumbnail(url='https://hypixel.net/attachments/621065/')
        embed.add_field(name='Player Name:', value=PlayerName, inline=False)
        embed.add_field(name='Player Rank:', value=PlayerRank['rank'], inline=False)
        embed.add_field(name='Player Level:', value=PlayerLevel, inline=False)
        await client.say(embed=embed)
    except:
        await client.say("The user you put in doesn't have data/does not exist...")



@client.command()
async def FNstats(arg):
    """Gets stats from Fortnite for a user"""
    try:
        player = fortnite.player(arg)
        statsQ = player.getStats(Mode.SQUAD)
        statsD = player.getStats(Mode.DUO)
        statsS = player.getStats(Mode.SOLO)

        embed = discord.Embed(
            title='Fortnite Stats',
            colour=discord.Colour.dark_purple()
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/409895347687522307/483009396616462356/FortniteClient-Win64-Shipping_123.png')
        embed.add_field(name='Name:', value=arg, inline=False)
        embed.add_field(name='Squad Wins:', value=statsQ.wins, inline=True)
        embed.add_field(name='Squad Kills:', value=statsQ.kills, inline=True)
        embed.add_field(name='Duo Wins:', value=statsD.wins, inline=True)
        embed.add_field(name='Duo KIlls:', value=statsD.kills, inline=True)
        embed.add_field(name='Solo Wins:', value=statsS.wins, inline=True)
        embed.add_field(name='Solo KIlls:', value=statsS.kills, inline=True)
        await client.say(embed=embed)
    except:
        await client.say("Oh no! We couldn't get stats for this user, or the user you put in doesn't exist...")
        
@client.command()
async def FNstatsPSN(arg):
    """Gets stats from Fortnite for a user"""
    try:
        player = fortnite.player(arg, Platform.PSN)
        statsQ = player.getStats(Mode.SQUAD)
        statsD = player.getStats(Mode.DUO)
        statsS = player.getStats(Mode.SOLO)

        embed = discord.Embed(
            title='Fortnite Stats',
            colour=discord.Colour.dark_purple()
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/409895347687522307/483009396616462356/FortniteClient-Win64-Shipping_123.png')
        embed.add_field(name='Name:', value=arg, inline=False)
        embed.add_field(name='Squad Wins:', value=statsQ.wins, inline=True)
        embed.add_field(name='Squad Kills:', value=statsQ.kills, inline=True)
        embed.add_field(name='Duo Wins:', value=statsD.wins, inline=True)
        embed.add_field(name='Duo KIlls:', value=statsD.kills, inline=True)
        embed.add_field(name='Solo Wins:', value=statsS.wins, inline=True)
        embed.add_field(name='Solo KIlls:', value=statsS.kills, inline=True)
        await client.say(embed=embed)
    except:
        await client.say("Oh no! We couldn't get stats for this user, or the user you put in doesn't exist...")

@client.command()
async def FNstatsXBOX(arg):
    """Gets stats from Fortnite for a user"""
    try:
        player = fortnite.player(arg, Platform.XBOX)
        statsQ = player.getStats(Mode.SQUAD)
        statsD = player.getStats(Mode.DUO)
        statsS = player.getStats(Mode.SOLO)

        embed = discord.Embed(
            title='Fortnite Stats',
            colour=discord.Colour.dark_purple()
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/409895347687522307/483009396616462356/FortniteClient-Win64-Shipping_123.png')
        embed.add_field(name='Name:', value=arg, inline=False)
        embed.add_field(name='Squad Wins:', value=statsQ.wins, inline=True)
        embed.add_field(name='Squad Kills:', value=statsQ.kills, inline=True)
        embed.add_field(name='Duo Wins:', value=statsD.wins, inline=True)
        embed.add_field(name='Duo KIlls:', value=statsD.kills, inline=True)
        embed.add_field(name='Solo Wins:', value=statsS.wins, inline=True)
        embed.add_field(name='Solo KIlls:', value=statsS.kills, inline=True)
        await client.say(embed=embed)
    except:
        await client.say("Oh no! We couldn't get stats for this user, or the user you put in doesn't exist...")


#Bitcoin

@client.command(pass_context=True)
async def bitcoin():
    """Gets the price of bitcoin from CoinDesk"""
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed (
            title='CryptoCurrency',
            colour= discord.Colour.gold()
        )

        embed.set_thumbnail(url='')
        embed.add_field(name='Bitcoin Price:', value=('$' + response['bpi']['USD']['rate']), inline=True)
        await client.say(embed=embed)

#Music

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

#weather
@client.command()
async def weather(arg):
    """Gets the weather for a location"""
    try:
        weather = Weather(unit=Unit.FAHRENHEIT)
        location = weather.lookup_by_location(arg)
        condition = location.condition
        date = condition.date
        text = condition.text
        temp = condition.temp

        C = (float(temp) - 32) * 5 / 9

        embed = discord.Embed(
            title='Weather',
            colour=discord.Colour.dark_blue()
        )

        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/412949621069840384/482633254227279882/d06.png')
        embed.add_field(name='Location:', value=arg, inline=False)
        embed.add_field(name='Date:', value=date, inline=False)
        embed.add_field(name='Weather:', value=text, inline=False)
        embed.add_field(name='Temp(F):', value=temp + ' F', inline=False)
        embed.add_field(name='Temp(C):', value=str(round(C)) + ' C', inline=False)
        await client.say(embed=embed)
    except:
        await client.say("The location you put in didn't have data, sorry!")


DISCORD = os.environ.get('DISCORD_KEY')
client.run(DISCORD)
