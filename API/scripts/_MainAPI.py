from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import util.API_NAME_ENUM as API_NAME_ENUM
from APIResponseParsers.APIResponseToJSON import APIResponseParser

parser = APIResponseParser()

class _API:
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
        :return: either a urlopen object or str if error
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

    @parser
    def _request_and_decode_API_response(self, URL_template: str, user_agent: str, apiCalled: API_NAME_ENUM,
                                         *args: list[str]) -> list:
        """
        This is the actual function a user should call to request and obtain data from one of the
            child Classes.
        :param URL_template: string containing the API URL needed formated to accept user input
        :param user_agent: string containing the intended use of that api information
        :param args: strings that contain the user supplied inputs necessary in the URL_Template
        :return: a list of the information provided by the api call
        """
        api_request = self._create_Request_from_URL_template(URL_template, user_agent, *args)

        data = self._call_API(api_request)

        return data


if __name__ == "__main__":
    api_test = _API()
    test_URL_template = 'https://secure.runescape.com/m=hiscore/index_lite.ws?player={0}'
    user_entry_no_space = "Zezima"
    user_entry_space = "Iron man"
    args = ["player name", "skill/ID", "#dogg ", "_$@^edgar "]

    print(api_test._clean_user_inputs(args))

    # print(api_test._create_Request_from_URL_template(test_URL_template, user_entry_no_space))
    # print(api_test._create_Request_from_URL_template(test_URL_template, user_entry_space))
