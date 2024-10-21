from typing import Callable
import API.src.Parsers.IParser as Parser
from API.src.API_Accessors._MainAPI import _API as API


class API_Parsed_Accessor():

    def __init__(self, Accessor:API, functionName:str, Parser_for_EndPoint:Parser):
        """
        An object that contains the API accessor and parser for a particular endpoint

        @param AccessorFunction: The API accessor that contacts and returns the API response
        @param Parser: The parsing strategy designed to parse this particular endpoint's
        data
        """
        self.Accessor = Accessor
        self.functionName =functionName
        self.Response_Parser = Parser_for_EndPoint

    # Function to call a method on an arbitrary object
    # Original from CHATGPT prompt
    # "How would I pass the function name and execute that on an arbitrary object
    # (that has a function declaration with that name) within python?"


    def call_And_Parse_API(self, *args, **kwargs):
        # Use getattr to get the function by name and then call it
        func = getattr(self.Accessor, self.functionName, None)


        if callable(func):
            returnable = self.Response_Parser().Parse_API_Response(func( *args, **kwargs))
            return returnable  # Call the function if it exists
        else:
            raise AttributeError(f"{self.__class__.__name__} does not have a function called {self.functionName}")


