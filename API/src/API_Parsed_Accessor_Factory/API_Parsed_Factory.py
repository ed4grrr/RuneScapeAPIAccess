from typing import Callable

import API.src.API_Accessors._MainAPI as API
import API.src.Parsers.IParser as Parser
from API.src.API_Parsed_Accessor_Factory.API_Parsed_Accessor import API_Parsed_Accessor


class API_Parsed_Accessor_Factory():
    def __init__(self, API_Parser_dict:dict[str:Parser]={}, User_Iput_API_dict:dict[str:[API,str]]={}):
        self.API_Parser_Dict = API_Parser_dict # used to map API endpoint classes options to specific parser classes
        self.User_Input_API_Dict = User_Iput_API_dict # used to map User Input to API endpoints.


    def add_Input_API_Combo(self, input:str, apiAccessor:API, functionName:str) -> None:
        self.User_Input_API_Dict[input] = {"Accessor":apiAccessor,"functionName":functionName}

    def delete_Input_API_Combo(self, input:str) -> None:
        del self.User_Input_API_Dict[input]


    def add_URL_Parser_Combo(self,URL:str, Parser:Parser ) -> None:
        """
        Add new URL Template/IParser-implementing object to use in Factory method

        To be used when adding a new endpoint and its parser to the factory method.

        @param URL: The url template for the API endpoint
        @param Parser: The parsing strategy necessary to get the API response as a usable
        Python data structure
        @return: None (Void)
        """
        self.API_Parser_Dict[URL] = Parser

    def remove_URL_Parser_Combo(self, URL:str) -> None:
        """
        Delete a URl Template/IParser-implemnting objects from API_Parser_Dict()


        @param URL: The URL template (which is used as the key) to be deleted
        @return: None (Void)
        """
        del self.API_Parser_Dict[URL]


    def determine_API_From_Input_Combo(self, input:str)-> Parser:
        try:
            return self.User_Input_API_Dict[input]
        except KeyError as e:
            raise KeyError(f"{input} is not a key within the User_Input_API_dict.\nDid you "
                           f"use add_Input_API_Combo with the expected user input and the"
                           +f"callable API function?")

    def determine_Parser_From_API_Combo(self, api:Callable)-> Parser:
        try:
            return self.API_Parser_Dict[api]
        except KeyError as e:
            raise KeyError(f"{input} is not a key within the API_Parser_dict.\nDid you "
                           f"use add_URL_Parser_Combo with the Callable API function and the"
                           +f"respective parser class?")


    def create_API_Parsed_Accessor(self, input:str ) -> API_Parsed_Accessor:

        choices = self.determine_API_From_Input_Combo(input)
        api = choices["Accessor"]
        function = choices["functionName"]

        parser = self.determine_Parser_From_API_Combo(api)

        return API_Parsed_Accessor(api, function, parser)




