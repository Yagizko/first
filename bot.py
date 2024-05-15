import discord
from discord.ext import commands
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def Kimsin(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def Naber(ctx):
    await ctx.send('İyiyim!')

@bot.command()
async def on_message(self, message):
    # we do not want the bot to reply to itself
    if message.author.id == self.user.id:
        return

    if message.content.startswith('guess'):
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await self.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}.')
bot.run("MTIzNzgzNjQ3OTYyNDExODI3Mw.GLEHvZ.sHoXnTImpwSVl3NUAmhQvymd8eaVW5u5nmcffw")
