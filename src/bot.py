import League_player as p
from Lol_dep import data as data



class Bot:
    def __init__(self):
        self.player = []
        self.champion = data.champ_dic
        self.spells = data.spells_dic

    def newPlayer(self, username, region):
        player = p.league_player(username, region)
        self.player.append(player)

    def removPlayer(self, username):
        self.player.remove(username)
