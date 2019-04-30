'''
Allows us to create and configure embeds faster.

Last update: 28/04/19
'''
# Dependancies
import discord

from configuration.global_config import V_MAJ,V_MED,V_MIN,V_PHASE
from configuration.graphic_config import THEME_COLOR

def Basic_Embed(client, title=None, thumb=None, footer=None, color=None):
    '''
    Generates a pre-configured embed.

    Return: discord.Embed
    '''
    # Init
    bot_avatar = client.user.avatar_url
    basic_footer = '{} v{}.{}.{} - {} | © 2019 - DrLarck\'s - MIT License'.format(client.user.name, V_MAJ, V_MED, V_MIN, V_PHASE)
    embed_color = THEME_COLOR

    if(color != None):
        embed_color = color

    if(title != None):
        basic_embed = discord.Embed(title=title, colour=embed_color)
    
    else:
        basic_embed = discord.Embed(colour=embed_color)
    
    if(thumb != None):
        basic_embed.set_thumbnail(url=thumb)
    
    if(footer != None):
        basic_embed.set_footer(text=footer)
    
    else:
        basic_embed.set_footer(text=basic_footer)
    
    basic_embed.set_author(name=client.user.name, icon_url=bot_avatar)

    return(basic_embed)
