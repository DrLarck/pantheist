'''
Manages the global error handler

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from cogs.utils.functions.check.direct_message import is_dm
from cogs.utils.translation.translation import Translator

class On_error(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    @commands.check(is_dm)
    async def on_command_error(self, ctx, error):
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(_('<@{}> You do not have the required permissions to proceed.').format(caller.id))
            pass

def setup(client):
    client.add_cog(On_error(client))