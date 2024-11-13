"""
RunescapeHiscoresSeasonalEventsAPI.py
Runescape Experience Calculator
Edgar Bowlin III

This serves as an easy way to access each Runescape Hiscores Seasonal Events API endpoints
as seen at https://runescape.wiki/w/Application_programming_interface#Seasonal.
Credit for the information on how to access API_Accessors goes to the authors of
the above article

Some Endpoints have been left out. They will be added as their function is understood enough
to abstract the parameters like category and table seen in the util.Runescape_Hiscores_URL_Templates.py
file.

"""



from API.src.API_Accessors.AbstractAPIAccessor import AbstractAPIAccessor
from Runescape_API_Example.util.commonImports import User_Agent_Strings, URL_Templates


class RunescapeHiscoresSeasonalEventsAPIAccessor(AbstractAPIAccessor):

    def __init__(self):
        super().__init__()

    def get_current_seasonal_rankings(self, player_name: str = "Zezima") -> list:
        """

        :param player_name: a string containing the name of the player in question
        :return: a list containing the given player's rankings in the current seasonal event
        as seen at https://runescape.wiki/w/Application_programming_interface#getRankings
        """

        return super().request_and_decode_api_response(URL_Templates.seasonal_get_current_rankings_URL,
                                                       User_Agent_Strings.runescape_seasonal_events,
                                                       [player_name])

    def get_archived_seasonal_rankings(self, player_name: str = "Zezima") -> list:
        """

        :param player_name: a string containing the name of the player in question
        :return: a list containing the given player's rankings in the archived seasonal events
        as seen at https://runescape.wiki/w/Application_programming_interface#getRankings
        """

        return super().request_and_decode_api_response(URL_Templates.seasonal_get_past_rankings_URL,
                                                       User_Agent_Strings.runescape_seasonal_events,
                                                       [player_name])

    def _get_current_seasonal_hiscores_details(self) -> list:
        """
        provides current Seasonal Events Hiscore details
        :return: a list of the current Seasonal Events as seen at
        https://runescape.wiki/w/Application_programming_interface#getHiscoreDetails
        """
        return super().request_and_decode_api_response(URL_Templates.seasonal_get_current_hiscore_details_URL,
                                                       User_Agent_Strings.runescape_seasonal_events)

    def _get_past_seasonal_hiscores_details(self) -> list:
        """
        provides archived Seasonal Events Hiscore details

        :return: a list of the current Seasonal Events as seen at
        https://runescape.wiki/w/Application_programming_interface#getHiscoreDetails
        """
        return super().request_and_decode_api_response(URL_Templates.seasonal_get_past_hiscore_details_URL,
                                                       User_Agent_Strings.runescape_seasonal_events)
