"""
Runescape_HiScores_URL_Templates.py
Runescape API Access -> RASPIA
Edgar Bowlin III

Templates used to go to the various RuneScape related APIs, so they are abstracted away from
the user.


If developing more APIs, just add more endpoints to this file. Make sure to update API_NAME_ENUM.py
and RASPIAUserAgentStrings with the relevant data/functionality to deal with custom endpoints.

"""




import API.util.API_NAME_ENUM as API_NAME_ENUM


# *****************************************RUNESCAPE HISCORES URLS*****************************************
ranking_url = 'https://secure.runescape.com/m=hiscore/ranking.json?table={0}&category={1}&size={2}'
userRanking_URL="https://secure.runescape.com/c={0}/m=hiscore/userRanking.json"
hiscores_lite_URL = 'https://secure.runescape.com/m=hiscore/index_lite.ws?player={0}'
ironman_hiscores_lite_URL = "https://secure.runescape.com/m=hiscore_ironman/index_lite.ws?player={0}"
hardcore_ironman_hiscores_lite_URL = "https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player={0}"
boss_groups_URL = 'https://secure.runescape.com/m=group_hiscores/v1//groups?groupSize={0}&size={1}&bossId={2}&page={3}'
# *********************************************************************************************************

# *****************************************SEASONAL EVENTS URLS*****************************************
seasonal_get_current_rankings_URL = "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}"
seasonal_get_past_rankings_URL = "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}\
&status=archived"
seasonal_get_current_hiscore_details_URL = "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json"
seasonal_get_past_hiscore_details_URL = "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json?status\
=archived"
# *********************************************************************************************************

# *****************************************CLAN URLS*****************************************
user_clan_ranking_URL = "http://services.runescape.com/c={0}/m=clan-hiscores/userClanRanking.json"
clan_ranking_URL = "http://services.runescape.com/m=clan-hiscores/clanRanking.json"
clan_members_lite_URL = 'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={0}'
# *********************************************************************************************************

# *****************************************RUNEMETRICS URLS*****************************************
runemetrics_player_URL = 'https://apps.runescape.com/runemetrics/profile/profile?user={0}&activities=20'
runemetrics_monthly_xp_URL = "https://apps.runescape.com/runemetrics/xp-monthly?searchName={0}&skillid={1}"
runemetrics_player_quest_data_URL = "https://apps.runescape.com/runemetrics/quests?user={0}"
runemetrics_total_player_count_URL = "https://www.runescape.com/player_count.js?varname=iPlayerCount&callback=jQuery000000000000000_0000000000&_=0"
runemetrics_rsusertotal_URL = "https://secure.runescape.com/m=account-creation-reports/rsusertotal.ws"
runemetrics_NXT_URL = "https://content.runescape.com/downloads/changelog.json"
runemetrics_windows_NXT_installer_info = "https://content.runescape.com/downloads-info/windows/RuneScape-Setup.exe.json"
runemetrics_OSX_NXT_installer_info = "https://content.runescape.com/downloads-info/osx/RuneScape.dmg.json"

# *********************************************************************************************************

# *****************************************WEIRD GLOOP URLS*****************************************
weird_gloop_GE_price_check_URL = "https://api.weirdgloop.org/exchange/history/rs/latest?name={0}"
weird_gloop_GE_price_history_all_URL = "https://api.weirdgloop.org/exchange/history/rs/all?name={0}"
weird_gloop_GE_price_history_sample_URL = "https://api.weirdgloop.org/exchange/history/rs/sample?name={0}"
weird_gloop_GE_price_history_last90d_URL = "https://api.weirdgloop.org/exchange/history/rs/last90d?name={0}"
weird_gloop_voice_of_seren_URL = "https://api.weirdgloop.org/runescape/vos"
weird_gloop_historical_voice_of_seren_URL = "https://api.weirdgloop.org/runescape/vos/history"

# *********************************************************************************************************

