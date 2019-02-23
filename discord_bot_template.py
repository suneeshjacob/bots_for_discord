from discord.ext import commands
secretkey='yourkey'
bot_prefix='#'
client=commands.Bot(command_prefix=bot_prefix)

def my_function(string):
    if x in ['bastard','cunt','fuck','whore','shit','bitch','mother fucker','blowjob','dick','slut','cock']:
        return 'No profanity allowed. If you continue you will be kicked or possibly banned'                                                
    elif x in ["Hello","Hi"]:
        return 'Hi there, how are you?'
    elif x in ["God\'s not real","God is fake"]:
        return 'no u'
    else:
        return ''
   

@client.event
async def on_message(message):
    if message.author==client.user:
        pass
    else:
        reply=my_function(message.content)
        await client.send_message(message.channel,reply)
client.run(secretkey)
