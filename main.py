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

def updateEncouragements(encouraging_message):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        encouragements.append(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]

def deleteEncouragment(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
    db[encouragements] = encouragements

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        quote = getQuote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    options = starter_encouragements
    if 'encouragements' in db.keys():
        options = options + db['encouragements']

    if msg.startswith('$new'):
        encouraging_message = msg.split('$new ', 1)[1]
        updateEncouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith('$del'):
        encouragements = []
        if 'encouragements' in db.keys():
            index = int(msg.split('$del', 1)[1])
            deleteEncouragment(index)
            encouragements = db['encouragements']
        await message.channel.send(encouragements)

client.run('TOKEN')