API_ENDPOINTS_NEEDING_JSON_PARSE = {
    'ranking_url': 'https://secure.runescape.com/m=hiscore/ranking.json?table={0}&category={1}&size={2}',
    'userRanking_URL': "https://secure.runescape.com/c={0}/m=hiscore/userRanking.json",

    'boss_groups_URL': 'https://secure.runescape.com/m=group_hiscores/v1//groups?groupSize={0}&size={1}&bossId={2}&page={3}',
    'seasonal_get_current_rankings_URL': "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}",
    'seasonal_get_past_rankings_URL': "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}&status=archived",
    'seasonal_get_current_hiscore_details_URL': "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json",
    'seasonal_get_past_hiscore_details_URL': "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json?status=archived",
    'user_clan_ranking_URL': "http://services.runescape.com/c={0}/m=clan-hiscores/userClanRanking.json",
    'clan_ranking_URL': "http://services.runescape.com/m=clan-hiscores/clanRanking.json",
    'clan_members_lite_URL': 'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={0}',
    'runemetrics_player_URL': 'https://apps.runescape.com/runemetrics/profile/profile?user={0}&activities=20',
    'runemetrics_monthly_xp_URL': "https://apps.runescape.com/runemetrics/xp-monthly?searchName={0}&skillid={1}",
    'runemetrics_player_quest_data_URL': "https://apps.runescape.com/runemetrics/quests?user={0}",
    'runemetrics_total_player_count_URL': "https://www.runescape.com/player_count.js?varname=iPlayerCount&callback=jQuery000000000000000_0000000000&_=0",
    'runemetrics_rsusertotal_URL': "https://secure.runescape.com/m=account-creation-reports/rsusertotal.ws",
    'runemetrics_NXT_URL': "https://content.runescape.com/downloads/changelog.json",
    'runemetrics_windows_NXT_installer_info': "https://content.runescape.com/downloads-info/windows/RuneScape-Setup.exe.json",
    'runemetrics_OSX_NXT_installer_info': "https://content.runescape.com/downloads-info/osx/RuneScape.dmg.json",
    'weird_gloop_GE_price_check_URL': "https://api.weirdgloop.org/exchange/history/rs/latest?name={0}",
    'weird_gloop_GE_price_history_all_URL': "https://api.weirdgloop.org/exchange/history/rs/all?name={0}",
    'weird_gloop_GE_price_history_sample_URL': "https://api.weirdgloop.org/exchange/history/rs/sample?name={0}",
    'weird_gloop_GE_price_history_last90d_URL': "https://api.weirdgloop.org/exchange/history/rs/last90d?name={0}",
    'weird_gloop_voice_of_seren_URL': "https://api.weirdgloop.org/runescape/vos",
    'weird_gloop_historical_voice_of_seren_URL': "https://api.weirdgloop.org/runescape/vos/history",
}

API_ENDPOINTS_NEEDING_HISCORE_LITE_PARSE ={
    'hiscores_lite_URL': 'https://secure.runescape.com/m=hiscore/index_lite.ws?player={0}',
    'ironman_hiscores_lite_URL': "https://secure.runescape.com/m=hiscore_ironman/index_lite.ws?player={0}",
    'hardcore_ironman_hiscores_lite_URL': "https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player={0}",

}

API_ENDPOINTS_NEEDING_CLAN_PARSE ={
'clan_members_lite_URL': 'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={0}'
}



