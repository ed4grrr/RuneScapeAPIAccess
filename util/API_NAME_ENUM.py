"""
API_NAME_ENUM.py
Runescape API Access -> RASPIA
Edgar Bowlin III

These enums are used to determine what parsing needs to occur when data is returned from the API.

To add more parsers, create a new enum definition below in APINameEnums

For example,    GRAND_EXCHANGE = 3  can be added just below the line "HISCORES_LITE = 2" line.
And so on and so forth. Be sure to edit the APIResponseToJSON.py file to add a parser for the new method
and add it to the match case code block.

"""

from enum import Enum

class APINameEnums(Enum):
    JSON = 0
    CLANS = 1
    HISCORES_LITE = 2
