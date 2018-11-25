import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('$'):
        command = message.content[1:]
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


client.run('NDczMDY5NDY1MDUxODU2ODk2.DtqzJA.KI4aFReRG-oFDgcaMVXePpB6uXY') 