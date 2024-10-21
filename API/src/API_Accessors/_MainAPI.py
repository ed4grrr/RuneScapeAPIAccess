"""
_MainAPI.py
Runescape API Access -> RASPIA
Edgar Bowlin III

This is an abstract method, meant only to act as a parent to a concrete child class. As seen in this class, and all children,
some functions begin with '_'. These functions should not be called directly outside of these src as they are
used internally within this library.

Some of these are truly internal functions. The rest (largely seen in only the Child classes) are methods accessing API_Accessors
where either I am stupid or the documentation is not the greatest on how to use, do not seem to be active, or any other
reason that may cause them to be highly unreliable.

As I continue with this project, I hope to test the "broken" internal functions to provide wider access to the more
niche endpoints.
"""



from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from API.src.Parsers.APIResponseToJSON import APIResponseParser

# this parser serves to wrap _request_and_decode_API_response results
# and return a user-friendly data structure. However, all data is
# still in a string format. It is up to the user to verify the data.


class _API:
    """
    The abstract parent class for all API accessing classes.
    """
    def __init__(self):
        pass

    def _clean_user_inputs(self, *api_arguments: list[str]) -> list:
        """
        cleans user input to be used in a URL
        :param api_arguments: string arguments that fulfill API required parameters
        :return: a list of "cleaned" strings usable in URLs
        """
        if len(api_arguments) > 0:  # if no argument, dont crash the program
            arguments_list = api_arguments[0]
            return [quote(str(api_argument)) for api_argument in arguments_list]


    def _create_Request_from_URL_template(self, URL_template: str, user_agent,
                                          *user_entered_arguments: str) -> str or Request:
        """
        used to create a usable url from user input
        :param URL_template: a string containing the API URL with formating marks {0}, {1}, etc. for all user
            entered arguments
        :param user_agent: a string meant to describe the device that is running your program, HOWEVER, when using
            the RS Wiki API_Accessors, they request that the user agent string be a name describing the end use of the data.
            For example, "Firemaking_Item_Price_Scraper"
        :param user_entered_arguments: strings containing the arguments a user has entered
        :return:
        """
        cleaned_args = self._clean_user_inputs(*user_entered_arguments)
        try:
            headers = {'User-Agent': user_agent}
            if len(cleaned_args) != 0:

                return Request(URL_template.format(*cleaned_args), headers=headers)
            else:
                return Request(URL_template, headers=headers)
        except IndexError as e:
            return f"Error: {e}. Not enough arguments provided to fill the URL template."
        except KeyError as e:
            return f"Error: {e}. Incorrect placeholder format in URL template."
        except Exception as e:
            return f"Unexpected error: {e}"

    def _call_API(self, api_request:Request)-> urlopen or str:
        """

        :param api_request: a string that holds the url to request data from
        :return: either an urlopen object or str if error
        """
        try:
            with urlopen(api_request) as r:
                return r.read().decode('iso-8859-1')
        except HTTPError as e:
            # TODO create new custom exceptions to describe these cases so
            #  that it can be raised to a higher level.
            return f"Unfulfilled Request,\nCode: {e.code}\nReason: {e.reason}"

        except URLError as e:
            return f"Failed to reach Server, \nReason: {e.reason} "




    def _request_and_decode_API_response(self, URL_template: str, user_agent: str,
                                         *args: list[str]) -> list:
        """
        This is the ACTUAL function a user should call to request and obtain data from one of the
            child Classes.
        :param URL_template: string containing the API URL needed formated to accept user input
        :param user_agent: a string meant to describe the device that is running your program, HOWEVER, when using
            the RS Wiki API_Accessors, they request that the user agent string be a name describing the end use of the data.
            For example, "Firemaking_Item_Price_Scraper"
        :param args: strings that contain the user supplied inputs necessary in the URL_Template
        :return: a parsed response from the API
        """
        api_request = self._create_Request_from_URL_template(URL_template, user_agent, *args)

        data = self._call_API(api_request)

        return data

