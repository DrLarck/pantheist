'''
These functions allows you to insert user informations into the database

Last update: 24/04/19
'''
# Dependancies
import asyncpg, time

async def Insert_user_info(client, user_object, date):
    '''
    Insert the passed informations about the user into the database

    Return: void
    '''
    conn = await client.db.acquire()

    query = 'INSERT INTO user_info(user_name, user_id, user_register_date, user_messages) VALUES($1, $2, $3, DEFAULT)'

    try:
        await conn.execute(query, user_object.name, user_object.id, date)
    
    except asyncpg.UniqueViolationError:  # Ignore the unique constraint error
        pass
        
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in insert.user_info.Insert_user_info : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Insert_init_pilory(client, user_object, server):
    '''
    Init the pilory by creating a sheet of the user in it

    Return: void
    '''
    conn = await client.db.acquire()
    query = 'INSERT INTO user_pilory(user_name, user_id, in_server) VALUES($1, $2, $3)'

    try:
        await conn.execute(query, user_object.name, user_object.id, server.id)
    
    except asyncpg.UniqueViolationError:  # Ignore the unique constraint error
        pass
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M')
        print('{} - Error in data.queries.insert.user_info.Insert_init_pilory : Try#1 : {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)