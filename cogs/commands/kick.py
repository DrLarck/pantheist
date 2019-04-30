'''
Manages the kick command behaviour

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from configuration.global_config import PREFIX
from cogs.utils.translation.translation import Translator

from cogs.utils.functions.auto_mod.wf_decision import Wait_for_kick
from cogs.utils.functions.auto_mod.logs_ import Pantheist_mod_logger
from cogs.utils.functions.check.direct_message import is_dm

class Kick(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.check(is_dm)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target: discord.Member, *, reason=None):
        '''
        Allows users who has the kick_members permission to kick a member
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller, server = ctx.message.author, ctx.message.guild

        # The caller can't kick himself

        if(caller == target):
            return

        await ctx.send(_('<@{}> You\'re about to **kick {}**, are you sure that you want to kick this user ?\n*(Type `{}yes` or `{}no` to proceed)*').format(caller.id, target.name, PREFIX[0], PREFIX[0]))
        if(reason == None):
            await Wait_for_kick(self.client, ctx, server, caller, target)
        
        else:
            await Wait_for_kick(self.client, ctx, server, caller, target, reason)

    '''
    Errors handler
    '''
    @kick.error 
    async def kick_error(self, ctx, error):
        '''
        Kick command error handler
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(_('<@{}> Error : a required argument is missing.').format(caller.id))
        
        if isinstance(error, commands.BadArgument):
            await ctx.send(_('<@{}> Error : I can\'t find this user.').format(caller.id))

def setup(client):
    client.add_cog(Kick(client))