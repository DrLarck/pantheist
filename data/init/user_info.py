'''
Create the tables about users.

Last update: 24/04/19
'''
# Dependancies
import asyncpg, asyncio, time

async def Create_User_Table(client):
    '''
    Create the user table which will store informations about him

    Return: void
    '''
    conn = await client.db.acquire()
    create_query = '''
    CREATE TABLE IF NOT EXISTS user_info(
        register_order SERIAL PRIMARY KEY,
        user_name TEXT DEFAULT 'NONE',
        user_id BIGINT,
        user_register_date TEXT DEFAULT 'NONE',
        user_lang TEXT DEFAULT 'EN',
        user_location TEXT DEFAULT 'NONE',
        user_messages BIGINT DEFAULT 0,
        user_level BIGINT DEFAULT 0,
        user_xp BIGINT DEFAULT 0
        );'''
    
    unique_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS user_id ON user_info(user_id);'

    try:
        await conn.execute(create_query)
        await conn.execute(unique_constraint)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in user_info.Create_User_Table : Try#1 {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)

async def Create_User_Pilory(client):
    '''
    The table that contains all the users warns, bans count, kicks etc.
    Everything that is bad for a user.

    Return: void
    '''
    conn = await client.db.acquire()
    create_query = '''
    CREATE TABLE IF NOT EXISTS user_pilory(
        user_name TEXT DEFAULT 'NONE',
        user_id BIGINT,
        in_server BIGINT,
        user_warns INT DEFAULT 0,
        user_kicks INT DEFAULT 0,
        user_bans INT DEFAULT 0
    )'''

    unique_constraint = 'CREATE UNIQUE INDEX IF NOT EXISTS one_per_server ON user_pilory(user_id, in_server);'

    try:
        await conn.execute(create_query)
        await conn.execute(unique_constraint)
    
    except Exception as error:
        error_time = time.strftime('%d/%m/%y - %H:%M', time.gmtime())
        print('{} - Error in user_info.Create_User_Pilory : Try#1 {}'.format(error_time, error))
        pass
    
    finally:
        await client.db.release(conn)