import asyncio
import datetime

import coc
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from qasync import QEventLoop, asyncSlot

from UI.MainGUI import Ui_MainWindow

from LocalClasses.LocalPlayer import playersToLocal
from LocalClasses.LocalWarLog import warLogsToLocal, LocalWarLog
from Accounts.ClashDatabase import ClashDatabase
from Accounts.ClashAccount import ClashAccount
from BasicData.SelectMode import PlayerType

from ShowDialogs.AddPlayerDialog import AddPlayerDialog
from ShowDialogs.SelectPlayerItemsDialog import SelectPlayerItemsDialog
from ShowDialogs.AddClanDialog import AddClanDialog
from ShowDialogs.ImportRobotsDialog import ImportRobotsDialog
from ShowDialogs.SelectPlayerFigItems import SelectPlayerFigItems

from ShowTables.ShowPlayerTable import ShowPlayerTable
from ShowTables.ShowMyPlayerTable import ShowMyPlayerTable
from ShowTables.ShowOtherPlayerTable import ShowOtherPlayerTable
from ShowTables.ShowClanTable import ShowClanTable

from ShowForms.ShowLocalPlayerForm import ShowLocalPlayerForm
from ShowForms.ShowClanWarForm import ShowClanWar

from MakeFigs.MakePlayerFigs import MakePlayerFigs

