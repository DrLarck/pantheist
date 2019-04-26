'''
These functions returns values from the user_pilory table.

Last update: 26/04/19
'''
# Dependancies
import asyncpg, asyncio, time

async def User_warn_amount(client, user_object, server):
    '''
    Return the value of user_warns

    Return: int
    '''
    # Init
    user_warns = 0
    conn = await client.db.acquire()
    query = 'SELECT user_warns FROM user_pilory WHERE user_id= $1 AND in_server= $2'

    try:
        user_warns = await conn.fetchval(query, user_object.id, server.id)
        user_warns = int(user_warns)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in data.queries.select.user_pilory.User_warn_amount : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(user_warns)