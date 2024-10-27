import json

from API.src.Parsers import IParser


class JSONParser(IParser):
    """This is a generic JSON parser that will decode any compatible JSON string into a python dict (JSON Data)"""

    def __init__(self):
        """
        Creates the JSON_Parser object
        """
        pass

    @staticmethod
    def Parse_API_Response(response:str)-> dict:
        """
        Returns a dict created from a JSON string


        @param response: a JSON string to be parsed
        @return: a dict (JSON data) created from the JSON string
        """
        return json.loads(response)