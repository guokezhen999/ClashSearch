def caculateLeague(trophies: int) -> str:
    if trophies < 400:
        league = "noLeague"
    elif trophies < 800:
        league = "bronze"
        if trophies < 500:
            league = league + "3"
        elif trophies < 600:
            league = league + "2"
        else:
            league = league + "1"
    elif trophies < 1400:
        league = "silver" + str(3 - (trophies - 800) // 200)
    elif trophies < 2000:
        league = "gold" + str(3 - (trophies - 1400) // 200)
    elif trophies < 2600:
        league = "crystal" + str(3 - (trophies - 2000) // 200)
    elif trophies < 3200:
        league = "master" + str(3 - (trophies - 2600) // 200)
    elif trophies < 4100:
        league = "champion" + str(3 - (trophies - 3200) // 300)
    elif trophies < 5000:
        league = "titan" + str(3 - (trophies - 4100) // 300)
    else:
        league = "legend"
    return league