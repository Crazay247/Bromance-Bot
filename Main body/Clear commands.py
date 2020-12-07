import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')
@client.command()
async def clear(ctx, amount=3):
     await ctx.channel.purge(limit=amount)


client.run('NzY4OTk2ODM3MjYwMDAxMzUw.X5ImHQ.4pqKTwYaE5c9HV-lvkyZS-xKBYE')