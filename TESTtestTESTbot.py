#BOT BY MADMAX

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#-INIZIALIZZAZIONE BOT-
client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='Cyberpunk2020'))
	print ("I am ready")
