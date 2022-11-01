from Lol_dep import __API_KEY
from Lol_dep import lol_watcher
from riotwatcher import LolWatcher, ApiError
from error_lol import error_dic


def user_info(user: str, region: str) -> dict:
    try:
        lol_watcher.summoner.by_name(region, user)

    except ApiError as err:
        print(error_dic[err])
    else:
        return lol_watcher.summoner.by_name(region, user)


def isLive(user_info: dict, region: str) -> dict:
    try:
        lol_watcher.spectator.by_summoner(region, user_info['id'])
    except ApiError as err:
        print(error_dic[err])
    else:
        return lol_watcher.spectator.by_summoner(region, user_info['id'])
