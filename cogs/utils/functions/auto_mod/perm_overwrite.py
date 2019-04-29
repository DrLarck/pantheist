'''
These functions overwrite permissions for all the channels in a server.

Last update: 29/04/19
'''
# Dependancies
import discord, asyncio, time

async def Mute_permissions(mute_role, server_object):
    '''
    Set the server's channels permissions for the role : 'Mute (pantheist)'

    Return: void
    '''
    guild_channels = server_object.text_channels

    for channel in guild_channels:
        await asyncio.sleep(0)
        await channel.set_permissions(mute_role, send_messages=False)