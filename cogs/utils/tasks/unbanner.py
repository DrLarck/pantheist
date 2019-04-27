'''
Manages the unbanner feature.

Last update: 27/04/19
'''
# Dependancies
import discord, asyncio, time

from configuration.background_config import UNBANNER_TIMER

from data.queries.select.user_pilory import Is_perma_ban, User_ban_until

async def Unbanner(client):
    '''
    Unban a user that has been temp-banned
    '''

    await client.wait_until_ready()

    while not client.is_closed():
        # We retrieve all the guilds the client is connected to

        all_servers = []
        all_servers = client.guilds
        current_time = time.time()

        # Then we proceed to the unban process

        for server in all_servers:
            # First we retrieve the banned member in each server the bot is in

            bans = await server.bans() 

            for user in bans:
                # Then we check into the database until when a user has been banned to
                # know if it's time to unban him or not
                # bans is a nametupled that returns BanEntry as 1 and reason as 0
                
                user_ban_until = await User_ban_until(client, user[1], server)
                user_perma_ban = await Is_perma_ban(client, user[1], server)

                if(current_time > user_ban_until and user_perma_ban == False):
                    await server.unban(user[1], reason='[AUTO-UNBAN]')
                
                else:
                    pass
    
        await asyncio.sleep(UNBANNER_TIMER)
