import json
from csv import reader
from io import StringIO

from util.UsefulLists import USER_LITE_SCORE_API_RESPONSE_ORDER

import util.UsefulLists
from util.commonImports import APINameEnums,URL_Templates



class APIResponseParser:
    def __init__(self,*args,**kwargs,):
        self.APIParser = new_parsers()
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"{args}")
            # Call the function to get the raw data
            textToParse = func(*args, **kwargs)
            # Use the parser to parse the raw data
            return self.choose_parser(textToParse, args[1])

        return wrapper

    def choose_parser(self, toDecode:str, URL_template:str):
        match URL_Templates.search_api_list(URL_template):
            case APINameEnums.CLANS:
                return self.APIParser._parse_clan_data(toDecode)
            case APINameEnums.HISCORES_LITE:
                return self.APIParser._parseUserHighScores(toDecode)
            case APINameEnums.JSON:
                return self.APIParser._parseJSON(toDecode)
            case _ :
                raise NotImplemented("Parser Not Implemented")




class new_parsers():
    def __init__(self):
        pass

    def _parse_clan_data(self, clan_data):
        clan_data_dict = {}
        clan_data_split = clan_data.split("\n")
        for clanmate in clan_data_split:
            clanmate_details = clanmate.split(",")
            if clanmate_details == ['']:
                continue
            clan_data_dict[clanmate_details[0]] = {"clanRank":clanmate_details[1], "totalXP":clanmate_details[2],
                                                   "kills":clanmate_details[3]}
        del clan_data_dict["Clanmate"]

        return clan_data_dict

    def _parseJSON(self, string):
        return json.loads(string)

    def _parseUserHighScores(self, textToParse: str) -> dict:
        data = [[float(number) if number != '' else 0 for number in entry.split(",")] for entry in
                textToParse.split("\n")]

        if len(data) == 0:
            return {"Error":"Invalid Player Name"}

        return dict(zip(USER_LITE_SCORE_API_RESPONSE_ORDER, data))



if __name__ == "__main__":
    textToParse = "55,2736,5400000000\n\
    493,99,200000000\n\
    966,99,200000000\n\
    503,99,200000000\n\
    421,99,200000000\n\
    721,99,200000000\n\
    254,99,200000000\n\
    625,99,200000000\n\
    3,99,200000000\n\
    217,99,200000000\n\
    92,99,200000000\n\
    484,99,200000000\n\
    276,99,200000000\n\
    233,99,200000000\n\
    275,99,200000000\n\
    434,99,200000000\n\
    373,99,200000000\n\
    144,99,200000000\n\
    3,99,200000000\n\
    421,120,200000000\n\
    381,99,200000000\n\
    193,99,200000000\n\
    213,99,200000000\n\
    196,99,200000000\n\
    190,99,200000000\n\
    675,120,200000000\n\
    193,99,200000000\n\
    182,120,200000000\n\
    332,120,200000000\n\
    -1,-1\n\
    -1,-1\n\
    133,26444969\n\
    -1,-1\n\
    -1,-1\n\
    2635,4285\n\
    2458,4161\n\
    1809,4354\n\
    3247,4405\n\
    1157,1944\n\
    427,552\n\
    20741,1258\n\
    -1,-1\n\
    6128,631\n\
    19882,605\n\
    39251,563812\n\
    -1,-1\n\
    -1,-1\n\
    -1,-1\n\
    -1,-1\n\
    -1,-1\n\
    637,169\n\
    -1,-1\n\
    -1,-1\n\
    611,20925\n\
    127,968\n\
    40857,7\n\
    41939,77\n\
    36068,68\n\
    22156,12"
    test = new_parsers()
    print(test._unlistAString('[{"name":"Lady Boo 1","score":"200,000,000","rank":"1"},\
{"name":"Allar","score":"200,000,000","rank":"2"},\
{"name":"lan","score":"200,000,000","rank":"3"},\
{"name":"Deja Vu Xiii","score":"200,000,000","rank":"4"},\
{"name":"Kh510","score":"200,000,000","rank":"5"},\
{"name":"Spdavis","score":"200,000,000","rank":"6"},\
{"name":"Petite","score":"200,000,000","rank":"7"},\
{"name":"Rasial God","score":"200,000,000","rank":"8"},\
{"name":"Drumgun","score":"200,000,000","rank":"9"},\
{"name":"Evil Abyssal","score":"200,000,000","rank":"10"}]\
'))
