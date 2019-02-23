from discord.ext import commands
secretkey='yourkey'
bot_prefix=''
client=commands.Bot(command_prefix=bot_prefix)

def my_function(string):
    if string=='Hello':
        return [True,'Hey']
    else:
        return [False,None]

@client.event
async def on_message(message):
    embedflag=0
    outputstring=''
    if message.author==client.user:
        pass
    else:
        reply=my_function(message.content)
        if reply[0]==True:
            outputstring=reply[1]
        else:
            pass
        await client.send_message(message.channel,outputstring)
client.run(secretkey)
