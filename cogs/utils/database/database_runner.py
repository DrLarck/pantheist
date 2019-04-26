'''
You can manage your database behaviours here.

Last update: 24/04/19
'''
# Dependancies
import asyncpg, asyncio

from configuration.connection_config import DB_USER, DB_HOST, DB_PASSWORD, DB_NAME, DB_PORT
from data.init.user_info import Create_User_Table, Create_User_Pilory

async def Connect_To_Database(client):
    '''
    Create the connection pool to your database

    Return: void
    '''
    # By doing this, we can call the database only by using client.db
    client.db = await asyncpg.create_pool(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

async def Init_Tables(client):
    '''
    Init the different tables.
    
    Return: void
    '''
    await Create_User_Table(client)
    await Create_User_Pilory(client)