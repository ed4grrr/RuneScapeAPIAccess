"""

BaseAPIClient.py
General Purpose Python API Accessor Factory. GPP-AAF
Edgar Bowlin III

This is an abstract class, meant only to act as a parent to a concrete child class. As seen in this class,some
functions begin with '_'. These functions should not be called directly outside of these file as they are used
internally within this module.

(not that Python will stop you)

"""

from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


# this parser serves to wrap _request_and_decode_API_response results
# and return a user-friendly data structure. However, all data is
# still in a string format. It is up to the user to verify the data.


class BaseAPIClient:
    """
    The abstract parent class for all API accessing classes.
    """

    def __init__(self):
        pass

    @staticmethod
    def _clean_user_inputs(*api_arguments: list[str]) -> list:
        """
        cleans user input to be used in a URL
        :param api_arguments: string arguments that fulfill API required parameters
        :return: a list of "cleaned" strings usable in URLs
        """
        if len(api_arguments) > 0:  # if no argument, dont crash the program
            arguments_list = api_arguments[0]
            return [quote(str(api_argument)) for api_argument in arguments_list]

    def _create_request_from_url_template(
        self, URL_template: str, user_agent, *user_entered_arguments: str
    ) -> Request:
        """
        used to create a Request object from a usable url created from user input and the provided URL Template

        :param URL_template: a string containing the API URL with formating marks {0}, {1}, etc. for all user
            entered arguments
        :param user_agent: a string meant to describe the device that is running your program, HOWEVER, many API's ask
            that you change this attribute to a string describing your API request's function. More specifically, If a
            weather-related program is using this module,the user agent string supplied here should look something like
            "daily_weather_program".
        :param user_entered_arguments: strings containing the arguments a user has entered
        :return: A request object that can be used with urlopen to access the supplied URL Template and arguments
        """
        cleaned_args = self._clean_user_inputs(*user_entered_arguments)
        try:
            headers = {"User-Agent": user_agent}
            if len(cleaned_args) != 0:

                return Request(URL_template.format(*cleaned_args), headers=headers)
            else:
                return Request(URL_template, headers=headers)
        except IndexError as e:
            raise IndexError(
                f"Error: {e}. Not enough arguments provided to fill the URL template."
            )
        except KeyError as e:
            raise IndexError(
                f"Error: {e}. Incorrect placeholder format in URL template."
            )
        except Exception as e:
            raise IndexError(f"Unexpected error: {e}")

    @staticmethod
    def _call_API(api_request: Request, text_encoding: str = "iso-8859-1") -> str:
        """
        Takes a Request object and ATTEMPTS to connect to the supplied formated API URL and returns the data.

        This function is what executes the hard work of calling the Request object to get the requested data.

        :param api_request: a string that holds the url to request data from
        :text_encoding: a str that describes the format of the API Response's Encoding
        :return: a string containing the decoded message

        """
        try:
            with urlopen(api_request) as r:
                return r.read().decode(text_encoding)
        except HTTPError as e:
            e.add_note("\nUnfulfilled Request,\nCode: {e.code}\nReason: {e.reason}")
            raise e

        except URLError as e:
            raise URLError(f"Failed to reach Server, \nReason: {e.reason} ")

    def request_and_decode_api_response(
        self, URL_template: str, user_agent: str, *args: list[str]
    ) -> str:
        """
        Takes a URL_template, a user string, and a list of API args to call and decode the API response


        :param URL_template: string containing the API URL needed formated to accept user input
        :param user_agent: a string meant to describe the device that is running your program, HOWEVER, many API's ask
            that you change this attribute to a string describing your API request's function. More specifically, If a
            weather-related program is using this module,the user agent string supplied here should look something like
            "daily_weather_program".
        :param args: a list of strings that contain the user supplied inputs necessary in the URL_Template
        :return: a parsed str response from the API
        """
        api_request = self._create_request_from_url_template(
            URL_template, user_agent, *args
        )

        data = self._call_API(api_request)

        return data
