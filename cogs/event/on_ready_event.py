'''
Do something when the bot is ready to use.

Last update: 24/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.ext import commands
from discord.ext.commands import Cog

from configuration.global_config import V_MAJ,V_MED,V_MIN,V_PHASE

class On_Ready(Cog):
    def __init__(self, client):
        self.client = client
    
    @Cog.listener()
    async def on_ready(self):
        '''
        Displays a message in the terminal when the bot is ready to use.
        '''
        execution_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        bot_name = self.client.user.name
        console_message = '\n\n{} v{}.{}.{} - {}\n\n{}\n----------------------------------------'.format(bot_name, V_MAJ, V_MED, V_MIN, V_PHASE, execution_time)

        print(console_message)
        
def setup(client):
    client.add_cog(On_Ready(client))