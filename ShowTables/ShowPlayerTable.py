from ShowTables import *
from BasicData.Items import Items
from BasicData.SelectMode import PlayerType
from LocalClasses.LocalPlayer import LocalPlayer
from ShowTables.PlayerItemDelegates import *
from ShowTables.IntItem import IntItem
from Accounts.ClashDatabase import ClashDatabase

class ShowPlayerTable:
    def __init__(self, tableView: QTableView, players: list[LocalPlayer], playType: PlayerType, database: ClashDatabase):
        self.tableView = tableView
        self.players = players
        self.playerType = playType
        self.database = database
        self.delegates = []

        self.infos = []
        self.heroes = []
        self.troops = []
        self.spells = []
        self.pets = []
        self.equipments = []
        self.heroesBuilder = []
        self.troopsBuilder = []
        self.achievements = []

        print(players[0].achievements)

    def generateBasicModel(self) -> tuple[int, QStandardItemModel]:
        model = QStandardItemModel()
        self.tableView.setIconSize(QSize(24, 24))
        # 设置表头
        model.setHorizontalHeaderItem(0, QStandardItem(str("详情")))
        self.delegates.append(0)
        columns = 1
        for i, name in enumerate(self.infos):
            model.setHorizontalHeaderItem(columns + i, QStandardItem(str(Items.playerInfosDict[name])))
        columns += len(self.infos)
        for i, name in enumerate(self.heroes):
            icon = QIcon(f"pictures/army/heroes/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.heroes)
        for i, name in enumerate(self.troops):
            icon = QIcon(f"pictures/army/troops/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.troops)
        for i, name in enumerate(self.spells):
            icon = QIcon(f"pictures/army/spells/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.spells)
        for i, name in enumerate(self.pets):
            icon = QIcon(f"pictures/army/pets/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.pets)
        for i, name in enumerate(self.equipments):
            icon = QIcon(f"pictures/army/equipments/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.equipments)
        for i, name in enumerate(self.heroesBuilder):
            icon = QIcon(f"pictures/army/builderHeroes/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.heroesBuilder)
        for i, name in enumerate(self.troopsBuilder):
            icon = QIcon(f"pictures/army/builderTroops/{name}.png")
            item = QStandardItem()
            item.setIcon(icon)
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.troopsBuilder)
        for i, name in enumerate(self.achievements):
            item = QStandardItem()
            item.setText(Items.playerAchievementsDict[name])
            model.setHorizontalHeaderItem(columns + i, item)
        columns += len(self.achievements)

        # 设置表体
        for row, player in enumerate(self.players):
            index = 1
            for col, name in enumerate(self.infos):
                item = QStandardItem()
                if name in Items.strPlayerInfos:
                    if name == "Role" and player.getInfo("Role") is not None:
                        item = QStandardItem(Items.roleDict[player.getInfo("Role")])
                    elif name == "Clan" and player.getInfo("Clan") is not None:
                        item = QStandardItem(str(player.getInfo(name)))
                        icon = QIcon(f"pictures/clan/flags/{player.getInfo('Clan Tag')}.png")
                        item.setIcon(icon)
                    else:
                        if player.getInfo(name) is None:
                            item = QStandardItem(str(""))
                        else:
                            item = QStandardItem(str(player.getInfo(name)))
                else:
                    if name == "Town Hall":
                        item = IntItem(str(player.getInfo(name)))
                        item.setIcon(QIcon(f"pictures/player/townHall/th-{player.getInfo('Town Hall')}.png"))
                    else:
                        if player.getInfo(name) is None:
                            item = IntItem(str("0"))
                        else:
                            item = IntItem(str(player.getInfo(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.infos)

            for col, name in enumerate(self.heroes):
                item = IntItem(str(player.getHero(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.heroes)
            for col, name in enumerate(self.troops):
                item = IntItem(str(player.getTroop(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.troops)
            for col, name in enumerate(self.spells):
                item = IntItem(str(player.getSpell(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.spells)
            for col, name in enumerate(self.pets):
                item = IntItem(str(player.getPet(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.pets)
            for col, name in enumerate(self.equipments):
                item = IntItem(str(player.getEquipment(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.equipments)
            for col, name in enumerate(self.heroesBuilder):
                item = IntItem(str(player.getHeroBuilder(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            index += len(self.heroesBuilder)
            for col, name in enumerate(self.troopsBuilder):
                item = IntItem(str(player.getTroopBuilder(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
            for col, name in enumerate(self.achievements):
                item = IntItem(str(player.getAchievement(name)))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                model.setItem(row, col + index, item)
        return columns, model

    def resetPlayers(self, players: list[LocalPlayer]):
        self.players = players

    def generateModel(self):
        pass

    def setModel(self, model: QStandardItemModel) -> None:
        self.tableView.setModel(model)
        self.tableView.setItemDelegateForColumn(0, ShowPlayerDetails(self.players, self.playerType,
                                                                     self.database, self.tableView))
        self.tableView.setSortingEnabled(True)
        self.tableView.resizeColumnsToContents()

    def show(self):
        pass

    def deleteDelegates(self):
        for index in self.delegates:
            self.tableView.setItemDelegateForColumn(index, None)
        self.delegates = []
