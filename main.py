'''
This is the main file. You can run the bot by executing this script.

Last update: 24/04/19
'''
# Dependancies 
import discord, asyncio, time, logging
from discord.ext import commands

from configuration.connection_config import BOT_TOKEN
from configuration.global_config import PREFIX, COGS
from cogs.utils.tasks.background_runner import Background_Task_Runner

# Client configuration
logging.basicConfig(level=logging.INFO)
client = discord.Client()
client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')  # We delete the basic help command to create our own

# Loading cogs
if __name__ == '__main__':
    for extension in COGS:
        try:
            client.load_extension(extension)
        
        except Exception as error:
            error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
            print('{} - Error in main.py : Loading cogs : {}'.format(error_time, error))
            pass

# Running tasks
Background_Task_Runner(client)
client.run(BOT_TOKEN)