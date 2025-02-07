from UI.DisplayClanForm import Ui_DisplayClanForm
from LocalClasses.LocalClan import LocalClan
from LocalClasses.LocalPlayer import LocalPlayer
from Utils.Caculations import caculateLeague
from BasicData.SelectMode import ClanType
from Accounts.ClashDatabase import ClashDatabase

from ShowForms import *
from ShowTables.ShowClanFormPlayerTable import ShowClanFormPlayerTable
from ShowForms.ShowWarLogForm import ShowWarLogForm
from ShowDialogs.SelectPlayerItemsDialog import SelectPlayerItemsDialog

class ShowLocalClanForm(Ui_DisplayClanForm, QDialog):
    def __init__(self, clan: LocalClan, players: list[LocalPlayer], clanType: ClanType, database: ClashDatabase):
        super().__init__()
        self.clan = clan
        self.players = players
        self.clanType = clanType
        self.database = database

    def showLocalClanForm(self):
        self.horizontalLayout_2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout_4.setAlignment(Qt.AlignmentFlag.AlignLeft)

        if self.clanType == ClanType.OFFLINE:
            self.pushButtonFocus.setHidden(True)

        self.labelName.setText(str(self.clan.getInfo("Name")))
        self.toolButtonTag.setText(self.clan.getInfo("Tag"))
        self.toolButtonMember.setIcon(QIcon("pictures/clan/info/memberCount.png"))
        self.toolButtonMember.setText(str(self.clan.getInfo("Member Count")))
        self.toolButtonType.setText(str(self.clan.getInfo("Type")))
        self.toolButtonLocation.setText(str(self.clan.getInfo("Location")))
        self.toolButtonWarFrequency.setIcon(QIcon("pictures/clan/info/warFrequency.png"))
        self.toolButtonWarFrequency.setText(self.clan.getInfo("War Frequency"))
        self.toolButtonRequiredTrophies.setIcon(QIcon("pictures/clan/info/required.png"))
        self.toolButtonRequiredTrophies.setText(str(self.clan.getInfo("Required Trophies")))
        self.toolButtonRequiredBuilderTrophies.setIcon(QIcon("pictures/clan/info/required.png"))
        self.toolButtonRequiredBuilderTrophies.setText(str(self.clan.getInfo("Required Builder Base Trophies")))
        self.toolButtonRequiredTownhall.setIcon(
            QIcon(f"pictures/player/townHall/th-{self.clan.getInfo('Required Townhall')}.png"))
        self.toolButtonRequiredTownhall.setText(str(self.clan.getInfo('Required Townhall')))

        self.toolButtonClanWarLeague.setText(str(self.clan.getInfo("War League")))
        self.toolButtonPonits.setText(str(self.clan.getInfo("Points")))
        self.toolButtonBuilderPoints.setText(str(self.clan.getInfo("Builder Base Points")))
        warIcon = QIcon("pictures/clan/info/war.png")
        self.toolButtonWarWinStreak.setStyleSheet("background:darkblue")
        self.toolButtonWarWinStreak.setIcon(warIcon)
        self.toolButtonWarWinStreak.setText(str(self.clan.getInfo("War Win Streak")))
        self.toolButtonWarWinStreak.setToolTip("连胜数")
        self.toolButtonWarWins.setStyleSheet("background:green")
        self.toolButtonWarWins.setIcon(warIcon)
        self.toolButtonWarWins.setText(str(self.clan.getInfo("War Wins")))
        self.toolButtonWarTies.setStyleSheet("background:gray")
        self.toolButtonWarTies.setIcon(warIcon)
        self.toolButtonWarTies.setText(str(self.clan.getInfo("War Ties")))
        self.toolButtonWarLosses.setStyleSheet("background:crimson")
        self.toolButtonWarLosses.setIcon(warIcon)
        self.toolButtonWarLosses.setText(str(self.clan.getInfo("War Losses")))

        if self.clan.getInfo("Capital Peak Level") > 0:
            self.toolButtonCapitalPeak.setIcon(
                QIcon(f"pictures/clan/capitalPeak/Capital_Hall{self.clan.getInfo('Capital Peak Level')}.png"))
            self.toolButtonCapitalPeak.setText(str(self.clan.getInfo('Capital Peak Level')))
            self.toolButtonCapitalPoints.setIcon(
                  QIcon(f"pictures/league/{caculateLeague(self.clan.getInfo('Capital Points'))}.png"))
            self.toolButtonCapitalPoints.setText(str(self.clan.getInfo("Capital Points")))
        else:
            self.toolButtonCapitalPeak.setHidden(True)
            self.toolButtonCapitalPoints.setHidden(True)

        item = QGraphicsPixmapItem(QPixmap(f"pictures/clan/flags/{self.clan.getInfo('Tag')}.png"))
        scene = QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphicsView.setScene(scene)

        self.plainTextEdit.setPlainText(str(self.clan.getInfo("Description")))
        if self.clan.getInfo("Public War Log") == False:
            self.pushButtonWarLog.setHidden(True)
            self.toolButtonWarTies.setHidden(True)
            self.toolButtonWarLosses.setHidden(True)

        # 显示部落成员
        self.showPlayerTable = ShowClanFormPlayerTable(self.tableView, self.players, self.database)
        self.showPlayerTable.show()

        self.pushButtonWarLog.clicked.connect(lambda: self.showWarLog())
        self.pushButtonSelectItems.clicked.connect(lambda: self.selectPlayerItems())

    def showWarLog(self):
        if self.clanType == ClanType.OFFLINE:
            logs = self.database.getWarLogs(self.clan.getInfo("Tag"))
        else:
            return
        form = ShowWarLogForm(logs)
        form.exec()

    def selectPlayerItems(self):
        dialog = SelectPlayerItemsDialog(self.showPlayerTable)
        dialog.exec()
