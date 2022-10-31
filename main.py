from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-0741b221-4c46-4a6d-8165-8d734ea71ed3')


my_region = 'euw1'
vers= lol_watcher.data_dragon.versions_for_region(my_region)
champ_vers = vers['n']['champion']

static_champ_list = lol_watcher.data_dragon.champions(champ_vers)


me = lol_watcher.summoner.by_name(my_region, 'Ghetto Mixer Fab')



# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
live = lol_watcher.spectator.by_summoner(my_region, me['id'])
print(live)
summ_id=str(me['id'])
list_participant = live['participants']
for participant in list_participant:
    if participant['summoner_id'] == summ_id:
        champ = participant['championId']
try:
    response = lol_watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise