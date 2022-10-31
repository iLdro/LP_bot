from Lol_dep import Lol_API
from riotwatcher import ApiError

_API = Lol_API()
lol_watcher = _API.get_API()


def list_champ(region: str) -> str:
    vers = lol_watcher.data_dragon.versions_for_region(region)
    champ_vers = vers['n']['champion']
    return lol_watcher.data_dragon.champions(champ_vers)


def user_info(user: str, region: str) -> dict:
    try:
        lol_watcher.summoner.by_name(region, user)

    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            return lol_watcher.summoner.by_name(region, user)


def isLive(user_info: dict, region: str) -> dict:
    try:
        lol_watcher.spectator.by_summoner(region, user_info['id'])
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        if err.response.status_code == 503:
            print("Service seems unvaialble")
        else:
            return lol_watcher.spectator.by_summoner(region, user_info['id'])
