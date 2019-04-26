'''
These functions return the user's informations stored in the user_info table

Last update: 26/04/19
'''
# Dependancies
import asyncpg, asyncio, time

async def User_language(client, user_object):
    '''
    Return the user's language acronym such as 'EN' or 'FR'

    Return: str
    '''
    # Init
    user_lang = ''
    conn = await client.db.acquire()
    query = 'SELECT user_lang FROM user_info WHERE user_id= $1'

    try:
        user_lang = await conn.fetchval(query, user_object.id)
        user_lang = str(user_lang)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in data.queries.select.user_info.User_language : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)
    
    return(user_lang)