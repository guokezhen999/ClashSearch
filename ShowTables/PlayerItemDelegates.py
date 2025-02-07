from ShowTables import *
from ShowForms.ShowLocalPlayerForm import ShowLocalPlayerForm
from BasicData.SelectMode import PlayerType
from LocalClasses.LocalPlayer import LocalPlayer, playersToLocal
from LocalClasses.LocalClan import LocalClan
from Accounts.ClashDatabase import ClashDatabase
from ShowDialogs.EditPlayerDialog import EditPlayerDialog

class ShowPlayerDetails(QItemDelegate):
    def __init__(self, players: list[LocalPlayer], flag: PlayerType, database: ClashDatabase, parent=None):
        super(ShowPlayerDetails, self).__init__(parent)
        self.players = players
        self.flag = flag
        self.database = database

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button = QToolButton()
            button.setIcon(QIcon("pictures/icons/detail.png"))
            button.index = [index.row(), index.column()]
            button.clicked.connect(self.showDetail)
            self.parent().setIndexWidget(index, button)

    def showDetail(self) -> None:
        ui = ShowLocalPlayerForm(self.players[self.parent().sender().index[0]], self.flag, self.database)
        dialog = QDialog()
        ui.setupUi(dialog)
        ui.showLocalPlayerForm()
        dialog.exec()


class EditPlayerInfos(QItemDelegate):
    def __init__(self, players: list[LocalPlayer], database: ClashDatabase, playerType: PlayerType, parent=None):
        super(EditPlayerInfos, self).__init__(parent)
        self.players = players
        self.playerType = playerType
        self.database = database

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button = QToolButton()
            button.setIcon(QIcon("pictures/icons/edit.png"))
            button.index = [index.row(), index.column()]
            button.clicked.connect(self.editPlayer)
            self.parent().setIndexWidget(index, button)

    def editPlayer(self):
        player = self.players[self.parent().sender().index[0]]
        ui = EditPlayerDialog(self.playerType, self.database, player)
        ui.setupUi(ui)
        ui.showDialog()
        ui.exec()

class DeletePlayer(QItemDelegate):
    def __init__(self, players: list[LocalPlayer], database: ClashDatabase, playerType: PlayerType, parent=None):
        super(DeletePlayer, self).__init__(parent)
        self.players = players
        self.playerType = playerType
        self.database = database

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button = QToolButton()
            button.setIcon(QIcon("pictures/icons/delete.png"))
            button.index = [index.row(), index.column()]
            button.clicked.connect(self.deletePlayer)
            self.parent().setIndexWidget(index, button)

    def deletePlayer(self):
        player = self.players[self.parent().sender().index[0]]
        confirm = QMessageBox.question(self.parent(), "删除玩家", f"你确定要删除玩家{player.getInfo('Name')}吗？",
                                       QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            self.database.deletePlayer(player.getInfo("Tag"), self.playerType)


