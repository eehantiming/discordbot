'''
Discord bot to take attendance for sprints.
TODO: handle exit and send a bye message
'''
import os
import random
from datetime import datetime

from dotenv import load_dotenv
import discord
from discord.ext import commands

# Copy your channels ID here
TEXT_CHANNEL_ID = 854295641525059587
VOICE_CHANNEL_ID = 854295641525059588

intents = discord.Intents.default()
intents.members = True # For accessing member list 
bot = commands.Bot(intents=intents, command_prefix='!') # bot is a subclass of Client which has all the functionalities and mores.

# Initilize shared member list to append to
bot.member_list = []

@bot.event
async def on_ready():
    guild = bot.guilds[0]
    print(f'Bot active as {bot.user.name} in {guild.name}')
    for member in guild.members:
        if not member.bot:
            bot.member_list.append(member.name)
    print(f'{bot.member_list}')
    bot.text_channel = bot.get_channel(TEXT_CHANNEL_ID)
    bot.voice_channel = bot.get_channel(VOICE_CHANNEL_ID)
    await bot.text_channel.send(f':robot:{bot.user.name} is active!')


@bot.command(name='att', help='Takes attendance and shows who have not joined the Sprint voice channel')
async def att(ctx): # callback must accept ctx which is the Context surrounding the invoked command, such as the channel and guild that the command is called from.
    print('!att called')
    current_time = datetime.now().strftime("%H:%M:%S")
    await ctx.send(f':pencil: Taking attendance in {bot.voice_channel.name} at {current_time}! :clock930:')

    present_members = [member.name for member in bot.voice_channel.members]
    absent_members = set(bot.member_list) - set(present_members)
    await ctx.send(f':eyes: Absent: {len(absent_members)}/{len(bot.member_list)}\n' + ' -' + '\n -'.join(absent_members))

@bot.command(name='roll', help='Rolls a random number')
async def roll(ctx, number: int=100):
    value = random.randint(0, number)
    if value >= 0.9 * number:
        exclamation = 'Wow!'
    elif value <= 0.1 * number:
        exclamation = 'lol.'
    else:
        exclamation = 'Cool'
    await ctx.send(f':game_die: You rolled {value}. {exclamation}')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)



# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @client.event
# async def on_message(message):
#     # Checks that msg is not from this bot.
#     if message.author == client.user:
#         return

#     if message.content.startswith('!att'):
#         print('Attendance Called!')
#         current_time = datetime.now().strftime("%H:%M:%S")
#         #get attendance
#         await message.channel.send('')

# TOKEN = os.getenv('DISCORD_TOKEN')
# client.run(TOKEN)