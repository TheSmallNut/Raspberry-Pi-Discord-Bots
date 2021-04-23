#!/usr/bin/python3
import discord
from discord.ext import commands
from owotrans import owo
import colorama
from colorama import Fore, Style 
from random import randrange
import random
AHELIID = 438542854982336512


def oodler(message):
    listOfVowels = ["a", "e", "i", "o", "u", "y"]
    nextMessage = ""
    for char in message:
        for vowel in listOfVowels:
            if char.lower() == vowel:
                nextMessage += "oodle"
                break
            elif vowel == "y":
                nextMessage += char
    return nextMessage


bot = commands.Bot(command_prefix="o!")


@bot.event
async def on_ready():
    print("Bot is ready.")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Oodle! {round(bot.latency * 1000)}ms")


@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        randomNumber = randrange(300)
        print("%s Is Bot: %s Message: \"%s\" Random Number: %s" %(ctx.author,ctx.author.bot,ctx.content,randomNumber))
        if randomNumber == 0:
            oodledMessage = oodler(ctx.content)
            if oodledMessage != ctx.content and ctx.author.id != 438542854982336512:
                await ctx.channel.send(oodledMessage)
        elif randomNumber == 1:
            owoedMessage = owo(ctx.content)
            if owoedMessage != ctx.content:
                await ctx.channel.send(owoedMessage)
    await bot.process_commands(ctx)


key = open("oodleKey.gitignore", 'r')
key = key.read()

bot.run(key)
