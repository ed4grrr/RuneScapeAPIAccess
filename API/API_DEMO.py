from API.src.API_Parsed_Accessor_Factory.API_Parsed_Factory import API_Parsed_Accessor_Factory as API_Factory
from API.src.API_Accessors import RunescapeHiscoresAPI
from API.src.Parsers.RS_Player_Stats_Parser import RS_Player_Stats_Parser as Parser

if __name__ == "__main__":


#-------------------------------------------API,INPUT, and PARSER Registering-----------------------------------------------------------------------#
    # the API Accessor that inherits from Main_API. This will be used to register this accessor with

    # the API Parsed Accessor Factory.
    api_accessor_to_be_called = RunescapeHiscoresAPI.RunescapeHiScoresAPI()


    # As seen in the examples, an API Accessor object can have many different method calls. This module

    # was designed with that in mind for "better" (in my opinion) code organization. Therefore, you must

    # specify which method must be called. This should ALWAYS be a string containing the method identifier

    # for the relevant function to be called. That means the string must match the identifier exactly.
    function_to_be_called = 'get_player_hiscore'




    # This dict is used to link a function name (that exists within a Main_API-inheriting class and the function calls

    # and returns the _request_and_decode_API_Response function from Main_API) and the parser required to put the

    # response into a Pythonic data structure for easier use. Some less-than-maintained APIs do not output into

    # unified response formats. For example, RuneScape's official APIs have been made over the course of over a decade.

    # This, among other factors, has left their API's outputting in JSON or CSV depending on the endpoint. This allows

    # the user to design objects with function families to group together similar endpoints and still provide separate

    # parsing strategies for each function within the API Parsed Accessor Factory.
    RS_Related_API_Parser_dict = {function_to_be_called: Parser} # The Parser here is RS_Player_Stats_Parser as seen by
                                                                 # its' import statement seen at the top.


    # This dict is meant to pair string inputs with the respective API endpoint Call. There can easily be more than one

    # but there MUST be at least one (correctly) formatted Key/Value pair for the API Parsed Accessor Factory can function

    # This dict stores the desired Input required for a call to a specific API endpoint, the relevant API Accessor

    # object, and a string containing the method identifier that calls and returns the API response. The Key is meant to

    # be the input. The value to this key is another dict, containing the "Accessor" and "functionName" keys with their

    # values being the relevant API Accessor object and the string containing the method identifier for the endpoint

    # to be called. The idea here is to provide a flexible system for the module user to add more types of

    # API_Parsed_Accessors the factory can create.
    RS_Related_Input_API_dict = {"User HiScore":
        {
        "Accessor":api_accessor_to_be_called,
        "functionName":function_to_be_called
        }
    }
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Making Factor object------------------------------------------------------------------------------------#


    test_factory = API_Factory(RS_Related_API_Parser_dict,RS_Related_Input_API_dict)

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Use Factory to Create API Parsed Accessor---------------------------------------------------------------#

    test_api = test_factory.create_API_Parsed_Accessor("User HiScore")
#---------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------Use API Parsed Object to make API call and print response-----------------------------------------------#
    response = test_api.call_And_Parse_API("Deathmunglar")

    print(response)
#---------------------------------------------------------------------------------------------------------------------------------------------------#