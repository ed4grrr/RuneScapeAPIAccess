import json

from util.UsefulLists import USER_LITE_SCORE_API_RESPONSE_ORDER


class APIResponseParser():
    def __init__(self):
        pass

    # My reasoning here, so far, is that either the response is going to be
    # either in a JSON dumpable format or as a string denominating new lines with \n.
    # this method requires full testing for each API type currently implemented.
    # However, I think (and hope) this should largely work after debugging.
    def JSONify(self, textToParse: str or list[str]) -> dict[str:any]:

        try:
            return json.loads(textToParse)

        except:

            data = self._parseMultiLinedString(textToParse)

            if len(data) == 0:
                # TODO CReate exception for this line below
                return ("Invalid Player Name")

            return json.load(dict(zip(USER_LITE_SCORE_API_RESPONSE_ORDER, data)))

    def _parseMultiLinedString(self, textToParse: str) -> list[int or str]:
        return [[int(number) if number != '' else 0 for number in entry.split(",")] for entry in
                textToParse.split("\n")]
