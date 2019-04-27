'''
Manages to run the background tasks

Last update: 27/04/19
'''
# Dependancies
from cogs.utils.tasks.presence import Discord_PresenceUpdater
from cogs.utils.tasks.unbanner import Unbanner
from cogs.utils.database.database_runner import Connect_To_Database, Init_Tables

def Background_Task_Runner(client):
    '''
    Runs the different background tasks

    Return: void
    '''
    # To run a background task we only need to use the asyncio event loop
    # as following 
    client.loop.create_task(Unbanner(client))
    client.loop.create_task(Discord_PresenceUpdater(client))
    client.loop.run_until_complete(Connect_To_Database(client))
    client.loop.run_until_complete(Init_Tables(client))