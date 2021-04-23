#!/usr/bin/python3
import discord
from discord.ext import commands
from random import randrange
import random

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print("Bot is ready.")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.event
async def on_message(ctx):
    DADBOTID = 503720029456695306
    AINSLEYID = 551538546251661323
    #THESMALLNUTID = 81898425720778752
    SHAANID = 329669482341597185
    # print(ctx)
    channel = ctx.channel
    if ctx.author.id == DADBOTID:
        arrayOfQuotes = [
            "shut up dad",
            "i hate you",
            "dad stfu",
            "you dont get it dad",
            "you just don't understand me",
            "<:sad:794058789375705098>",
            "<:crying:794058506269098015> not like this dad",
            "dont talk to me",
        ]
        randomQuote = random.choice(arrayOfQuotes)
        await channel.send(randomQuote)
    elif ctx.author.id == AINSLEYID:
        arrayOfQuotes = [
            "ainsley listening to her music again smh",
            "ainsley, dont be mean to people based on their preferences",
            "weeb",
            "wanna be in my deathnote ainsley?",
            "lets play valorant, ill play yoru",
        ]
        randomNum = randrange(50)
        print(randomNum)
        if randomNum == 0:
            randomQuote = random.choice(arrayOfQuotes)
            await channel.send(randomQuote)
    elif ctx.author.id == SHAANID:
        arrayOfQuotes = [
            "hahahahhahahahhahahahhahagba",
            "shaan you're so sexy aaah..hahaha",
            "this is not pogchamp",
        ]
        randomNum = randrange(10)
        print(randomNum)
        if randomNum == 0:
            randomQuote = random.choice(arrayOfQuotes)
            await channel.send(randomQuote)

    # if ctx.author.id != 794141958783631412:
    #    await channel.send('hi')

key = open("bot.gitignore", 'r')
key = key.read()

bot.run(key)
