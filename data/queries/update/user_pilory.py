'''
These functions allows you to update the value of the user_pilory table.

Last update: 26/04/19
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