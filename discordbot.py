from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
　　if message.author == client.user:
　　　　return

　　if message.content.startswith('$ぐえー'):
　　　　await message.channel.send('ぐえー')

bot.run(token)
