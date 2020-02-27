"""
Main class

--

Author : DrLarck

Last update : 27/02/20 (DrLarck)
"""

# dependancies
import discord
import asyncio
import os

from discord.ext.commands import Bot

class Main():
    """
    Run the bot and manages the bot configuration

    - Method

    `start()` : Run the bot
    """

    prefix = ["**"]
    token = os.environ["pantheist_token"]

    def start(self):
        """
        Run the bot

        --

        Return : `None`
        """    

        # init
        client = None
        activity = None

        # defining the activity
        activity = discord.Game("**help | v2 - BETA")

        # defining the client
        client = Bot(self.prefix, activity = activity, help_command = None)

        # run the bot
        client.run(self.token)

        return

# run the Main class
if(__name__ == "__main__"):
    Main().start()