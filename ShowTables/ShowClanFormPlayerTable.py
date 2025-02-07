from ShowTables.ShowPlayerTable import ShowPlayerTable
from LocalClasses.LocalPlayer import LocalPlayer
from BasicData.Items import Items
from ShowTables import *
from BasicData.SelectMode import PlayerType
from Accounts.ClashDatabase import ClashDatabase

class ShowClanFormPlayerTable(ShowPlayerTable):
    def __init__(self, tableView: QTableView, players: list[LocalPlayer], database):
        super().__init__(tableView, players, PlayerType.CLAN_FORM_PLAYER, database)
        self.excludeInfos = ["Clan", "Clan Tag", "Email", "Bind Date"]
        self.infos = [info for info in Items.playerInfos if info not in self.excludeInfos]

    def generateModel(self):
        columns, model = self.generateBasicModel()
        return columns, model

    def show(self):
        columns, model = self.generateModel()
        self.setModel(model)

