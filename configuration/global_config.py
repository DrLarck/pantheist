'''
Here we manage the global configuration of the bot, such as its version, prefixes, images, icons, etc.

Last update: 06/05/19
'''
# Basic configuration

PREFIX = ['**']

COGS = ['cogs.event.on_ready_event', 'cogs.event.on_message_event', 'cogs.commands.warn',
        'cogs.commands.kick', 'cogs.commands.help', 'cogs.commands.ban',
        'cogs.commands.mute', 'cogs.event.on_error_event', 'cogs.commands.language']

V_MAJ, V_MED, V_MIN, V_PHASE = 0,1,58,'ALPHA' 

# Customization
        # Roles

MUTE_ROLE = 'Muted (pantheist)'

        # Channels

LOGGER = 'p_logs'