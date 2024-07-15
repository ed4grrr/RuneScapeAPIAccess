from Main_API import _API
import util.Runescape_HiScores_URL_Templates as URL_Templates


class RunemetricAPI(_API):

    def __init__(self):
        super().__init__()


#TODO determine return type for runemetrics based "api" responses
    def get_player_profile(self,URL_template, player_name):
        """
        provides the player profile from Runemetrics, as described at
        https://runescape.wiki/w/Application_programming_interface#Profile

        :param URL_template: the url template required for getting player profiles\
            from the runemetrics profile

        :param player_name: string containg the player name in question

        :return: a list of the Runemetric data on the said player, as seen at
            https://runescape.wiki/w/Application_programming_interface#Profile
        """
        return super().request_and_decode_API_response(URL_template, player_name)

    def get_player_monthly_xp(self, URL_template:str, player_name:str, skill_id:str)->list:
        """
        provides the monthly_xp over the
        :param URL_template: the url template required for getting monthly xp totals for a specificed player
            from RuneMetrics
        :param player_name: string containing the player name in question
        :param skill_id: a string containing an int to specific a specific skill, if -1, then overall xp is shown
        :return: a list of timestampped xp gains for the past year
        """

        return super().request_and_decode_API_response(URL_template, player_name, skill_id)

