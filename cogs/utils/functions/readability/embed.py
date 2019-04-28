'''
Allows us to create and configure embeds faster.

Last update: 28/04/19
'''
# Dependancies
import discord

from configuration.global_config import THEME_COLOR, V_MAJ,V_MED,V_MIN,V_PHASE

def Basic_Embed(client, title=None, thumb=None, footer=None):
    '''
    Generates a pre-configured embed.

    Return: discord.Embed
    '''
    # Init
    bot_avatar = client.user.avatar_url
    basic_footer = '{} v{}.{}.{} - {} | © 2019 - DrLarck\'s - MIT License'.format(client.user.name, V_MAJ, V_MED, V_MIN, V_PHASE)

    if(title != None):
        basic_embed = discord.Embed(title=title, colour=THEME_COLOR)
    
    else:
        basic_embed = discord.Embed(colour=THEME_COLOR)
    
    if(thumb != None):
        basic_embed.set_thumbnail(url=thumb)
    
    if(footer != None):
        basic_embed.set_footer(text=footer)
    
    else:
        basic_embed.set_footer(text=basic_footer)
    
    basic_embed.set_author(name=client.user.name, icon_url=bot_avatar)

    return(basic_embed)
