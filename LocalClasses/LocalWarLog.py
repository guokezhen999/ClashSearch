import datetime

from LocalClasses import *
from BasicData.Items import Items

class LocalWarLog:
    def __init__(self):
        self.infos = {}
        
    def setInfo(self, name, value):
        self.infos[name] = value
        
    def getInfo(self, name):
        return self.infos[name]

def warLogToLocal(warLog: dict) -> LocalWarLog:
    localWarLog = LocalWarLog()
    clan = warLog['clan']
    print(clan['tag'])
    opponent = warLog['opponent']
    print(opponent)
    clanUrl = clan['badgeUrls']['medium'].split('/')[-1]
    opponentUrl = opponent['badgeUrls']['medium'].split('/')[-1]
    endDateStr = warLog['endTime'].split('T')[0]
    date = datetime.datetime.strptime(endDateStr, '%Y%m%d').date()
    print(date)
    values = [
        clan['name'], clan['tag'], clan['clanLevel'], clanUrl,
        opponent['name'], opponent['tag'], opponent['clanLevel'], opponentUrl,
        warLog['result'], date, warLog['teamSize'], clan['attacks'],
        clan['stars'], clan['destructionPercentage'],
        opponent['stars'], opponent['destructionPercentage'],
        clan['expEarned']
    ]
    for i, info in enumerate(Items.warLogInfos):
        localWarLog.setInfo(info, values[i])
    return localWarLog

def warLogsToLocal(warLogs: list[dict]) -> list[LocalWarLog]:
    localWarLogs = []
    for log in warLogs:
        localWarLogs.append(warLogToLocal(log))
    return localWarLogs