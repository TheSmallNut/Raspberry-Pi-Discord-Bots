#!/usr/bin/python3
import discord
from discord.ext import commands
from random import randrange
import random

bot = commands.Bot(command_prefix="ITT/")


@bot.event
async def on_ready():
    print("Bot is ready.")


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)

key = open("ITT.gitignore", 'r')
key = key.read()

bot.run(key)
