import discord
from discord.ext import commands
secretkey='yourkey'
Client=discord.Client
bot_prefix=''
client=commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_message(message):
    embedflag=0
    if message.author==client.user:
        pass
    else:
        a,b=message.content.split(',')
        if int(a) > int(b):
            outputstring="a is larger than b"
        elif int(a) == int(b):
            outputstring="a is equal to b"
        else:
            outputstring="a is smaller than b"
        await client.send_message(message.channel,outputstring)
client.run(secretkey)
