import Lol_dep

class league_player :
    def __init__(self,username,region):
        self.lol = Lol_dep
        self.username = username
        self.region = region

    def set_user(self):
        self.me = self.lol.user_info(self.username, self.region)

    def live(self):
        self.live = self.lol.isLive(self.username,self.region)
