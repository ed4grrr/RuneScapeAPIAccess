import traceback
from time import sleep

from API.scripts.RunemetricsAPI import RunemetricAPI
from API.scripts.RunescapeHiscoresAPI import RunescapeHiScoresAPI
from API.scripts.RunescapeHiscoresClansAPI import RunescapeHiscoresClansAPI
from API.scripts.RunescapeHiscoresSeasonalEventsAPI import RunescapeHiscoresSeasonalEventsAPI
from API.scripts.WeirdGloopGrandExhangeAPI import GrandExhangeAPI
from APIResponseParsers.APIResponseToJSON import APIResponseParser
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time to include milliseconds
formatted_time = now.strftime('%Y_%m_%d_%H_%M_%S_%f')

# Round milliseconds to the nearest tenth of a second
# Extract milliseconds from formatted_time



def saveFile(strs):
    with open(f"{formatted_time}.txt", "a") as text_file:
        text_file.write(strs)

def print_exception_info(exc):
    """
    Prints detailed information about an exception to the console.
    :param exc: The exception instance to print information about.
    """
    # Print the exception type and message
    saveFile(f"Exception type: {type(exc).__name__}")
    saveFile(f"Exception message: {exc}")

    # Print the traceback details
    saveFile("Traceback details:")
    tb = exc.__traceback__
    traceback_lines = traceback.format_exception(type(exc), exc, tb)
    for line in traceback_lines:
        saveFile(line)

def call_all_methods(obj):
    # Retrieve all attributes of the object
    attributes = dir(obj)
    parser = APIResponseParser()

    for attr_name in attributes:

        # Get the attribute
        attr = getattr(obj, attr_name)

        # Check if it is callable and is not a built-in method
        if callable(attr) and not attr_name.startswith('__') and not attr_name.startswith("_"):
            saveFile(f"\n############## {attr_name.upper()} T E S T##############\n")
            try:
                # Call the method and capture the result
                result = attr()

                saveFile(f"Method {attr_name} called successfully. Response is of type {type(result)}\nResult:\n{result}\n")

            except TypeError as e:
                # Handle methods that require arguments or other TypeErrors
                saveFile(f"Method {attr_name} could not be called without arguments:\n{print_exception_info(e)}\n")
            except Exception as e:
                # Handle any other exceptions that may occur.
                saveFile(f"Error calling method {attr_name}:\n{print_exception_info(e)}\n")
            saveFile("\n############################\n")
            sleep(1.5)



def multiple_objects_call_all_methods(object_list: list[object]):
    for obj in object_list:
        saveFile("*******************************************")
        saveFile(f"\n&&&&&&&&&&&&&&&&&&&&&&&&The object being called is {type(obj)}&&&&&&&&&&&&&&&&&&&&&&&&\n")
        call_all_methods(obj)
        saveFile("*******************************************")
        saveFile("\n")




if __name__ == "__main__":
    api = RunescapeHiScoresAPI()
    api2 = RunemetricAPI()
    api3 = RunescapeHiscoresClansAPI()
    api4 = RunescapeHiscoresSeasonalEventsAPI()
    api5 = GrandExhangeAPI()

    obj_list = [api,api2,api3,api4,api5]

    multiple_objects_call_all_methods(obj_list)
"""    parser = APIResponseParser()
    response = api.get_player_hiscore("Zezima").read().decode()
    saveFile(response)
    saveFile(parser.JSONify(response))"""