REVERSED_API_ENDPOINTS_NEEDING_JSON_PARSE = {
    'https://secure.runescape.com/m=hiscore/ranking.json?table={0}&category={1}&size={2}': 'ranking_url',
    "https://secure.runescape.com/c={0}/m=hiscore/userRanking.json": 'userRanking_URL',
    'https://secure.runescape.com/m=group_hiscores/v1//groups?groupSize={0}&size={1}&bossId={2}&page={3}': 'boss_groups_URL',
    "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}": 'seasonal_get_current_rankings_URL',
    "http://services.runescape.com/m=temp-hiscores/getRankings.json?player={0}&status=archived": 'seasonal_get_past_rankings_URL',
    "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json": 'seasonal_get_current_hiscore_details_URL',
    "http://services.runescape.com/m=temp-hiscores/getHiscoreDetails.json?status=archived": 'seasonal_get_past_hiscore_details_URL',
    "http://services.runescape.com/c={0}/m=clan-hiscores/userClanRanking.json": 'user_clan_ranking_URL',
    "http://services.runescape.com/m=clan-hiscores/clanRanking.json": 'clan_ranking_URL',
    'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={0}': 'clan_members_lite_URL',
    'https://apps.runescape.com/runemetrics/profile/profile?user={0}&activities=20': 'runemetrics_player_URL',
    "https://apps.runescape.com/runemetrics/xp-monthly?searchName={0}&skillid={1}": 'runemetrics_monthly_xp_URL',
    "https://apps.runescape.com/runemetrics/quests?user={0}": 'runemetrics_player_quest_data_URL',
    "https://www.runescape.com/player_count.js?varname=iPlayerCount&callback=jQuery000000000000000_0000000000&_=0": 'runemetrics_total_player_count_URL',
    "https://secure.runescape.com/m=account-creation-reports/rsusertotal.ws": 'runemetrics_rsusertotal_URL',
    "https://content.runescape.com/downloads/changelog.json": 'runemetrics_NXT_URL',
    "https://content.runescape.com/downloads-info/windows/RuneScape-Setup.exe.json": 'runemetrics_windows_NXT_installer_info',
    "https://content.runescape.com/downloads-info/osx/RuneScape.dmg.json": 'runemetrics_OSX_NXT_installer_info',
    "https://api.weirdgloop.org/exchange/history/rs/latest?name={0}": 'weird_gloop_GE_price_check_URL',
    "https://api.weirdgloop.org/exchange/history/rs/all?name={0}": 'weird_gloop_GE_price_history_all_URL',
    "https://api.weirdgloop.org/exchange/history/rs/sample?name={0}": 'weird_gloop_GE_price_history_sample_URL',
    "https://api.weirdgloop.org/exchange/history/rs/last90d?name={0}": 'weird_gloop_GE_price_history_last90d_URL',
    "https://api.weirdgloop.org/runescape/vos": 'weird_gloop_voice_of_seren_URL',
    "https://api.weirdgloop.org/runescape/vos/history": 'weird_gloop_historical_voice_of_seren_URL',
}

REVERSED_API_ENDPOINTS_NEEDING_HISCORE_LITE_PARSE = {
    'https://secure.runescape.com/m=hiscore/index_lite.ws?player={0}': 'hiscores',
    "https://secure.runescape.com/m=hiscore_ironman/index_lite.ws?player={0}": 'ironman_hiscores_lite_URL',
    "https://secure.runescape.com/m=hiscore_hardcore_ironman/index_lite.ws?player={0}": 'hardcore_ironman_hiscores_lite_URL',
}


REVERSED_API_ENDPOINTS_NEEDING_CLAN_PARSE = {
    'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={0}': 'clan_members_lite_URL'
}

SEARCHABLE_API_ENDPOINTS = {API_NAME_ENUM.APINameEnums.CLANS:REVERSED_API_ENDPOINTS_NEEDING_CLAN_PARSE,
                            API_NAME_ENUM.APINameEnums.HISCORES_LITE:REVERSED_API_ENDPOINTS_NEEDING_HISCORE_LITE_PARSE
                            , API_NAME_ENUM.APINameEnums.JSON:REVERSED_API_ENDPOINTS_NEEDING_JSON_PARSE}



def search_api_list(URL_template:str)-> API_NAME_ENUM.APINameEnums | None:
    """
    Returns the enum representing the parser meant to be used.
    :param URL_template: the template that we used to get the response
    :return: the enum of the parser, or None if no suitable parser is found
    """
    #print(f"This is the url template in question {URL_template}")
    for parserType,dict in SEARCHABLE_API_ENDPOINTS.items():
        try:
            #print(f"Trying to find {URL_template}")
            test =dict[URL_template]
            #print(f"Returning {parserType}")
            return parserType
        except :
            continue
    #print(f"Didn't find anything")
    return None








