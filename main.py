import discord
#import os
#os library works if we hide our token in an online editor

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTA0NzQ3OTcyNDgxMzkyNzIw.YYACNg.T1oH7wB98cCxCl3KKwh8yWUHEtA')
