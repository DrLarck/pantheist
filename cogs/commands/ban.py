'''
Manages the ban feature.

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from configuration.global_config import PREFIX
from cogs.utils.translation.translation import Translator
from cogs.utils.functions.auto_mod.wf_decision import Wait_for_ban
from cogs.utils.functions.auto_mod.logs_ import Pantheist_mod_logger
from cogs.utils.functions.check.direct_message import is_dm

class Ban(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.check(is_dm)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target: discord.Member, ban_until=None, *, reason=None):
        '''
        Bans a member.
        ban_until : timer in seconds. 
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller, server = ctx.message.author, ctx.message.guild

        # The caller can't ban himself 

        if(caller == target):
            return
            
        # Now if the user has specified a ban limit we check if it's full digits
        # if it's not, it means that is a perma ban with a reason

        if(ban_until != None):
            if not ban_until.isdigit() :
                # If ban_until is not a numerical value it probably means that it's the reason
                # Also we couldnt work with a non numerical value so

                reason = ban_until
                ban_until = None
        
        if(ban_until == None):
            # If there is no ban_until it means its a perma ban

            await ctx.send(_('<@{}> You\'re about to **perma-ban {}**, are you sure about that ?\n*(Type `{}yes` or `{}no` to proceed)*').format(caller.id, target.name, PREFIX[0], PREFIX[0]))
            if(reason == None):
                await Wait_for_ban(self.client, ctx, server, caller, target)
            
            else:
                await Wait_for_ban(self.client, ctx, server, caller, target, reason=reason)
        
        elif(ban_until.isdigit()):
            ban_until = int(ban_until)
            await ctx.send(_('<@{}> You\'re about to **ban {}** for **{:,}** seconds. Are you sure about that ?\n*(Type `{}yes` or `{}no` to proceed)*').format(caller.id, target.name, ban_until, PREFIX[0], PREFIX[0]))
            if(reason == None):
                await Wait_for_ban(self.client, ctx, server, caller, target, ban_until=ban_until)
            
            else:
                await Wait_for_ban(self.client, ctx, server, caller, target, reason=reason, ban_until=ban_until)

    '''
    Errors handler
    '''
    @ban.error 
    async def ban_error(self, ctx, error):
        '''
        Ban command error handler
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(_('<@{}> Error : a required argument is missing.').format(caller.id))
        
        if isinstance(error, commands.BadArgument):
            await ctx.send(_('<@{}> Error : I can\'t find this user.').format(caller.id))
                
def setup(client):
    client.add_cog(Ban(client))