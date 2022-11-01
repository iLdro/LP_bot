from riotwatcher import ApiError,riotwatcher
def ErrorHandler(e):
    if e == 429:
        print("yes")