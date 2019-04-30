'''
Manages the user's language setting.

Last update: 30/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from cogs.utils.translation.translation import Translator
from cogs.utils.functions.check.direct_message import is_dm

from data.queries.update.user_info import Update_user_lang

class Language(Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['lang'])
    @commands.check(is_dm)
    async def language(self, ctx, lang: str):
        '''
        Allows the user to select a language.
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author
        lang = lang.upper().strip().split()

        if(lang[0] == 'FR'):
            await Update_user_lang(self.client, caller, 'FR')
            await ctx.send('<@{}> La langue sélectionnée est maintenant le français.'.format(caller.id))
        
        elif(lang[0] == 'EN'):
            await Update_user_lang(self.client, caller, 'EN')
            await ctx.send('<@{}> You\'ve set the language to english.'.format(caller.id))
        
        else:
            await ctx.send(_('<@{}> Please select a language between `EN` and `FR`.'.format(caller.id)))
    
    '''
    Error handler
    '''
    @language.error 
    async def lang_error(self, ctx, error):
        '''
        Language command error handler
        '''
        # Init
        _ = await Translator(self.client, ctx)
        caller = ctx.message.author

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(_('<@{}> Error : a required argument is missing.').format(caller.id))
        
        if isinstance(error, commands.BadArgument):
            await ctx.send(_('<@{}> An invalid argument has been passed.').format(caller.id))

def setup(client):
    client.add_cog(Language(client))