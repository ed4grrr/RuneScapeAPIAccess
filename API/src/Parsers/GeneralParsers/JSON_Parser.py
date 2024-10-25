from API.src.Parsers import IParser
import json

class JSON_Parser(IParser):
    def __init__(self):
        pass

    def Parse_API_Response(self, response:str)-> dict:
        """
        Returns a dict created from a JSON string


        @param response: a JSON string to be parsed
        @return: a dict (JSON data) created from the JSON string
        """
        return json.loads(response)