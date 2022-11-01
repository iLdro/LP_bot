from Lol_dep import user_command as command
from Lol_dep import data as data


class league_player:
    def __init__(self, username, region):
        self.lol_command = command
        self.username = username
        self.region = region

    def set_user(self):
        self.me = self.lol_command.user_info(self.username, self.region)

    def live(self):
        self.live = self.lol_command.isLive(self.username, self.region)
