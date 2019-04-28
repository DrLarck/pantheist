'''
Thanks to these functions, the bot will wait until the user gives a correct answer.

Last update: 27/04/19
'''
# Dependancies
import asyncio, discord, time

from configuration.global_config import PREFIX
from configuration.auto_mod_config import BAN_LIMIT
from cogs.utils.translation.translation import Translator

from data.queries.select.user_pilory import User_warn_amount
from data.queries.update.user_pilory import Update_ban_until

async def Wait_for_kick(client, ctx, server, caller, target, reason=None):
    '''
    If the caller says 'yes' or 'no' using the prefix, the target is kicked from the server.

    Return: void
    '''
    # Init
    _ = await Translator(client, ctx)

    def Check_author(message):
        if(message.author == caller):
            message_content = message.content 
            message_content = message_content.upper()
            yes_ans, no_ans = '{}YES'.format(PREFIX[0]), '{}NO'.format(PREFIX[0])

            if(message_content == yes_ans or message_content == no_ans):
                return(True)
            
            else:
                return(False)
    
    # Here we're waiting for the caller decision
    # if he takes too much time, we cancel everything

    try:
        message = await client.wait_for('message', timeout=120, check=Check_author)
    
    except asyncio.TimeoutError:
        await ctx.send(_('<@{}> *[KICK]* Aborting.').format(caller.id), delete_after=5)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in cogs.utils.functions.auto_mod.wf_decision.Wait_for_kick : Try#1 : {}'.format(error_time, error))
        pass
    
    else:
        message_content = message.content 
        message_content = message_content.upper()
        yes_ans, no_ans = '{}YES'.format(PREFIX[0]), '{}NO'.format(PREFIX[0])

        if(message_content == yes_ans):
            try:
                user_warns = await User_warn_amount(client, target, server)
                await ctx.send(_('<@{}> Kicking **{}**.').format(caller.id, target.name))

                if(reason == None):
                    await server.kick(target, reason='[KICK] Kicked after {} warns by {}.'.format(user_warns, caller))
                    return
                
                else:
                    await server.kick(target, reason=reason)
                    return
            
            except discord.errors.Forbidden:
                await ctx.send(_('<@{}> I\'m not able to kick this user.').format(caller.id), delete_after=5)
                return
        
        if(message_content == no_ans):
            await ctx.send(_('<@{}> *[KICK]* Cancellation.').format(caller.id))
            return

async def Wait_for_ban(client, ctx, server, caller, target, reason=None):
    '''
    If the caller says 'yes' or 'no' using the prefix, the target is banned from the server.

    Return: void
    '''
    # Init
    _ = await Translator(client, ctx)

    def Check_author(message):
        if(message.author == caller):
            message_content = message.content 
            message_content = message_content.upper()
            yes_ans, no_ans = '{}YES'.format(PREFIX[0]), '{}NO'.format(PREFIX[0])

            if(message_content == yes_ans or message_content == no_ans):
                return(True)
            
            else:
                return(False)
    
    # Here we're waiting for the caller decision
    # if he takes too much time, we cancel everything

    try:
        message = await client.wait_for('message', timeout=120, check=Check_author)
    
    except asyncio.TimeoutError:
        await ctx.send(_('<@{}> *[BAN]* Aborting.').format(caller.id), delete_after=5)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in cogs.utils.functions.auto_mod.wf_decision.Wait_for_ban : Try#1 : {}'.format(error_time, error))
        pass
    
    else:
        message_content = message.content 
        message_content = message_content.upper()
        yes_ans, no_ans = '{}YES'.format(PREFIX[0]), '{}NO'.format(PREFIX[0])

        if(message_content == yes_ans):
            try:
                user_warns = await User_warn_amount(client, target, server)
                time_now = time.time()
                ban_until = time_now + BAN_LIMIT

                await ctx.send(_('<@{}> Banning **{}**.').format(caller.id, target.name))
                if(reason == None):
                    await server.ban(target, reason='[BAN] Banned after {} warns by {}.'.format(user_warns, caller))
                    await Update_ban_until(client, target, server, ban_until)
                    return

                else:
                    await server.ban(target, reason=reason)
                    await Update_ban_until(client, target, server, ban_until)
                    return
            
            except discord.errors.Forbidden:
                await ctx.send(_('<@{}> I\'m not able to ban this user.').format(caller.id), delete_after=5)
                return
        
        if(message_content == no_ans):
            await ctx.send(_('<@{}> *[BAN]* Cancellation.').format(caller.id))
            return