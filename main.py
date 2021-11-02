import discord
import requests
import json
import random
#import os
#os library works if we hide our token in an online editor

client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'mad', 'miserable']
starter_encouragements = ["Cheer up!", "Hang in there.",
"You are a great person/bot", "Dont be sad please, darling"]

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        quote = getQuote()
        await message.channel.send(quote)

    msg = message.content
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run('TOKEN')
