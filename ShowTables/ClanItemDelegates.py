from ShowTables import *
from LocalClasses.LocalClan import LocalClan
from Accounts.ClashDatabase import ClashDatabase
from ShowForms.ShowLocalClanForm import ShowLocalClanForm
from BasicData.SelectMode import ClanType

class ShowClanDetails(QItemDelegate):
    def __init__(self, clans: list[LocalClan], database: ClashDatabase, parent=None):
        super(ShowClanDetails, self).__init__(parent)
        self.clans = clans
        self.database = database

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            button = QToolButton()
            button.setIcon(QIcon("pictures/icons/detail.png"))
            button.index = [index.row(), index.column()]
            button.clicked.connect(self.showDetail)
            self.parent().setIndexWidget(index, button)

    def showDetail(self):
        clan = self.clans[self.parent().sender().index[0]]
        players = self.database.getPlayersByClanTag(clan.getInfo("Tag"))
        form = ShowLocalClanForm(clan, players, ClanType.OFFLINE, self.database)
        form.setupUi(form)
        form.showLocalClanForm()
        form.exec()

