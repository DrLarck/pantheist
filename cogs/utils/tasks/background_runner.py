'''
Manages to run the background tasks

Last update: 24/04/19
'''
# Dependancies
from cogs.background.presence import Discord_PresenceUpdater

def Background_Task_Runner(client):
    '''
    Runs the different background tasks

    Return: void
    '''
    # To run a background task we only need to use the asyncio event loop
    # as following 
    client.loop.create_task(Discord_PresenceUpdater(client))