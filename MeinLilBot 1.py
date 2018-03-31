import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client ()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("The bot is ready for camp!")

@client.event
async def on_message(message):
    if message.content == "tell me something i dont know":
        await client.send_message(message.channel, "Ze meaning of Ze life")
    if message.content == "meaning of ze life":
        await client.send_message(message.channel, "Twini Victor")
    if message.content.upper().startswith('!MAZEL'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> TOV!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "148477485695238144":
            args = message.content.split(" ")
            #args[0] = !SAY
            #args[1] = Shalom
            #args[2] = Goyim
            #args [1:] = Shalom Goyim
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "Heh do you actually think a jew can run commands")
    if message.content.upper().startswith('!AMIJEWISH'):
        if "423918698730881024" in [role.id for role in message.author.roles]:
             userID = message.author.id
             await client.send_message(message.channel, "<@%s> Of course you're one of us brother" % (userID))
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> You're just a filthy imposter" % (userID))


