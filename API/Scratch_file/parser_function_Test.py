from API.scripts.RunemetricsAPI import RunemetricAPI
from API.scripts.RunescapeHiscoresAPI import RunescapeHiScoresAPI
from API.scripts.RunescapeHiscoresClansAPI import RunescapeHiscoresClansAPI
from API.scripts.RunescapeHiscoresSeasonalEventsAPI import RunescapeHiscoresSeasonalEventsAPI
from API.scripts.WeirdGloopGrandExhangeAPI import GrandExhangeAPI


def call_all_methods(obj):
    # Retrieve all attributes of the object
    attributes = dir(obj)

    for attr_name in attributes:
        # Get the attribute
        attr = getattr(obj, attr_name)

        # Check if it is callable and is not a built-in method
        if callable(attr) and not attr_name.startswith('__') and not attr_name.startswith("_"):
            try:
                # Call the method and capture the result
                result = attr()
                print(f"Method {attr_name} called successfully. Result: {result}\n")
            except TypeError as e:
                # Handle methods that require arguments or other TypeErrors
                print(f"Method {attr_name} could not be called without arguments: {e}\n")
            except Exception as e:
                # Handle any other exceptions that may occur
                print(f"Error calling method {attr_name}: {e}\n")


def multiple_objects_call_all_methods(object_list: list[object]):
    for obj in object_list:
        print(f"The object being called is {type(obj)}")
        call_all_methods(obj)
        print("\n")




if __name__ == "__main__":
    api = RunescapeHiScoresAPI()
    api2 = RunemetricAPI()
    api3 = RunescapeHiscoresClansAPI()
    api4 = RunescapeHiscoresSeasonalEventsAPI
    api5 = GrandExhangeAPI()

    obj_list = [api, api2, api3, api4, api5]

    multiple_objects_call_all_methods(obj_list)
"""    parser = APIResponseParser()
    response = api.get_player_hiscore("Zezima").read().decode()
    print(response)
    print(parser.JSONify(response))"""
