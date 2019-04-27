'''
These functions returns values from the user_pilory table.

Last update: 27/04/19
'''
# Dependancies
import asyncpg, asyncio, time

async def User_warn_amount(client, user_object, server_object):
    '''
    Return the value of user_warns

    Return: int
    '''
    # Init
    user_warns = 0
    conn = await client.db.acquire()
    query = 'SELECT user_warns FROM user_pilory WHERE user_id= $1 AND in_server= $2'

    try:
        user_warns = await conn.fetchval(query, user_object.id, server_object.id)
        user_warns = int(user_warns)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in data.queries.select.user_pilory.User_warn_amount : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(user_warns)

async def User_ban_until(client, user_object, server_object):
    '''
    Returns the value as seconds of the date until the user is banned from a server.

    Return: int
    '''
    # Init
    ban_until = 0
    conn = await client.db.acquire()
    query = 'SELECT user_ban_until FROM user_pilory WHERE user_id= $1 AND in_server= $2'

    try:
        ban_until = await conn.fetchval(query, user_object.id, server_object.id)
        ban_until = int(ban_until)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in data.queries.select.user_pilory.User_ban_until : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(ban_until)

async def Is_perma_ban(client, user_object, server_object):
    '''
    If the user is perma_ban from a server returns True, else returns False.

    Return: bool
    '''
    # Init
    is_perma_ban = 0
    conn = await client.db.acquire()
    query = 'SELECT user_perma_ban FROM user_pilory WHERE user_id= $1 AND in_server= $2'

    try:
        is_perma_ban = await conn.fetchval(query, user_object.id, server_object.id)
        is_perma_ban = int(is_perma_ban)

    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in data.queries.select.user_pilory.Is_perma_ba, : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    if(is_perma_ban == 0):
        return(False)
    
    elif(is_perma_ban == 1):
        return(True)
    
    else:
        return(False)