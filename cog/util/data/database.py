"""
Database manager

--

Author : DrLarck

Last update : 27/02/20 (DrLarck)
"""

# depenandancies
import asyncio
import asyncpg
import os

class Database():
    """
    A simple asynchronous database object

    - Attribute

    # config

    `host` (`str`) : The database host ip adress

    `database` (`str`) : Represents the database name

    `user` (`str`) : Represents the user

    `password` (`str`) : Represents the user password

    `port` (`str`)

    # connection

    `pool` (`asyncpg.pool.Pool`) : Create a connection pool

    `coonection` (`asyncpg.connection.Connection`) : Database connection from the `pool`

    - Method

    :coro:`init()` : `None` - Get the connection pool and set the connection
    """
    
    # config
    host = "localhost"
    database = "dev-pantheist"
    user = os.environ["pantheist_db_user"]
    password = os.environ["pantheist_db_password"]
    port = "5432"

    pool = None
    connection = None

    # method
    async def init(self):
        """
        `coroutine`

        Get the connection pool and set the connection

        --

        Return : `None`
        """

        self.pool = await asyncpg.create_pool(
            host = self.host, database = self.database, user = self.user,
            password = self.password, port = self.port
        )

        # create the connection to the database from the pool
        # if the pool creation has worked
        if(self.pool != None):
            self.connection = await self.pool.acquire()

        return