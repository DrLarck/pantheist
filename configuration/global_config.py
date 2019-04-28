'''
Here we manage the global configuration of the bot, such as its version, prefixes, images, icons, etc.

Last update: 28/04/19
'''
# Basic configuration

PREFIX = ['**']

COGS = ['cogs.event.on_ready_event', 'cogs.event.on_message_event', 'cogs.commands.warn',
        'cogs.commands.kick', 'cogs.commands.help', 'cogs.commands.ban']

V_MAJ, V_MED, V_MIN, V_PHASE = 0,1,14,'Prototype' 

# Customization

THEME_COLOR = 0x6600ff  # Hexadecimal form color