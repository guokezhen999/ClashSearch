import datetime

import matplotlib.pyplot as plt

from MakeFigs import *
from LocalClasses.LocalPlayer import LocalPlayer
from Accounts.ClashDatabase import ClashDatabase
from BasicData.SelectMode import PlayerType

class MakePlayerFigs():
    def __init__(self, players: list[LocalPlayer], database: ClashDatabase, playerType: PlayerType):
        self.players = players
        self.database = database
        self.playerType = playerType

        self.infos = []
        self.playerTags = [player.getInfo("Tag") for player in players]

    def processData(self) -> list[tuple[str, list[datetime.date], dict[str, list]]]:
        playerTagDict = {}
        for player in self.players:
            playerTagDict[player.getInfo("Tag")] = player.getInfo("Name")
        datas = self.database.getPlayerInfoTrack(self.playerType, self.playerTags, self.infos)
        returnList = []
        for key in datas:
            data = datas[key]
            dates = []
            name = playerTagDict[key]
            picData = [[] for i in range(len(data[0]) - 1)]
            for combo in data:
                dates.append(combo[0])
                for j, info in enumerate(combo[1:]):
                    picData[j].append(info)
            picInfoDict = {}
            for i, info in enumerate(self.infos):
                picInfoDict[info] = picData[i]
            returnList.append((name, dates, picInfoDict))
        print(returnList)
        return returnList

    def makeFig(self):
        filePaths = []
        if self.playerType == PlayerType.MY_PLAYER:
            dir = "pictures/figures/myPlayers/"
        elif self.playerType == PlayerType.FOCUS_PLAYER:
            dir = "pictures/figures/focusPlayers/"
        elif self.playerType == PlayerType.ROBOT:
            dir = "pictures/figures/robots/"
        else:
            return
        datas = self.processData()
        names = []
        xData = []
        yData = {}
        for info in self.infos:
            yData[info] = []
        for data in datas:
            names.append(data[0])
            xData.append(data[1])
            for info in self.infos:
                yData[info].append(data[2][info])
        print(yData)
        nameFile = ""
        for name in names:
            nameFile += f"_{name}"
        today = datetime.datetime.now().date()
        for i, info in enumerate(self.infos):
            plt.figure(i, figsize=(12.0, 4.8))
            for j in range(len(xData)):
                x = xData[j]
                y = yData[info][j]
                plt.plot(x, y, label=names[j])
                lastB = None
                for a, b in zip(x, y):
                    if lastB != b:
                        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=9)
                    lastB = b
            plt.legend(loc='best')
            filePath = f"{dir}{info.replace('.', '')}{nameFile}_{today}.png"
            plt.savefig(filePath)
            plt.close()
            filePaths.append(filePath)
        return filePaths



