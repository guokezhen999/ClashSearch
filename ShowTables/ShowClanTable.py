from ShowTables import *

from BasicData.Items import Items
from ShowTables.ClanItemDelegates import *
from ShowTables.IntItem import IntItem

class ShowClanTable:
    def __init__(self, tableView: QTableView, clans: list[LocalClan], database: ClashDatabase):
        self.tableView = tableView
        self.clans = clans
        self.database = database
        self.delegates = []
        self.infos = [info for info in Items.clanInfos]

    def generateModel(self) -> tuple[int, QStandardItemModel]:
        model = QStandardItemModel()
        self.tableView.setIconSize(QSize(24, 24))
        # 设置表头
        model.setHorizontalHeaderItem(0, QStandardItem(str("详情")))
        self.delegates.append(0)
        columns = 1
        for i, name in enumerate(self.infos):
            model.setHorizontalHeaderItem(columns + i, QStandardItem(str(Items.clanInfosDict[name])))
        columns += len(self.infos)

        # 设置表体
        for row, clan in enumerate(self.clans):
            index = 1
            for col, name in enumerate(self.infos):
                if name == "Name":
                    icon = QIcon(QPixmap(f"pictures/clan/flags/{clan.getInfo('Tag')}.png"))
                    item = QStandardItem(icon, clan.getInfo("Name"))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                elif name == "Public War Log":
                    item = QStandardItem("是") if clan.getInfo(name) == 1 else QStandardItem("否")
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                else:
                    if name not in Items.intClanInfos:
                        item = QStandardItem(str(clan.getInfo(name)))
                        if name == "Description":
                            item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
                            item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
                        else:
                            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    else:
                        item = IntItem(str(clan.getInfo(name)))
                model.setItem(row, col + index, item)

        return columns, model

    def resetClans(self, clans: list[LocalClan]):
        self.clans = clans

    def deleteDelegates(self):
        for index in self.delegates:
            self.tableView.setItemDelegateForColumn(index, None)
        self.delegates = []

    def show(self):
        columns, model = self.generateModel()

        self.tableView.setItemDelegateForColumn(0, ShowClanDetails(self.clans, self.database, self.tableView))
        self.delegates.append(0)

        self.tableView.setModel(model)
        self.tableView.setSortingEnabled(True)
        self.tableView.resizeColumnsToContents()

