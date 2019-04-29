'''
Manages the kick command behaviour

Last update: 28/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from configuration.global_config import PREFIX
from cogs.utils.translation.translation import Translator

from cogs.utils.functions.auto_mod.wf_decision import Wait_for_kick

class Kick(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
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

def setup(client):
    client.add_cog(Kick(client))