'''
Manages the mute command.

Last update: 29/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog
from discord.utils import get

from cogs.utils.translation.translation import Translator
from cogs.utils.functions.auto_mod.perm_overwrite import Mute_permissions
from configuration.global_config import MUTE_ROLE

from data.queries.update.user_pilory import Update_mute_until

class Mute(Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, target: discord.Member, duration: int, *, reason=None):
        '''
        Allows the user to mute a member. If the mute role doesn't exist in the server
        we create it.
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author
        server = ctx.message.guild
        pantheist_mute_role = MUTE_ROLE
        get_pantheist_mute_role = get(server.roles, name=pantheist_mute_role)
        mute_color = discord.Color(0xff0000)
        server_roles = server.roles

        # The user can't mute himself

        if(caller == target):
            return

        # If the role doesn't exists, we create it

        if not get_pantheist_mute_role in server_roles:
            await server.create_role(name=pantheist_mute_role, colour=mute_color)

        # Now we set all the server's channels perm to avoid the muted user to talk in 
        # these channels

        get_pantheist_mute_role = get(server.roles, name=pantheist_mute_role)
        await Mute_permissions(get_pantheist_mute_role, server)

        # Now that everything is good, we apply the role to the user and we set the duration
        if(reason == None):
            await target.add_roles(get_pantheist_mute_role)
            await ctx.send(_('<@{}> I\'ve muted **{}** for **{:,}** seconds.').format(caller.id, target.name, duration))
            
            # Now we try to send a DM to the target

            try:
                await target.send(_('<@{}> You\'ve been muted for **{:,}** seconds by **{}** in `{}`.\n*No reason provided.*').format(target.id, duration, caller.name, server.name))
            
            except discord.errors.Forbidden:
                pass
        
        else:
            await target.add_roles(get_pantheist_mute_role, reason=reason)
            await ctx.send(_('<@{}> I\'ve muted **{}** for **{:,}** seconds.').format(caller.id, target.name, duration))

            # Now we try to send a DM to the target

            try:
                await target.send(_('<@{}> You\'ve been muted for **{:,}** seconds by **{}** in `{}`.\nReason : *"{}"*').format(target.id, duration, caller.name, server.name, reason))
            
            except discord.errors.Forbidden:
                pass

        # Now we set the duration time

        time_now = time.time()
        duration = time_now + duration
        await Update_mute_until(self.client, target, server, duration)
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, target: discord.Member):
        '''
        Simply remove the target's muted role
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author
        server = ctx.message.guild
        pantheist_mute_role = get(server.roles, name=MUTE_ROLE)

        await target.remove_roles(pantheist_mute_role, reason='Removed by {}'.format(caller.name))
        await ctx.send(_('<@{}> I\'ve unmutted **{}**').format(caller.id, target.name))

def setup(client):
    client.add_cog(Mute(client))