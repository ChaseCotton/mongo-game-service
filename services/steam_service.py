import os
import requests

def login(steam_ticket):
    steam_api_key = os.getenv("STEAM_API_KEY")
    steam_app_id = os.getenv("STEAM_APP_ID")

    params = {
        "ticket" : steam_ticket,
        "appid" : int(steam_app_id),
        "key" : steam_api_key
    }

    response = requests.get("https://partner.steam-api.com/ISteamUserAuth/AuthenticateUserTicket/v1", params=params)

    if response.status_code == 200: 
        json = response.json()
        if "response" in json.keys():
            data = json["response"]["params"]
            return data["steamid"]
    
    return None


def get_player_gamertag(steam_id):
    steam_api_key = os.getenv("STEAM_API_KEY")

    params = {
        "key" : steam_api_key,
        "steamIds" : steam_id
    }

    response = requests.get("https://partner.steam-api.com/ISteamUser/GetPlayerSummaries/v2/", params = params)

    if response.status_code == 200: 
        json = response.json()
        if "response" in json.keys():
            if "players" in json["response"].keys():
                data = json["response"]["players"][0]
                return data["personaname"]
    return ""