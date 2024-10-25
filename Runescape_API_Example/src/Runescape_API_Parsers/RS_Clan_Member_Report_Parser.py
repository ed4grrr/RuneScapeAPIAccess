

from API.src.Parsers.IParser import iParser


class RS_Clan_Member_Report_Parser(iParser):

    def __init__(self):

        pass



    def __parse_clan_data(self, clan_data):
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

    def Parse_API_Response(self, response: str) -> dict:
        """
        This method parses the API-Output into a Python friendly data structure for the end user.
        @param response: the string containing the API output received from a RS Clan Member API
        endpoint
        @return: a dict containing the members name as the key, their rank, experience earned while
        in the clan, and the total kills of the player within Clan Wars.
        """
        return self.__parse_clan_data(response)