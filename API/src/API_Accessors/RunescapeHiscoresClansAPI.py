"""
RuneescapeHiscoresClansAPI.py
Runescape API Access -> RASPIA
Edgar Bowlin III

This serves as an easy way to access each Runescape Clans Hiscore API endpoint
https://runescape.wiki/w/Application_programming_interface#Clans.
Credit for the information on how to access API_Accessors goes to the authors of
the above article

Some Endpoints have been left out. They will be added as their function is understood enough
to abstract the parameters like category and table seen in the util.Runescape_Hiscores_URL_Templates.py
file.

"""




from API.util.commonImports import User_Agent_Strings, URL_Templates
from ._MainAPI import _API


class RunescapeHiscoresClansAPI(_API):

    def __init__(self):
        super().__init__()

    def _get_clan_ranking(self) -> list:
        """
        provides the top three clans from the clan hiscores list

        :return: a list of the top three clans on the clan hiscores as seen at
        https://runescape.wiki/w/Application_programming_interface#clanRanking
        """

        return super()._request_and_decode_API_response(URL_Templates.clan_ranking_URL,
                                                        User_Agent_Strings.runescape_clans)

    def _get_user_clan_ranking(self, user_session_id: str) -> list:
        """
        provides the currently logged-in user's clan name and rank
        :param user_session_id: the current session id of LOGGED IN player
        :return: a list of containing their name, clan name, and clan rank as seen
        at https://runescape.wiki/w/Application_programming_interface#userClanRanking
        """

        return super()._request_and_decode_API_response(URL_Templates.clan_ranking_URL,
                                                        User_Agent_Strings.runescape_clans,
                                                        [user_session_id])

    def get_clan_members_lite(self, clan_name: str = "The Citadel Kingdom") -> list:
        """
        Provides data on each clan member, provided the name of a clan as seen at
        https://runescape.wiki/w/Application_programming_interface#Clan_Members_Lite
        :param clan_name: a string containing the name of the clan in questions
        :return: a list of all clan memebers in the given clan as described at
        https://runescape.wiki/w/Application_programming_interface#Clan_Members_Lite
        """
        return super()._request_and_decode_API_response(URL_Templates.clan_members_lite_URL,
                                                        User_Agent_Strings.runescape_clans,
                                                        [clan_name])
