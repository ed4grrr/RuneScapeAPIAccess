import util.RASPIAUserAgentStrings as User_Agent_Strings
import util.Runescape_HiScores_URL_Templates as URL_Templates
from ._MainAPI import _API


class RunescapeHiscoresClansAPI(_API):

    def __init__(self):
        super().__init__()



    def get_clan_ranking(self)->list:
        """
        provides the top three clans from the clan hiscores list

        :return: a list of the top three clans on the clan hiscores as seen at
        https://runescape.wiki/w/Application_programming_interface#clanRanking
        """

        return super().request_and_decode_API_response(URL_Templates.clan_ranking_URL,
                                                       User_Agent_Strings.runescape_clans)

    def get_user_clan_ranking(self, user_session_id:str)->list:
        """
        provides the currently logged-in user's clan name and rank
        :param user_session_id: the current session id of LOGGED IN player
        :return: a list of containing their name, clan name, and clan rank as seen
        at https://runescape.wiki/w/Application_programming_interface#userClanRanking
        """

        return super().request_and_decode_API_response(URL_Templates.clan_ranking_URL,
                                                       User_Agent_Strings.runescape_clans, [user_session_id])
    def get_clan_members_lite(self, clan_name:str)->list:
        """
        Provides data on each clan member, provided the name of a clan as seen at
        https://runescape.wiki/w/Application_programming_interface#Clan_Members_Lite
        :param clan_name: a string containing the name of the clan in questions
        :return: a list of all clan memebers in the given clan as described at
        https://runescape.wiki/w/Application_programming_interface#Clan_Members_Lite
        """
        return super().request_and_decode_API_response(URL_Templates.clan_members_lite_URL,
                                                       User_Agent_Strings.runescape_clans, [clan_name])
