'''
Manages the help command.

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from cogs.utils.translation.translation import Translator
from cogs.utils.functions.readability.embed import Basic_Embed
from cogs.utils.functions.check.direct_message import is_dm
from configuration.global_config import PREFIX

class Help(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.check(is_dm)
    async def help(self, ctx):
        '''
        Displays the help message
        '''
        # Init
        _ = await Translator(self.client, ctx)
        help_embed = Basic_Embed(self.client)
        help_title = _('Help')
        help_desc = _('Welcome in the help panel.\nA parameter between [square brackets] is **necessary**, otherwise the command will not work.\nA parameter between {braces} is **optional**.\nThe \'**@**\' symbol means that the command needs a **mention**.\nBy default, the temp-ban is set to 1 day.\nPrefix : `**`')

        # Commands name
        ban_n = _('ban [@user] {time: seconds} {"reason"}')
        mute_n = _('mute [@user] [duration seconds] {"reason"}')
        kick_n = _('kick [@user] {reason}')
        warn_n = _('warn | w [@user] {"reason"}')

        # Commands description
        ban_desc = _('[Perm : ban members] - Allows you to ban a member from the server.\nIf it\'s a **temp-ban**, please pass the time as **seconds**.\nAlso pass the **reason** between "quotation marks".')
        mute_desc = _('[Perm : kick members] - Allow you to mute a member for certain amount of time (in second).')
        kick_desc = _('[Perm : kick members] - Allows you to kick a member from the server.\n')
        warn_desc = _('[Perm : kick members, ban members] - Allows you to warn a user, after a certain amount of warns the warn system will invite you to kick/temp-ban the user.')

        # Set the display
        help_embed.add_field(name=help_title, value=help_desc, inline= False)

        help_embed.add_field(name=ban_n, value=ban_desc, inline=False)
        help_embed.add_field(name=mute_n, value=mute_desc, inline=False)
        help_embed.add_field(name=kick_n, value=kick_desc, inline= False)
        help_embed.add_field(name=warn_n, value=warn_desc, inline= False)

        await ctx.send(embed=help_embed)

def setup(client):
    client.add_cog(Help(client))