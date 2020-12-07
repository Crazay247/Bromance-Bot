import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
@client.command()
async def clear(ctx, amount=3):
     await ctx.channel.purge(limit=amount)


client.run('bot token')
