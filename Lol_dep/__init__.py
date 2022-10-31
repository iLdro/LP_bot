from riotwatcher import LolWatcher, ApiError

class Lol_API:
    def __init__(self):
        self.API = lol_watcher = LolWatcher('RGAPI-0741b221-4c46-4a6d-8165-8d734ea71ed3')

    def get_API(self):
        return self.API
