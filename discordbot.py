import os
import discord
import requests

guee_api = os.environ['GUEE_API_HOST']
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ぐえー'):
        resp = requests.get(guee_api)
        text = resp.text
        print(f"response={text}")
        await message.channel.send(text)

client.run(token)
