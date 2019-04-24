'''
Manages the settings for the connections, such as the database connection and to the Discord Websocket.

Last update: 24/04/19
'''
# Dependancies 
import os

# To discord connection
BOT_TOKEN = os.environ['PANTHEIST_TOKEN']  # Insert your token here, as the BOT_TOKEN variable's value.

# To database
# For this bot, we're using the async version of PostgreSQL
# If you have you want a simpler database I recommend you
# to use sqlite3.
# The following variables are waiting for str type values
# raplace all of the values by your own values
DB_USER = os.environ['PANTHEIST_DB_USER']  # Your PostgreSQL user name
DB_HOST = os.environ['PANTHEIST_DB_HOST']  # The host adress
DB_PASSWORD = os.environ['PANTHEIST_DB_PASSWORD']  # The password to connect to your database
DB_NAME = os.environ['PANTHEIST_DB_NAME']  # The name of your database
DB_PORT = '5432'  # Initially the PostgreSQL port is 5432