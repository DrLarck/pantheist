### What is pantheist ?
**Pantheist** is a free and open-source moderation Discord Bot.
It has been first developped for the **Discord Ball Z** community.
The project has started on **23/04/2019** at 10 PM (GMT +1) in France.

### How does it work ?
**Pantheist** is written in **python3.7** which means that if you want to run it by yourself, you need to download the right **python** version.
For the moment the bot isn't well developped, but it will be designed to let anyone run it on their machine and let them free to modify the code as they want.

To run it, type one of these commands in your terminal :
* Windows :
`python -B main.py`

* Ubuntu :
`python3.7 -B main.py`

*(The `-B` parameter avoid the creation of the `__pycache__` folders and files)*

### Is it customizable ?
**Yes**, **Pantheist** is a fully customizable bot.
You can add your own commands, edit an existing command, or simply the behaviour of the program by editing the `configuration` files.
If you just want to edit the behaviour of your bot, you can edit one of the files that is contained in the `configuration` folder using a Text Editor.
I recommend you to use **Notepad++**.

Now if you want to add a brand new command that you've imagined by your own, just go to the `cogs` folder, then `commands`. Afterward, create a new **python file** (with the `.py` extension) just like : `my_amazing_command.py` and init your file as following :
 ```python
 '''
 A clear description of the file you've created
 
 Last update: ENTER_THE_DATE_HERE
 '''
 # Dependancies
 import discord, asyncio  # Just import all the modules you need for your command
 from discord.ext import commands
 from discord.ext.commands import Cog
 
 class YOUR_CLASS(Cog):
      def __init__(self, client):
          self.client = client
 
      '''
      ENTER YOUR CODE HERE
      '''
 
 def setup(client):
      client.add_cog(YOUR_CLASS(client))
```

### Requirements
The requirements are the followings : 
* `python version 3.7` or higher.
* `asyncpg`
    * `asyncpg` is required for the **database**. We're using **PostgreSQL**.