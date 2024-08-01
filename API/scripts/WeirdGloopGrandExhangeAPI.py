"""
WeirdGloopGrandExhangeAPI.py
Runescape API Access -> RASPIA
Edgar Bowlin III

This serves as an easy way to access each Weird Gloop Grand Exchange API endpoint
https://api.weirdgloop.org/.
Credit for the information on how to access APIs goes to the authors of
the above article

Some Endpoints have been left out. They will be added as their function is understood enough
to abstract the parameters like category and table seen in the util.Runescape_Hiscores_URL_Templates.py
file.

"""




from util.commonImports import APINameEnums, User_Agent_Strings, URL_Templates
from ._MainAPI import _API


class GrandExhangeAPI(_API):
    def __init__(self):
        super().__init__()

    def get_price_by_name(self, item_name: str = "Abyssal Whip") -> list:
        """
        provides a pricecheck on an item
        :param item_name: a string containing the item name
        :return: a list containing the item's price as seen at
        https://api.weirdgloop.org/#/exchange/getExchangeCurrentPrice
        """
        return self._request_and_decode_API_response(URL_Templates.weird_gloop_GE_price_check_URL,
                                                     User_Agent_Strings.weird_gloop_GE,
                                                     [item_name])

    def get_price_history_all_by_name(self, item_name: str = "Abyssal Whip") -> list:
        """
        provides a price history on an item
        :param item_name: a string containing the item name
        :return: a list containing the item's price history as seen at
        https://api.weirdgloop.org/#/exchange/getExchangeHistoryAll
        """
        return self._request_and_decode_API_response(URL_Templates.weird_gloop_GE_price_history_all_URL,
                                                     User_Agent_Strings.weird_gloop_GE,
                                                     [item_name])

    def get_price_history_sample_by_name(self, item_name: str = "Abyssal Whip") -> list:
        """
        provides a sample of price history on an item
        :param item_name: a string containing the item name
        :return: a list containing the item's price history sample as seen at
        https://api.weirdgloop.org/#/exchange/getExchangeHistoryAll
        """
        return self._request_and_decode_API_response(URL_Templates.weird_gloop_GE_price_history_sample_URL,
                                                     User_Agent_Strings.weird_gloop_GE,
                                                     [item_name])

    def get_price_history_last90d_by_name(self, item_name: str = "Abyssal Whip") -> list:
        """
        provides a price history over the last 90 days on an item
        :param item_name: a string containing the item name
        :return: a list containing the item's price history in the last 90 days as seen at
        https://api.weirdgloop.org/#/exchange/getExchangeHistoryAll
        """
        return self._request_and_decode_API_response(URL_Templates.weird_gloop_GE_price_history_last90d_URL,
                                                     User_Agent_Strings.weird_gloop_GE,
                                                     [item_name])
