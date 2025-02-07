from BasicData.Items import Items

from LocalClasses import *


class LocalClan:
    def __init__(self):
        self.infos = {}

    def setInfo(self, name, value):
        self.infos[name] = value

    def getInfo(self, name):
        return self.infos[name]


def clanToLocal(clan: coc.Clan) -> LocalClan:
    localClan = LocalClan()
    if clan.war_league is not None:
        warLeague = clan.war_league.name
    else:
        warLeague = "未排名"
    if len(clan.capital_districts) > 0:
        peak = clan.capital_districts[0].hall_level
    else:
        peak = 0
    if clan.location is not None:
        location = clan.location.name
    else:
        location = "未设置"
    infoValues = [
        clan.name, clan.tag, clan.level, clan.member_count, warLeague, clan.points,
        clan.builder_base_points, peak, clan.capital_points, clan.war_frequency, clan.war_win_streak,
        clan.war_wins, clan.war_losses, clan.war_ties, location, clan.type, clan.required_trophies,
        clan.required_builder_base_trophies, clan.required_townhall, clan.public_war_log, clan.description
    ]
    for i, value in enumerate(infoValues):
        localClan.setInfo(Items.clanInfos[i], value)
    return localClan

def clansToLocal(clans: list[coc.Clan]) -> list[LocalClan]:
    localClans = []
    for clan in clans:
        localClan = clanToLocal(clan)
        localClans.append(localClan)
    return localClans