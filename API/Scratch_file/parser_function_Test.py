import traceback
from time import sleep

from API.scripts.RunemetricsAPI import RunemetricAPI
from API.scripts.RunescapeHiscoresAPI import RunescapeHiScoresAPI
from API.scripts.RunescapeHiscoresClansAPI import RunescapeHiscoresClansAPI
from API.scripts.RunescapeHiscoresSeasonalEventsAPI import RunescapeHiscoresSeasonalEventsAPI
from API.scripts.WeirdGloopGrandExhangeAPI import GrandExhangeAPI
from APIResponseParsers.APIResponseToJSON import APIResponseParser


def print_exception_info(exc):
    """
    Prints detailed information about an exception to the console.
    :param exc: The exception instance to print information about.
    """
    # Print the exception type and message
    print(f"Exception type: {type(exc).__name__}")
    print(f"Exception message: {exc}")

    # Print the traceback details
    print("Traceback details:")
    tb = exc.__traceback__
    traceback_lines = traceback.format_exception(type(exc), exc, tb)
    for line in traceback_lines:
        print(line, end='')

def call_all_methods(obj):
    # Retrieve all attributes of the object
    attributes = dir(obj)
    parser = APIResponseParser()

    for attr_name in attributes:

        # Get the attribute
        attr = getattr(obj, attr_name)

        # Check if it is callable and is not a built-in method
        if callable(attr) and not attr_name.startswith('__') and not attr_name.startswith("_"):
            print(f"\n############## {attr_name.upper()} T E S T##############\n")
            try:
                # Call the method and capture the result
                result = attr()
                if type(result) != str:
                    result = result.read().decode("iso-8859-1")
                print(f"Method {attr_name} called successfully.\nResult:\n{result.encode("iso-8859-1")}\n")
                print(
                    f"Parsing result: Type-> {type(parser.JSONify(result.replace('\r\n', '\n'), "Clans"))} \n{parser.JSONify(result, "Clans")}\n")
            except TypeError as e:
                # Handle methods that require arguments or other TypeErrors
                print(f"Method {attr_name} could not be called without arguments:\n{print_exception_info(e)}\n")
            except Exception as e:
                # Handle any other exceptions that may occur.
                print(f"Error calling method {attr_name}:\n{print_exception_info(e)}\n")
            print("\n############################\n")
            sleep(1.5)



def multiple_objects_call_all_methods(object_list: list[object]):
    for obj in object_list:
        print("*******************************************")
        print(f"\n&&&&&&&&&&&&&&&&&&&&&&&&The object being called is {type(obj)}&&&&&&&&&&&&&&&&&&&&&&&&\n")
        call_all_methods(obj)
        print("*******************************************")
        print("\n")




if __name__ == "__main__":
    api = RunescapeHiScoresAPI()
    api2 = RunemetricAPI()
    api3 = RunescapeHiscoresClansAPI()
    api4 = RunescapeHiscoresSeasonalEventsAPI()
    api5 = GrandExhangeAPI()

    obj_list = [api3]

    multiple_objects_call_all_methods(obj_list)
"""    parser = APIResponseParser()
    response = api.get_player_hiscore("Zezima").read().decode()
    print(response)
    print(parser.JSONify(response))"""
