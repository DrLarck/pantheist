'''
Manages the warn command

Last update: 24/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog
from cogs.utils.translation.translation import Translator

from data.queries.select.user_pilory import User_warn_amount
from data.queries.update.user_pilory import Update_user_warns
from data.queries.insert.user_info import Insert_init_pilory

class Warn(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['w'])
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user: discord.Member, *, reason= None):
        '''
        Allows a member that has the right permission to warn a member
        After a certain amount of warns, the member is kicked from the server
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author
        server = ctx.message.guild
        user_warns = await User_warn_amount(self.client, user, server)
        await Insert_init_pilory(self.client, user, server)

        # Now we've the amount of the user's warns we can update it
        user_warns += 1
        await Update_user_warns(self.client, user, user_warns)

        # Now we check, if any reason has been specified for the warn
        # If a reason has been specified, we send a DM to the user to notice him
        # otherwise we send a DM without the reason
        if(reason != None):
            # Here we do a Try statment to see if the user allows receiving DMs
            # If he doesnt, we send the message in the current channel.
            try:
                await user.send(_('<@{}> You\'ve been warned by **{}** in `{}` for the following reason : *"{}"*\nYou have now **{:,}** warns in this server.').format(user.id, caller.name, server.name, reason, user_warns))
            
            except discord.errors.Forbidden:
                channel = ctx.message.channel
                await channel.send('<@{}> You\'ve been warned by **{}** in `{}` for the following reason : *"{}"*\nYou have now **{:,}** warns in this server.'.format(user.id, caller.name, server.name, reason, user_warns))
        
        else:
            try:
                await user.send('<@{}> You\'ve been warned by **{}** in `{}`.\nYou have now **{:,}** warns in this server.'.format(user.id, caller.name, server.name, user_warns))
            
            except discord.errors.Forbidden:
                channel = ctx.message.channel
                await channel.send('<@{}> You\'ve been warned by **{}** in `{}`.\nYou have now **{:,}** warns in this server.'.format(user.id, caller.name, server.name, user_warns))

def setup(client):
    client.add_cog(Warn(client))