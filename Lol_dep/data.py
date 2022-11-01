from Lol_dep import __API_KEY
from riotwatcher import LolWatcher

lol_watcher = LolWatcher(__API_KEY)
champ_dic = lol_watcher.data_dragon.champions(lol_watcher.data_dragon.versions_for_region("EUW1")['n']['champion'])
spells_dic = lol_watcher.data_dragon.summoner_spells(lol_watcher.data_dragon.versions_for_region("EUW1")['n']['spells'])