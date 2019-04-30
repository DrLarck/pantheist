'''
Manages the check function that tells if it's a direct message or not.

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time

async def is_dm(ctx):
    '''
    Check if a command is used in direct message channel.
    Returns False if it's the case, True if it's not

    Return: bool
    '''
    # We're using a reversed logic because the check will block
    # the command if False is returned

    # Init
    channel = ctx.message.channel
    dm_channel = discord.DMChannel

    if(type(channel) == dm_channel):
        return(False)
    
    else:
        return(True)