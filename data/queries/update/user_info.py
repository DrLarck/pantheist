'''
These functions update the user columns from the user_info table

Last update: 30/04/19
'''
# Dependancies
import asyncpg, time

async def Update_user_lang(client, user_object, lang):
    '''
    Update the user_lang column

    Return: void
    '''
    # Init
    conn = await client.db.acquire()
    query = 'UPDATE user_info SET user_lang= $1 WHERE user_id= $2'

    try:
        await conn.execute(query, lang, user_object.id)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in data.queries.update.user_info.Update_user_lang : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)