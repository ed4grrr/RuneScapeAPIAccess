"""
RunescapeHiscoresAPI.py
Runescape Experience Calculator
Edgar Bowlin III

This serves as an easy way to access each Runescape Hiscorces API endpoints
as seen at https://runescape.wiki/w/Application_programming_interface#Hiscores.
Credit for the information on how to access APIs goes to the authors of
the above article

Some Endpoints have been left out. They will be added as their function is understood enough
to abstract the parameters like category and table seen in the util.Runescape_Hiscores_URL_Templates.py
file.

"""

from Main_API import _API
import util.Runescape_HiScores_URL_Templates as URL_Templates


class RunescapeHiScoresAPI(_API):

    def __init__(self):
        super().__init__()



    def get_rankings(self, URL_template: str, current_activity: str, skill_or_activity_name: str, amount_of_ranks: str)->list:
        """

        :param URL_template: the template required for this endpoint
        :param current_activity: a string containing the int of the current skill, overall level, or activity
        :param skill_or_activity_name: a string containing the int of the skills or activities
        :param amount_of_ranks: a string containing the int of the amount of players requested, MAX 50
        :return:a list directly from Jagex that contains the name, score, and rank of the top amount_ranks
            players as seen at
            https://runescape.wiki/w/Application_programming_interface#ranking
        """

        return super().request_and_decode_API_response(URL_template, current_activity, skill_or_activity_name, amount_of_ranks)
    def get_userRanking(self, current_session_id:str)->list:

        return  super().request_and_decode_API_response(URL_Templates.)


    def get_player_hiscore(self, URL_template: str, player_name: str) -> list:
        """

        used to get the hiscores data for a given player, as described at

        :param URL_template: the url template for the needed API endpoint
        :param player_name: the name of the user to look up
        :return: a list directly from Jagex that contains the information on that user as seen at
            https://runescape.wiki/w/Application_programming_interface#Hiscores_Lite
        """
        return super().request_and_decode_API_response(URL_template, player_name)

    def get_clan_member_data(self, URL_template:str, clan_name:str)->list:
        """
        Provides
        :param URL_template: the template required for this endpoint
        :param clan_name:
        :return: a list of all clan memebers in the given clan as described at
        https://runescape.wiki/w/Application_programming_interface#Clan_Members_Lite
        """
        return super().request_and_decode_API_response(URL_template, clan_name)


if __name__ == "__main__":
    test = RunescapeHiScoresAPI()
    user_entry_no_space = "Zezima"
    user_entry_space = "Iron man"

    response = test.get_player_hiscore(URL_Templates.player_hiscores_lite_URL, user_entry_space)

    print(response.read().decode().split("\n"))
