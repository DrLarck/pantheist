'''
Manages the creation of auto-mod logs.

Last update: 29/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.utils import get

from configuration.global_config import LOGGER
from configuration.graphic_config import KICK_COLOR, MUTE_COLOR, WARN_COLOR, BAN_COLOR, UNMUTE_COLOR
from cogs.utils.functions.readability.embed import Basic_Embed

async def Pantheist_mod_logger(client, caller_object, target_object, server_object, log_origin, duration=None, reason=None):
    '''
    Send messages to the logs channel
    The log_origin represents the moderation action performed

    Return: discord.Message
    '''
    # Init
    log_origin = log_origin.upper().strip().split()
    logs_channel = get(server_object.text_channels, name=LOGGER)

    # Set the behaviour in function of the log_origin

    # BAN
    if(log_origin[0] == 'BAN'):
        # Init
        ban_log = Basic_Embed(client, title='Ban', color=BAN_COLOR)
        ban_n = '{}\'s action performed on {} :'.format(caller_object.name, target_object.name)

        if(reason == None):
            ban_desc = '{} has been banned, no reason provided.'.format(target_object.name)
        
        else:
            ban_desc = '{} has been banned for the following reason : *"{}"*'.format(target_object.name, reason)
        
        ban_log.add_field(name=ban_n, value=ban_desc, inline=False)

        try:
            await logs_channel.send(embed=ban_log)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M')
            print('{} - Error in cogs.utils.functions.auto_mode.logs_ : Try @BAN : {}'.format(error_time, error))
            pass

    # KICK
    if(log_origin[0] == 'KICK'):
        # Init
        kick_log = Basic_Embed(client, title='Kick', color=KICK_COLOR)
        kick_n = '{}\'s action performed on {} :'.format(caller_object.name, target_object.name)
        
        if(reason == None):
            kick_desc = '{} has been kicked, no reason provided.'.format(target_object.name)
        
        else:
            kick_desc = '{} has been kick for the following reason : *"{}"*'.format(target_object.name, reason)
        
        kick_log.add_field(name=kick_n, value=kick_desc, inline=False)

        try:
            await logs_channel.send(embed=kick_log)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M')
            print('{} - Error in cogs.utils.functions.auto_mode.logs_ : Try @KICK : {}'.format(error_time, error))
            pass
    
    # MUTE
    if(log_origin[0] == 'MUTE'):
        # Init
        mute_log = Basic_Embed(client, title='Mute', color=MUTE_COLOR)
        mute_n = '{}\'s action performed on {} :'.format(caller_object.name, target_object.name)

        if(reason == None):
            mute_desc = '{} has been muted, no reason provided.'.format(target_object.name)
        
        else:
            mute_desc = '{} has been muted for the following reason : *"{}"*'.format(target_object.name, reason)
        
        mute_log.add_field(name=mute_n, value=mute_desc, inline=False)

        try:
            await logs_channel.send(embed=mute_log)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M')
            print('{} - Error in cogs.utils.functions.auto_mode.logs_ : Try @MUTE : {}'.format(error_time, error))
            pass
    
    if(log_origin[0] == 'UNMUTE'):
        # Init
        unmute_log = Basic_Embed(client, title='Unmute', color=UNMUTE_COLOR)
        unmute_n = '{}\'s action performed on {} :'.format(caller_object.name, target_object.name)

        if(reason == None):
            unmute_desc = '{} has been unmutted, no reason provided.'.format(target_object.name)
        
        else:
            unmute_desc = '{} has been unmutted for the following reason : *"{}"*'.format(target_object.name, reason)
        
        unmute_log.add_field(name=unmute_n, value=unmute_desc, inline=False)

        try:
            await logs_channel.send(embed=unmute_log)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M')
            print('{} - Error in cogs.utils.functions.auto_mode.logs_ : Try @UNMUTE : {}'.format(error_time, error))
            pass
    
    # WARN
    if(log_origin[0] == 'WARN'):
        # Init
        warn_log = Basic_Embed(client, title='Warn', color=WARN_COLOR)
        warn_n = '{}\'s action performed on {} :'.format(caller_object.name, target_object.name)

        if(reason == None):
            warn_desc = '{} has been warned, no reason provided.'.format(target_object.name)
        
        else:
            warn_desc = '{} has been warned for the following reason : *"{}"*'.format(target_object.name, reason)
        
        warn_log.add_field(name=warn_n, value=warn_desc, inline=False)

        try:
            await logs_channel.send(embed=warn_log)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M')
            print('{} - Error in cogs.utils.functions.auto_mode.logs_ : Try @UNMUTE : {}'.format(error_time, error))
            pass