class ClashSearch(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.database = ClashDatabase()

        # 查询界面
        self.pushButtonSearchPlayer.clicked.connect(self.searchPlayerOnline)

        # 我的玩家界面
        myPlayers = self.database.getPlayersAll(PlayerType.MY_PLAYER)
        self.showMyPlayersTable = ShowMyPlayerTable(self.tableViewMyPlayers, myPlayers, self.database)
        self.showMyPlayersTable.show()
        self.pushButtonAddMyPlayer.clicked.connect(lambda: self.addPlayer(PlayerType.MY_PLAYER))
        self.pushButtonUpdateMyPlayers.clicked.connect(lambda: self.updatePlayers(PlayerType.MY_PLAYER))
        self.pushButtonSelectItemsMyPlayers.clicked.connect(lambda: self.selectPlayerItems(self.showMyPlayersTable))
        self.pushButtonUpdateMyPlayersWar.clicked.connect(lambda: self.showPlayerWar(PlayerType.MY_PLAYER))
        self.pushButtonMakeFigMyPlayer.clicked.connect(lambda: self.makeFig(PlayerType.MY_PLAYER))

        # 关注部落界面
        clans = self.database.getClansAll()
        self.showClanTable = ShowClanTable(self.tableViewClans, clans, self.database)
        self.showClanTable.show()
        self.pushButtonUpdateClans.clicked.connect(lambda: self.updateClans())
        self.pushButtonAddClan.clicked.connect(lambda: self.addClan())
        self.pushButtonUpdateClanWar.clicked.connect(lambda: self.showClanWar())

        # 关注玩家界面
        focusPlayers = self.database.getPlayersAll(PlayerType.FOCUS_PLAYER)
        self.showFocusPlayerTable = ShowOtherPlayerTable(self.tableViewFocusPlayers, focusPlayers,
                                                         PlayerType.FOCUS_PLAYER, self.database)
        self.showFocusPlayerTable.show()
        self.pushButtonAddFocusPlayer.clicked.connect(lambda: self.addPlayer(PlayerType.FOCUS_PLAYER))
        self.pushButtonUpdateFocusPlayers.clicked.connect(lambda: self.updatePlayers(PlayerType.FOCUS_PLAYER))
        self.pushButtonSelectItemsFocusPlayers.clicked.connect(
            lambda: self.selectPlayerItems(self.showFocusPlayerTable))
        self.pushButtonFocusPlayerWar.clicked.connect(lambda: self.showPlayerWar(PlayerType.FOCUS_PLAYER))
        self.pushButtonMakeFigFocusPlayer.clicked.connect(lambda: self.makeFig(PlayerType.FOCUS_PLAYER))

        # 脚本号界面
        robots = self.database.getPlayersAll(PlayerType.ROBOT)
        self.showRobotTable = ShowOtherPlayerTable(self.tableViewRobots, robots, PlayerType.ROBOT, self.database)
        self.showRobotTable.show()
        self.pushButtonAddRobots.clicked.connect(lambda: self.exportRobots())
        self.pushButtonUpdateRobots.clicked.connect(lambda: self.updatePlayers(PlayerType.ROBOT))
        self.pushButtonSelectItemsRobots.clicked.connect(lambda: self.selectPlayerItems(self.showRobotTable))
        self.pushButtonWarRobots.clicked.connect(lambda: self.showPlayerWar(PlayerType.ROBOT))
        self.pushButtonMakeFigMyRobots.clicked.connect(lambda: self.makeFig(PlayerType.ROBOT))

        # 自动更新
        asyncio.run(self.autoUpdate())

    @asyncSlot()
    async def searchPlayerOnline(self):
        account = ClashAccount()
        try:
            await account.login()
        except Exception as _:
            self.labelResult.setText("连接失败")
        player = await account.searchPlayer(self.lineEditPlayerTag.text())
        await account.close()
        if player is not None:
            self.labelResult.setText(f"查询到玩家{player.name}")
            localPlayer = playersToLocal([player])[0]
            form = ShowLocalPlayerForm(localPlayer, PlayerType.ONLINE_PLAYER, self.database)
            form.setupUi(form)
            form.showLocalPlayerForm()
            form.exec()

    def addPlayer(self, type: PlayerType):
        dialog = AddPlayerDialog(type, self.database)
        dialog.setupUi(dialog)
        dialog.showDialog()
        dialog.exec()

    def addClan(self):
        dialog = AddClanDialog(self.database)
        dialog.setupUi(dialog)
        dialog.showDialog()
        dialog.exec()

    # 通过账号查询
    async def getCurrentPlayersInfo(self, type: PlayerType, account: ClashAccount):
        localPlayers = self.database.getPlayersAll(type)
        tags = [player.getInfo("Tag") for player in localPlayers]
        print(f"正在查询玩家{type}：", tags)
        players = []
        try:
            players = await account.searchPlayers(tags)
            print(f"查询玩家{type}成功：", players)
        except Exception as _:
            print(f"查询玩家{type}失败！")
        return players

    async def getCurrentClansInfo(self, account: ClashAccount):
        localClans = self.database.getClansAll()
        clanTags = [clan.getInfo("Tag") for clan in localClans]

        clans = []
        clanPlayers = []

        # 查询部落
        print("正在查询部落：", clanTags)
        try:
            clans = await account.searchClans(clanTags)
            print("查询部落成功：", clans)
        except Exception as _:
            print("查询部落失败！")

        playerTags = []
        publicClanTags = []
        for clan in clans:
            playerTags += list(clan.members_dict.keys())
            if clan.public_war_log:
                publicClanTags.append(clan.tag)

        # 查询部落成员
        print("正在查询部落成员：", playerTags)
        try:
            clanPlayers = await account.searchPlayers(playerTags)
            print(f"查询部落成员成功：", clanPlayers)
        except Exception as _:
            print(f"查询部落成员失败！")

        # 查询部落战日志
        warLogs = {}
        limits = self.getWarLogSearchLimit(publicClanTags)
        print("部落战记录查询场数：", limits)
        for tag in publicClanTags:
            logDatas = {}
            try:
                warLog = await account.searchWarLog(tag, limits[tag])
                logDatas = warLog._init_logs
            except Exception as _:
                print(f"查询部落{tag}对战记录失败！")
            logs = []
            for data in logDatas:
                try:
                    if data['attacksPerMember'] == 2:
                        logs.append(data)
                except Exception as _:
                    print("无此项信息")
            localLogDatas = warLogsToLocal(logs)
            warLogs[tag] = localLogDatas

        return clans, clanPlayers, warLogs

    def showPlayers(self, type: PlayerType, players: list[coc.Player]):
        self.database.updatePlayers(players, type)
        self.database.createPlayerDailyTable(type)
        self.database.updatePlayerDailyTable(players, type)
        localPlayersNew = self.database.getPlayersAll(type)
        if type == PlayerType.MY_PLAYER:
            self.showMyPlayersTable.resetPlayers(localPlayersNew)
            self.showMyPlayersTable.show()
            QMessageBox.about(self, "更新", "更新我的玩家成功！")
        elif type == PlayerType.ROBOT:
            self.showRobotTable.resetPlayers(localPlayersNew)
            self.showRobotTable.show()
            QMessageBox.about(self, "更新", "更新机器人成功！")
        elif type == PlayerType.FOCUS_PLAYER:
            self.showFocusPlayerTable.resetPlayers(localPlayersNew)
            self.showFocusPlayerTable.show()
            QMessageBox.about(self, "更新", "更新关注玩家成功！")

    def showClans(self, clans: list[coc.Clan], players: list[coc.Player], warLogs: dict[str, list[LocalWarLog]]):
        self.database.updateClans(clans)
        self.database.updateClanPlayers(players)
        self.database.createClanDailyTable()
        self.database.updateClanDailyTable(clans)
        self.database.updateWarLog(warLogs)
        localClansNew = self.database.getClansAll()
        self.showClanTable.resetClans(localClansNew)
        self.showClanTable.show()
        QMessageBox.about(self, "更新关注部落", "数据更新成功！")

    @asyncSlot()
    async def updatePlayers(self, type: PlayerType):
        account = ClashAccount()
        await account.login()
        players = await self.getCurrentPlayersInfo(type, account)
        self.showPlayers(type, players)

    @asyncSlot()
    async def updateClans(self):
        account = ClashAccount()
        await account.login()
        clans, players, warLogs = await self.getCurrentClansInfo(account)
        self.showClans(clans, players, warLogs)

    def selectPlayerItems(self, showPlayerTable: ShowPlayerTable):
        dialog = SelectPlayerItemsDialog(showPlayerTable)
        dialog.exec()

    @asyncSlot()
    async def showPlayerWar(self, playerType: PlayerType):
        clans = self.database.getClansAll()
        clanTags = [clan.getInfo('Tag') for clan in clans]
        account = ClashAccount()
        await account.login()
        wars = await account.searchWars(clanTags)
        print(wars)
        await account.close()
        players = self.database.getPlayersAll(playerType)
        playerTags = [player.getInfo("Tag") for player in players]
        form = ShowClanWar(playerType, wars, playerTags)
        form.exec()

    @asyncSlot()
    async def showClanWar(self):
        indexes = self.showClanTable.tableView.selectionModel().selectedRows()
        clanTags = []
        for index in indexes:
            clan = self.showClanTable.clans[index.row()]
            clanTags.append(clan.getInfo("Tag"))
        print(clanTags)
        account = ClashAccount()
        await account.login()
        wars = await account.searchWars(clanTags)
        print(wars)
        await account.close()
        playerTags = []
        for war in wars:
            if war is not None:
                for member in war.clan.members:
                    playerTags.append(member.tag)
        form = ShowClanWar(PlayerType.NO_TYPE, wars, playerTags)
        form.exec()

    def exportRobots(self):
        dialog = ImportRobotsDialog(self.database)
        dialog.exec()

    def makeFig(self, playerType: PlayerType):
        if playerType == PlayerType.MY_PLAYER:
            showTable = self.showMyPlayersTable
        elif playerType == PlayerType.FOCUS_PLAYER:
            showTable = self.showFocusPlayerTable
        elif playerType == PlayerType.ROBOT:
            showTable = self.showRobotTable
        else:
            return
        indexes = showTable.tableView.selectionModel().selectedRows()
        selectedPlayers = []
        for index in indexes:
            selectedPlayers.append(showTable.players[index.row()])
        print(selectedPlayers)
        figMaker = MakePlayerFigs(selectedPlayers, self.database, playerType)
        selectPlayerFigItems = SelectPlayerFigItems(figMaker, playerType)
        selectPlayerFigItems.exec()

    async def autoUpdate(self):
        currentTime = datetime.datetime(2000, 1, 1, 1, 1, 1)
        with open('Accounts/databaseFiles/lastUpdate.txt', 'r') as f:
            timeStr = f.read()
        update = False
        print(timeStr)
        if timeStr == "":
            update = True
        elif timeStr != "":
            time = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
            date = time.date()
            currentTime = datetime.datetime.now()
            if date != currentTime.date():
                update = True
        if update:
            # try:
            print("自动更新中")
            await self.updatePlayers(PlayerType.MY_PLAYER)
            await self.updatePlayers(PlayerType.FOCUS_PLAYER)
            await self.updatePlayers(PlayerType.ROBOT)
            await self.updateClans(True)
            with open('Accounts/databaseFiles/lastUpdate.txt', 'w') as fp:
                fp.write(currentTime.strftime('%Y-%m-%d %H:%M:%S'))
            QMessageBox.about(self, "自动更新", "开始自动更新")
            # except Exception as _:
            #     QMessageBox.about(self, "自动更新", "更新失败！")

    def getWarLogSearchLimit(self, tags: list[str]) -> dict[str, int]:
        limits = {}
        lastUpdates = {}
        date = datetime.date(2000, 1, 1)
        with open('Accounts/databaseFiles/warLogUpdate.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            tag, dateStr = line.split('=')
            date = datetime.datetime.strptime(dateStr, '%Y-%m-%d').date()
            lastUpdates[tag] = date
        oldTags = lastUpdates.keys()
        today = datetime.datetime.now().date()
        for tag in tags:
            if tag in oldTags:
                limit = (today - date).days // 2 + 1
            else:
                limit = 0
            limits[tag] = limit
        with open('Accounts/databaseFiles/warLogUpdate.txt', 'w') as fp:
            for tag in tags:
                fp.write(f'{tag}={today.strftime("%Y-%m-%d")}\n')
        return limits

