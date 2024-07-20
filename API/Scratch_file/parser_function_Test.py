from API.scripts.RunescapeHiscoresAPI import RunescapeHiScoresAPI

if __name__ == "__main__":
    api = RunescapeHiScoresAPI()
    response = api.get_player_hiscore("Zezima")
    print(response.read().decode())
