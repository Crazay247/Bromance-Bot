import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix='.')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    


client.run('NzY4OTk2ODM3MjYwMDAxMzUw.X5ImHQ.4pqKTwYaE5c9HV-lvkyZS-xKBYE')