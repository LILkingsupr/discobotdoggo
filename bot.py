import discord

TOKEN = ''

client = discord.Client()


@client.event
async def on_ready():
    print('i am better than catto')


@client.event
async def on_message(message):

        print('hi')
        username = str(message.author).split('#')[0]
        channel = str(message.channel.name)

        if message.author == client.user:
            return
        elif username == 'Catto':
            await message.channel.send('doggo > catto')
            return
        elif message.content == '$D help':
            await message.channel.send('DOGGO IS HERE TO HELP')
            await message.channel.send('type $D doggo for dog picture')
            await message.channel.send('type $D suicide to be kicked from the server')
            return
        elif message.content == '$D suicide':
            await message.author.kick(message.author)
            return
        elif message.content == '$D doggo':
            return

client.run(TOKEN)