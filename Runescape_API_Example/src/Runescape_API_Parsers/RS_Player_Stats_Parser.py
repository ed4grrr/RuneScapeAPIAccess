

from API.src.Parsers.IParser import iParser


class RS_Player_Stats_Parser(iParser):

    def __init__(self):
        self.USER_LITE_SCORE_API_RESPONSE_ORDER = ["Overall",
                                      "Attack",
                                      "Defence",
                                      "Strength",
                                      "Constitution",
                                      "Ranged",
                                      "Prayer",
                                      "Magic",
                                      "Cooking",
                                      "Woodcutting",
                                      "Fletching",
                                      "Fishing",
                                      "Firemaking",
                                      "Crafting",
                                      "Smithing",
                                      "Mining",
                                      "Herblore",
                                      "Agility",
                                      "Thieving",
                                      "Slayer",
                                      "Farming",
                                      "Runecrafting",
                                      "Hunter",
                                      "Construction",
                                      "Summoning",
                                      "Dungeoneering",
                                      "Divination",
                                      "Invention",
                                      "Archaeology",
                                      "Necromancy",
                                      "Bounty Hunter",
                                      "B.H. Rogues",
                                      "Dominion Tower",
                                      "The Crucible",
                                      "Castle Wars games",
                                      "B.A. Attackers",
                                      "B.A. Defenders",
                                      "B.A. Collectors",
                                      "B.A. Healers",
                                      "Duel Tournament",
                                      "Mobilising Armies",
                                      "Conquest",
                                      "Fist of Guthix",
                                      "GG: Athletics",
                                      "GG: Resource Race",
                                      "WE2: Armadyl Lifetime Contribution",
                                      "WE2: Bandos Lifetime Contribution",
                                      "WE2: Armadyl PvP kills",
                                      "WE2: Bandos PvP kills",
                                      "Heist Guard Level",
                                      "Heist Robber Level",
                                      "CFP: 5 game average",
                                      "AF15: Cow Tipping",
                                      "AF15: Rats killed after the miniquest",
                                      "RuneScore",
                                      "Clue Scrolls Easy",
                                      "Clue Scrolls Medium",
                                      "Clue Scrolls Hard",
                                      "Clue Scrolls Elite",
                                      "Clue Scrolls Master"
                                      ]

    def __parseUserHighScores(self, textToParse: str) -> dict:
        """
        Use this to parse a user's hiscore api response. Doesn't matter if Main/Iron/Hardcore
        :param textToParse: the CSV string that is returned from the official RS HiScores API
        :return: a dict containing either an error or a dict of the requested user's hiscore data
        """

        data = [[float(number) if number != '' else 0 for number in entry.split(",")] for entry in
                textToParse.split("\n")]

        if len(data) == 0:
            return {"Error": "Invalid Player Name"}

        return dict(zip(self.USER_LITE_SCORE_API_RESPONSE_ORDER, data))

    def Parse_API_Response(self, response: str) -> dict:
        """
        This method parses the API-Output into a Python friendly data structure for the end user.
        @param response: the string containing the API output received from an API Accessor object.
        @return: a dict containing the HiScores entry for a player
        """
        return self.__parseUserHighScores(response)