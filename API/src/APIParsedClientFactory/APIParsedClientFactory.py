from typing import Type

import API.src.APIClient.BaseAPIClient as API
import API.src.Parsers.IParser as Parser
from API.src.APIClient.APIParsedClient import ApiParsedClient


class APIParsedClientFactory:

    def __init__(
        self,
        API_Function_Parser_dict: {str:Type[Parser]} =None,
        User_Input_API_dict: {str:{str:Type[API], str:str}}=None,
    ):
        """
        creates an API Parsed Accessor Factory object.

        can be instantiated as is, or given pre-made API_Function_Parser_dict and/or User_Input_API_dict

        For an object of this class to work, each API Endpoint function/object/user input combos need to be placed in
        the appropriate dictionaries. If the API object/Parsers entry AND the matching "user" input/API object pairs are
        added

        @param API_Function_Parser_dict: A dictionary where the key is the API Accessor's function name to be called and
        the value is the Parser class that is meant to parse that endpoint's response
        @param User_Input_API_dict: A dictionary where the key is the input from the "user" and the values are the API
        Accessor Object to be associated with this input, and the function identifier to be called as a str
        """
        if API_Function_Parser_dict is None:
            API_Function_Parser_dict = {}
        if User_Input_API_dict is None:
            User_Input_API_dict = {}
        self.API_Function_Parser_Dict = API_Function_Parser_dict  # used to map API endpoint classes' methods to specific parser classes
        self.User_Input_API_Dict = (
            User_Input_API_dict  # used to map User Input to API endpoints.
        )

    def add_Input_API_Combo(
        self, user_input: str, apiAccessor: Type[API], functionName: str
    ) -> None:
        """
        add an Input_string : {API Accessor Class, and function_name_string} entry to the self.User_Input_API_dict.


        @param user_input: a string containing the user input to associate with this specific endpoint's API Accessor
        @param apiAccessor: an object based on the associated API Accessor class which is determined by the input parameter
        @param functionName: A string containing the function identifier associated with the relevant API Accessor object
        @return: None, Nothing, Nada
        """
        self.User_Input_API_Dict[user_input] = {
            "Accessor": apiAccessor,
            "functionName": functionName,
        }

    def delete_Input_API_Combo(self, user_input: str) -> None:
        """
        Deletes an Input/API/Function name entry in the User_Input_API_dict.

        @param user_input: a string containing the user input key to be deleted from the previously mentioned dict
        @return: None, Nothing, Nada
        """
        try:
            del self.User_Input_API_Dict[user_input]
        except KeyError:
            print(f"Key {user_input} not found within User_Input_API_dict.")

    def add_URL_Parser_Combo(self, URL: str, parser: Type[Parser]) -> None:
        """
        Add new URL Template/IParser-implementing object to use in Factory method

        To be used when adding a new endpoint and its parser to the factory method.

        @param URL: The url template for the API endpoint
        @param parser: The parsing strategy necessary to get the API response as a usable
        Python data structure
        @return: None (Void)
        """
        self.API_Function_Parser_Dict[URL] = parser

    def remove_URL_Parser_Combo(self, URL: str) -> None:
        """
        Delete a URl Template/IParser-implementing objects from API_Parser_Dict()


        @param URL: The URL template (which is used as the key) to be deleted
        @return: None (Void)
        """
        try:
            del self.API_Function_Parser_Dict[URL]
        except KeyError:
            print(f"Key {URL} not found within API_Function_Parser_Dict.")

    def determine_API_From_Input_Combo(self, user_input: str) -> Type[API]:
        """
        determines which API Accessor object to create when a user input is given.

        @param user_input: a string that is (hopefully) added as a key to the appropriate API Accessor Class
        @return: the type of the API Accessor based on user input
        """
        try:
            return self.User_Input_API_Dict[user_input]
        except KeyError as e:
            raise KeyError(
                f"{user_input} is not a key within the User_Input_API_dict.\nDid you "
                f"use add_Input_API_Combo with the expected user input and the"
                + f" relevant API Accessor Object?"
            )

    def determine_Parser_From_API_Combo(self, function_name: str) -> Type[Parser]:
        """
        determines the Parser required based on the string containing the function identifier passed in as an argument

        @param function_name: a string containing the identifier of the relevant function in an API Accessor Object
        @return: The Parser class used to parse the API's output
        """
        try:
            return self.API_Function_Parser_Dict[function_name]
        except KeyError as e:
            raise KeyError(
                f"{function_name} is not a key within the API_Parser_dict.\nDid you "
                f"use add_URL_Parser_Combo with the Callable API function identifier (as a string) and the"
                + f"respective parser class?"
            )

    def create_API_Parsed_Accessor(self, user_input: str) -> ApiParsedClient:
        """
        Creates an API_Parsed_Accessor ready to accept arguments for the specified endpoint

        @param user_input: the string given by the "user" to determine which api settings to use when creating the API Parsed
        Accessor objects.
        @return: An API Parsed Accessor object that allow for contacting the API endpoint specified.
        """

        # Get the API's dict entry that contains the Accessor Class adn the function identifier of the function to be
        # called within the specified Accessor Class
        choices = self.determine_API_From_Input_Combo(user_input)

        api = choices["Accessor"]
        function = choices["functionName"]

        parser = self.determine_Parser_From_API_Combo(function)

        return ApiParsedClient(api, function, parser)
