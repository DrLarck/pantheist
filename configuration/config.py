"""
Config class

--

Author : DrLarck

Last update : 27/02/20 (DrLarck)
"""

# dependancies
from configuration.sub.color import Color

class Config():
    """
    Manages the bot configuration

    - Attribute

    `color` (`Color()`) : Set of bot's colors
    """

    color = Color()