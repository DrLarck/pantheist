'''
Manages the on message event.

Last update: 24/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from data.queries.insert.user_info import Insert_user_info, Insert_init_pilory

class On_Message(Cog):
    def __init__(self, client):
        self.client = client
    
    @Cog.listener()
    async def on_message(self, message):
        '''
        Do something when the client sees a message

        Return: void
        '''
        if(message.author != self.client.user):
            # Var
            user = message.author
            server = message.guild
            date = time.strftime('%d/%m/%y', time.gmtime())
            await Insert_user_info(self.client, user, date)
            await Insert_init_pilory(self.client, user, server)

def setup(client):
    client.add_cog(On_Message(client))