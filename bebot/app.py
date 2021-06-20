import discord
from dotenv import dotenv_values

ENV = dotenv_values()
bebot = discord.Client()

@bebot.event
async def on_ready():
    print('HELLO WORLD!')

bebot.run(ENV['TOKEN'])