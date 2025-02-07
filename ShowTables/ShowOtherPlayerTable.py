from ShowTables import *
from ShowTables.PlayerItemDelegates import *
from ShowTables.ShowPlayerTable import ShowPlayerTable
from LocalClasses.LocalPlayer import LocalPlayer
from BasicData.SelectMode import PlayerType
from Accounts.ClashDatabase import ClashDatabase
from BasicData.Items import Items

class ShowOtherPlayerTable(ShowPlayerTable):
    def __init__(self, tableView: QTableView, players: list[LocalPlayer], playerType: PlayerType,
                 database: ClashDatabase):
        super().__init__(tableView, players, playerType, database)
        self.excludeInfos = ["Clan Tag", "Bind Date", "Email"]
        self.infos = [info for info in Items.playerInfos if info not in self.excludeInfos]

    def generateModel(self) -> tuple[int, QStandardItemModel]:
        columns, model = self.generateBasicModel()
        # 设置表头
        model.setHorizontalHeaderItem(columns, QStandardItem(str("修改")))
        model.setHorizontalHeaderItem(columns + 1, QStandardItem(str("删除")))
        return columns, model

    def show(self):
        columns, model = self.generateModel()
        self.tableView.setItemDelegateForColumn(columns, EditPlayerInfos(self.players, self.database,
                                                                         self.playerType, self.tableView))
        self.tableView.setItemDelegateForColumn(columns + 1, DeletePlayer(self.players, self.database,
                                                                          self.playerType, self.tableView))
        self.delegates.append(columns)
        self.delegates.append(columns + 1)
        self.setModel(model)
