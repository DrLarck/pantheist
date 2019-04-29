'''
These functions allows you to update the value of the user_pilory table.

Last update: 27/04/19
'''
# Dependancies
import asyncpg, asyncio, time

async def Update_user_warns(client, user_object, new_amount):
    '''
    Replace the user_warns value by the given new_amount

    Return: void
    '''
    # Init
    conn = await client.db.acquire()
    query = 'UPDATE user_pilory SET user_warns= $1 WHERE user_id= $2'

    try:
        await conn.execute(query, new_amount, user_object.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - data.queries.update.user_pilory.Update_user_warns : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Update_ban_until(client, user_object, server_object, ban_until):
    '''
    Update the value of the column user_ban_until in user_pilory.
    You need to pass the date as seconds, otherwise it couldn't work properly.

    Return: void
    '''
    # Init
    conn = await client.db.acquire()
    query = 'UPDATE user_pilory SET user_ban_until= $1 WHERE user_id= $2 AND in_server= $3'

    try:
        await conn.execute(query, ban_until, user_object.id, server_object.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - data.queries.update.user_pilory.Update_ban_until : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Update_user_perma_ban(client, user_object, server_object, perma_ban):
    '''
    Set the new state of the user.
    You need to pass the 'perma_ban' value as an int.
    perma_ban = 1 = True
    perma_ban = 0 = False

    Return: void
    '''
    # Init
    conn = await client.db.acquire()
    query = 'UPDATE user_pilory SET user_perma_ban= $1 WHERE user_id= $2 AND in_server= $3'

    try:
        await conn.execute(query, perma_ban, user_object.id, server_object.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - data.queries.update.user_pilory.Update_user_warns : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Update_mute_until(client, user_object, server_object, mute_until):
    '''
    Update the date of the user's mute limit

    Return: void
    '''
    # Init
    conn = await client.db.acquire()
    query = 'UPDATE user_pilory SET user_mute_until= $1 WHERE user_id= $2 AND in_server= $3'

    try:
        await conn.execute(query, mute_until, user_object.id, server_object.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - data.queries.update.user_pilory.Update_mute_until : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)