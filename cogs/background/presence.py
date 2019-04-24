'''
Manages the bot's presence on discord

Last update: 24/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands

from configuration.background_config import PRESENCE_UPDATER_TIMER
from configuration.global_config import V_MAJ,V_MED,V_MIN,V_PHASE

async def Discord_PresenceUpdater(client):
    '''
    Update the bot's presence on Discord

    Return: void
    '''
    await client.wait_until_ready()

    while not client.is_closed():

        server_count = len(client.guilds)
        version = 'v{}.{}.{} - {}'.format(V_MAJ,V_MED,V_MIN,V_PHASE)
        presence = '{} servers | {}'.format(server_count, version)
        activity = discord.Game(name=presence)

        await client.change_presence(activity=activity)
    
        # Sleep
        await asyncio.sleep(PRESENCE_UPDATER_TIMER)