from Lol_dep import __API_KEY
from riotwatcher import LolWatcher, ApiError
import error_lol as error

lol_watcher = LolWatcher(__API_KEY)
def user_info(user: str, region: str) -> dict:
    try:
        lol_watcher.summoner.by_name(region, user)

    except ApiError as err:
        error.ErrorHandler(err)
    else:
        return lol_watcher.summoner.by_name(region, user)


def isLive(user_info: dict, region: str) -> dict:
    try:
        lol_watcher.spectator.by_summoner(region, user_info['id'])
    except ApiError as err:
        error.ErrorHandler(err)
    else:
        return lol_watcher.spectator.by_summoner(region, user_info['id'])
