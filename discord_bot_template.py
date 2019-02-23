from discord.ext import commands
secretkey='yourkey'
bot_prefix=''
client=commands.Bot(command_prefix=bot_prefix)

from my_functions import my_function

@client.event
async def on_message(message):
    if message.author==client.user:
        pass
    else:
        reply=my_function(message.content)
        await client.send_message(message.channel,reply)
client.run(secretkey)
