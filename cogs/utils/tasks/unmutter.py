'''
Manages the unmutter behaviour

Last update: 29/04/19
'''
# Dependancies
import discord, asyncio, time
from discord.utils import get

from configuration.background_config import UNBANNER_TIMER
from configuration.global_config import MUTE_ROLE

from data.queries.select.user_pilory import User_mute_until

async def Unmutter(client):
    '''
    Unmute a member the duration time is passed.

    Return: void
    '''
    await client.wait_until_ready()

    while not client.is_closed():
        # Init
        server_list = client.guilds

        for server in server_list:
            await asyncio.sleep(0)

            try:
                pantheist_mute_role = get(server.roles, name=MUTE_ROLE)
            
            except Exception as error:
                error_time = time.strftime('%d/%m/%y - %H:%M')
                print('{} - Error in cogs.utils.tasks.unmutter.Unmutter : Try#1 : {}'.format(error_time, error))
                pass

            server_members = server.members 

            for member in server_members:
                member_roles = member.roles

                if pantheist_mute_role in member_roles:
                    mute_until = await User_mute_until(client, member, server)
                    time_now = time.time()

                    if(time_now >= mute_until):
                        await member.remove_roles(pantheist_mute_role, reason='[AUTO-UNMUTE]')

                        try:
                            await member.send('You\'ve been unmutted from `{}`.'.format(server.name))
                        
                        except discord.errors.Forbidden:
                            pass
                    
                    else:
                        pass
        
        await asyncio.sleep(UNBANNER_TIMER)