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

    # connection

    :coro:`init()` : `None` - Get the connection pool and set the connection

    :coro:`close()` : `None` - Close the connection to the database

    # query management

    :coro:`execute(query, parameter)` [`str`, `list`] : `None` - Execute the query

    :coro:`fetchval(query)` [`str`] : `None` - Fetch a value from the database
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

        # get the connection pool if it has not been defined yet
        if(self.pool == None):
            self.pool = await asyncpg.create_pool(
                host = self.host, database = self.database, user = self.user,
                password = self.password, port = self.port
            )

        # create the connection to the database from the pool
        # if the pool creation has worked
        if(self.pool != None):
            self.connection = await self.pool.acquire()

        return
    
    async def close(self):
        """
        `coroutine`

        Close the connection to the database

        --

        Return : `None`
        """

        # release the connection
        await self.pool.release(self.connection)

        # close the connection
        await self.pool.close()

        return
    
    async def execute(self, query, parameter = None):
        """
        `coroutine`

        Execute an SQL command

        - Parameter : 

        `query` (`str`) : The PostgreSQL query

        [optional]`parameter` (`list`) : List containing sequences arguments

        - Example :

        ```python
        await database.execute("INSERT INTO table(col) VALUES ($1, $2, $3)", ["a", "b", "c"])
        ```

        --

        Return : `None`
        """

        # init
        if(parameter == None):
            parameter = []
        
        await self.init()

        # execute the query and pass the arguments stored in 
        # parameter to it
        try:
            await self.connection.execute(
                query, *parameter
            )
        
        # ignore the unique constraint violation error
        except asyncpg.UniqueViolationError:
            pass
        
        # error handling
        except Exception as error:
            print(f"##########\n(DATABASE : EXECUTE) - Error while executing the query : '{query}' \nError : {error}\n##########")

        # gracefully close the connection
        finally:
            await self.close()

        return
    
    async def fetchval(self, query):
        """
        `coroutine`

        Fetch a value from the databse

        - Parameter 

        `query` (`str`)

        -- 

        Return : Fetched value or `None` if not found
        """

        # init
        value = None
        await self.init()

        # get the value
        try:
            value = await self.connection.fetchval(query)
        
        # error handling
        except Exception as error:
            print(f"##########\n(DATABASE : EXECUTE) - Error while executing the query : '{query}' \nError : {error}\n##########")
        
        # gracefully close the connection
        finally:
            await self.close()

        return(value)
    
    async def fetch(self, query):
        """
        `coroutine`

        Fetch rows by executing the query

        - Paramater

        `query` (`str`)

        --

        Return : `list` of rows or `None` if not found
        """

        # init
        rows = None
        await self.init()

        # get the rows
        try:
            rows = await self.connection.fetch(query)
        
        # error handling
        except Exception as error:
            print(f"##########\n(DATABASE : EXECUTE) - Error while executing the query : '{query}' \nError : {error}\n##########")
        
        # gracefully close the connection
        finally:
            await self.close()

        return(rows)