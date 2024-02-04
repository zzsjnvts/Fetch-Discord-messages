import discord
from discord.ext import commands

channel_id = input("enter channel id:")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    try:
        channel = bot.get_channel(channel_id)
        if channel:
            async for message in channel.history(limit=None):
                print(f'{message.author.name}: {message.content}')
        else:
            print("Channel not found. Make sure the bot has access to the specified channel.")
    except Exception as e:
        print(f'Error: {e}')


bot.run()
