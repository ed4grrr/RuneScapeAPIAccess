import json
from csv import reader
from io import StringIO

import util.UsefulLists


class APIResponseParser():
    def __init__(self):
        pass

    # My reasoning here, so far, is that either the response is going to be
    # either in a JSON dumpable format or as a string denominating new lines with \n.
    # this method requires full testing for each API type currently implemented.
    # However, I think (and hope) this should largely work after debugging.
    def JSONify(self, textToParse: str or list[str], apiCalled: str) -> dict[str:any]:


        try:
            return json.loads(textToParse)

        except:
            match apiCalled:
                case "Hiscores":
                    data = self._create_dict_from_list(self._csv_to_list(textToParse),
                                                       util.UsefulLists.USER_LITE_SCORE_API_RESPONSE_ORDER)
                case _:
                    data = "Not_Parsable"
            return data

    def _csv_to_list(self, csv_string):
        f = StringIO(csv_string)
        list_of_csv = reader(f)
        returnable = [row for row in list_of_csv]
        return returnable

    def JSONifyPlayerHiscores(self, textToParse):

        return self._create_dict_from_list(self._csv_to_list(textToParse), util.UsefulLists.SKILL_NAMES)

    # Convert the list of lists into a list of dictionaries
    def _create_dict_from_list(self, csv_data, list_names):

        names = list_names[:len(csv_data)]

        # Create a dictionary with names as keys and rows as values
        data = {name: row for name, row in zip(names, csv_data)}
        return data

    def _parseMultiLinedString(self, textToParse: str) -> list[int or str]:
        return [[float(number) if number != '' else 0 for number in entry.split(",")] for entry in
                textToParse.split("\n")]


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
    test = APIResponseParser()
    print(test.JSONify(textToParse))
