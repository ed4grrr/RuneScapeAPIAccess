"""
APIResponseToJSON.py
Runescape API Access -> RASPIA
Edgar Bowlin III

This class of families handles parsing of the data retrieved from the desired API. The
User of this library should not directly create this object. The APIResponseParser is within each _API
child and wraps the function that retrieves data from the desired server.


"""

import json
from util.UsefulLists import USER_LITE_SCORE_API_RESPONSE_ORDER
from util.commonImports import APINameEnums, URL_Templates


class APIResponseParser:
    def __init__(self):

        self.APIParser = ParsingStrategies()

    def __call__(self, func):
        """
        This is being overwritten so that an APIResponseParser object can simply be called so that it
            can be easily used as a wrapper.
        :param func: the function to wrap, in this case, the _request_and_decode_response in _MainAPI.py
        :return: the data from the api fully parsed into a python object depending on the response recieved.
        """

        def wrapper(*args, **kwargs):
            print(f"{args}")
            # Call the function to get the raw data
            textToParse = func(*args, **kwargs)
            # Use the parser to parse the raw data
            return self.choose_parser(textToParse, args[1])

        return wrapper

    def choose_parser(self, toDecode: str, URL_template: str):
        """
        This serves to determine the appropriate parsing strategy based on the response.
            To extend this system, a new APINameEnum must be created alongside another parsing strategy method.
            Then, adjust this method accordingly.

        :param toDecode: a string containing the response from the API
        :param URL_template: The url template used to get the response. Necessary for determining correct
            parsing strategy for toDecode
        :return: a python data structure (dict/list) containing the data from the API response, appropriately labelled.
        """

        match URL_Templates.search_api_list(URL_template):  #  See if this template matches an existing parser

            case APINameEnums.CLANS:

                return self.APIParser._parse_clan_data(toDecode)

            case APINameEnums.HISCORES_LITE:

                return self.APIParser._parseUserHighScores(toDecode)

            case APINameEnums.JSON:

                return self.APIParser._parseJSON(toDecode)

            case _:

                raise NotImplemented("Parser Not Implemented")


class ParsingStrategies():
    def __init__(self):
        pass

    def _parse_clan_data(self, clan_data):
        """
        Use this parser to create a python friendly dict from the API response of the Runescape Clan System.

        :param clan_data: a string containing the clan data from the requested clan
        :return: a dict that contains entries in the form of
        "Clan_member_1_name":{'clanRank':"Their_rank", 'totalXP':"some_float_str", 'kills':"some_int_str"}
        """
        clan_data_dict = {}
        clan_data_split = clan_data.split("\n")
        for clanmate in clan_data_split:
            clanmate_details = clanmate.split(",")
            if clanmate_details == ['']:
                continue
            clan_data_dict[clanmate_details[0]] = {"clanRank": clanmate_details[1], "totalXP": clanmate_details[2],
                                                   "kills": clanmate_details[3]}
        del clan_data_dict["Clanmate"]

        return clan_data_dict

    def _parseJSON(self, string):
        """
        Use this parser to create a python friendly dict or list of dicts from most of the RS-related APIs

        :param string: the JSON string returned from the API
        :return: a dict or list containing dicts with the parsed response. all data entries are STILL STRINGS
        """
        return json.loads(string)

    def _parseUserHighScores(self, textToParse: str) -> dict:
        """
        Use this to parse a user's hiscore api response. Doesn't matter if Main/Iron/Hardcore
        :param textToParse: the CSV string that is returned from the official RS HiScores API
        :return: a dict containing either an error or a dict of the requested user's hiscore data
        """

        data = [[float(number) if number != '' else 0 for number in entry.split(",")] for entry in
                textToParse.split("\n")]

        if len(data) == 0:
            return {"Error": "Invalid Player Name"}

        return dict(zip(USER_LITE_SCORE_API_RESPONSE_ORDER, data))
