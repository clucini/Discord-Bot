import discord
import asyncio
import io
import aiohttp
import random
import os
import makemame as mm
import csv
import pandas as pd
import reddit

client = discord.Client()

names = ['Sarah', 'Connor', 'Claudio', 'Liam', 'Ben', 'Stacey', 'Bronte', 'Immy']

async def download_hist(channel):
    messages = []
    async for message in client.logs_from(channel, 100000):
        messages.append([message.content,message.author, str(message.timestamp)])
    with open('messages/' + str(channel) + '_messages.csv', 'w+', encoding='utf-8') as f:
        writer = csv.writer(f,lineterminator = '\n')
        for message in messages:
            writer.writerow([message[0], message[1], message[2]])

def rank_check(min_rank, person):
    pass

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Biggest Benis'))

@client.event
async def on_message(message):
    if message.content.startswith('$'):
        command = message.content.split()[0][1:].lower()
        if command == 'help':
            await client.send_message(message.channel, "no u")
        
        elif command == 'messages':
            counter = {}
            tmp = await client.send_message(message.channel, 'Calculating messages...')
            async for log in client.logs_from(message.channel, limit=100):
                if not log.author in counter:
                    counter[log.author] = 1    
                else:
                    counter[log.author] += 1
            await client.edit_message(tmp, '-------------Biggest Boys-------------')
            for person in sorted(counter, key=counter.get, reverse=True):
                await client.send_message(message.channel, '{} : {}'.format(person, counter[person]))
                
        elif command == 'coin':
            coin = random.randint(0,100)
            if coin < 50:
                await client.send_message(message.channel, 'heads')
            else: 
                await client.send_message(message.channel, 'tails')

        elif command == 'fight':
            if len(message.attachments) != 0:
                await client.send_message(message.channel, 'Meme captured')
                async with aiohttp.ClientSession() as session:
                    async with session.get(message.attachments[0]['url']) as resp:
                        image = await resp.read()

                name = 'memes/'+ str(random.randint(0,10)) +'.png'
                pername = 'perms' + str(len(os.listdir('perms/'))) + '.png'
                with open(name, 'wb') as f:
                    f.write(image)
                with open(pername, 'wb') as f:
                    f.write(image)

                mm.make(name)

            elif '-combined' in message.content:
                mm.make('redditimages/' + random.choice(os.listdir('redditimages/')))

            elif '-reddit' in message.content:
                if len(message.content.split()) < 4:
                    await client.send_message(message.channel, 'Usage: $fight sub1 sub2 -reddit [-top]')
                else:
                    top = '-top' in message.content
                    subs = ' '.join(filter(lambda x:x[0]!='-', message.content.split()[1:]))
                    print(subs)
                    im1, sub1 = reddit.get_random(subs.split()[0],top)
                    im2, sub2 = reddit.get_random(subs.split()[1],top)
                    if im1 == "error":
                        await client.send_message(message.channel, "Error on sub: " + sub1)
                    if im2 == "error":
                        await client.send_message(message.channel, "Error on sub: " + sub2)                        
                    if 'rand' in subs:
                        await client.send_message(message.channel, sub1 + " : " + sub2)
                    async with aiohttp.ClientSession() as session:
                        async with session.get(im1) as resp:
                            image1 = await resp.read()
                    async with aiohttp.ClientSession() as session:
                        async with session.get(im2) as resp:
                            image2 = await resp.read()
                    name1 = 'redditimages/' + str(len(os.listdir('redditimages/'))) + '.png'
                    with open(name1, 'wb') as f:
                        f.write(image1)
                    name2 = 'redditimages/' + str(len(os.listdir('redditimages/'))) + '.png'
                    with open(name2, 'wb') as f:
                        f.write(image2)
                    mm.makereddit(name1, name2)

            else:
                await client.send_message(message.channel, 'No meme sent')
                mm.make("")
            await client.send_file(message.channel, 'badmeme.png')


        elif command == 'quote':
            quoter = message.author
            quotee = message.content.split()[1]
            if quotee in names:
                with open('quotes.csv', 'a') as f:
                    quotes_writer = csv.writer(f) 
                    quotes_writer.writerow([quotee, message.content.partition(' ')[2].partition(' ')[2], quoter])
                    await client.send_message(message.channel, 'Quoted')
            else:
                await client.send_message(message.channel, 'Invalid name')

        elif command == 'search':
            quotes = pd.read_csv('quotes.csv')
            if message.content.split()[1] == 'random':
                await client.send_message(message.channel, quotes.sample())
        
        elif command == "download_channel":
            await client.send_message(message.channel, 'Running...')
            await download_hist(message.channel)
            await client.send_file(message.channel, 'messages/' + str(message.channel) + '_messages.csv')

        elif command == "reddit":
            sub = message.content.split()[1]
            text = ""
            if "-top" in message.content:
                text = reddit.get_random(sub, True)
            else:
                text = reddit.get_random(sub, False)                
            await client.send_message(message.channel, text)

        elif command == "randimage":
            await client.send_message(message.channel, 'https://r.sine.com/?_=0')

    elif message.content.lower().startswith("im ") or message.content.lower().startswith("i'm "):
        await client.send_message(message.channel, "Hi " + message.content.partition(" ")[2] + ", I'm the FBI")



client.run('NDczMDY5NDY1MDUxODU2ODk2.Dt0MZg.igeJpA81VFBjslLlZtAASi2o9pU') 