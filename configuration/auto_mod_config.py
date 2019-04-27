'''
This is the auto-moderation config.

Last update: 27/04/19
'''
# Beware, don't change the name of the variables
# just change their value

# Enable/disable auto-moderation such as auto-ban
# auto-kick, auto-mute etc.
# True = enabled
# False = disabled

AUTO_MOD = True

# Auto-kick/ban necessary warns
# Those variables defines the minimum amount of warns
# needed to auto-kick/ban a user from your server

KICK_WARNS_AMOUNT = 3
BAN_WARNS_AMOUNT = 9

# Timers
# These timers are in seconds, if you set the BAN_LIMIT to 120
# the user will be unbanned after 2 minutes with the auto-unban
# if they've been banned with the auto-mod

BAN_LIMIT = 86400