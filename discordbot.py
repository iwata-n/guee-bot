import os
import discord

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ぐえー'):
        await message.channel.send('ぐえー')

client.run(token)
