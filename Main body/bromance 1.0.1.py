import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.Game('with your feelings'))
   

@client.command()
async def info(ctx):
    
    
        helpEmbed = discord.Embed(title="Help", description = "Im happy to help", color=0x00ff00 )
        helpEmbed.add_field(name='These are my commands',value='version', inline=False)
        helpEmbed.add_field(name='Total commands', value='1', inline=False)
        helpEmbed.set_footer(text='More commands to be added soon ')
        helpEmbed.set_author(name='Crazay')

        await ctx.message.channel.send(embed=helpEmbed)
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)} ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful." ]
    await ctx.send(f'The question :{question}\n Answer: {random.choice(responses)}' )

client.run('NzY4OTk2ODM3MjYwMDAxMzUw.X5ImHQ.4pqKTwYaE5c9HV-lvkyZS-xKBYE')    