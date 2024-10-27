"""

APIParsedClient.py
General Purpose Python API Accessor Factory. GPP-AAF
Edgar Bowlin III

Created by the API_Parsed_Factory, this class's objects are used by the end user to get data from an API endpoint

This object should not be created directly, but created from an API_Parsed_Factory object. Using the object received from
the factory's function "call_and_parse_api" would be the correct way to receive this object.


"""

from typing import Any, Type

import API.src.Parsers.IParser as Parser
from API.src.APIClient.BaseAPIClient import BaseAPIClient as API


class ApiParsedClient:
    """
    The factory used to create API Parsed Accessor in an easy-to-use manner and abstract away the minutia.
    """

    def __init__(self, Accessor: Type[API], functionName: str, Parser_for_EndPoint: Type[Parser]):
        """
        the constructor for the API_Parsed_Accessor, the object received from the API_Parsed_Factory

        @param Accessor: the accessor object required to make the specified API call
        @param functionName: a string with the name of the function that should be called on the object
        @param Parser_for_EndPoint: The parser class that is made to parse the API output into a python friendly
        data structure
        """

        try:
            self.Accessor_Class = Accessor
            self.Accessor_Object = Accessor()
        except TypeError as e:
            e.add_note(f"\nThe argument 'Accessor' ({Accessor}) is of type {type(Accessor)}."
                       f"\nThis needs to be of {Type[Accessor]}.")

        self.functionName = functionName
        self.Response_Parser = Parser_for_EndPoint

    # Function to call a method on an arbitrary object
    # Original from CHATGPT prompt
    # "How would I pass the function name and execute that on an arbitrary object
    # (that has a function declaration with that name) within python?"

    def call_And_Parse_API(self, *args: list[str], **kwargs: str) -> Any:
        """
        takes API arguments, calls the respective function in the API Accessor object, and returns the parsed data


        @param args: The arguments for the API URL IN THE ORDER you have defined in the URL Template string.
        @param kwargs: The same as args, but with keyword arguments
        @return: Varies depending on the parser implementation. More than likely a string or a dict
        """
        # Use getattr to get the function by name and then call it
        func = getattr(self.Accessor_Class, self.functionName, None)

        # if the string is a callable method identifier
        if callable(func):
            # then, call that function with the supplied args/kwargs and give that response to the response parser to
            # be parsed. Store that to be returned
            returnable = self.Response_Parser().Parse_API_Response(
                # as this function will primarily be bound to an object, func must be
                # given the arguments for an Object of type AbstractAPIAccessor and then
                # all other arguments necessary for calling the relevant API endpoint. This
                # object will take the role of the self argument within the relevant function
                func(self.Accessor_Object,*args, **kwargs)
            )
            return returnable
        else:
            # else, more than likely, you gave the wrong function name or the wrong accessor object
            raise AttributeError(
                f"{self.__class__.__name__} does not have a function called {self.functionName}. Are you sure you are "
                f"using the correct accessor and the correct method identifier string?-"
            )
