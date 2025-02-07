import datetime

from UI.AddPlayerDialog import Ui_AddPlayerDialog
from ShowDialogs import *
from BasicData.SelectMode import PlayerType
from Accounts.ClashDatabase import ClashDatabase
from LocalClasses.LocalPlayer import LocalPlayer

class EditPlayerDialog(Ui_AddPlayerDialog, QDialog):
    def __init__(self, playerType: PlayerType, database: ClashDatabase, player: LocalPlayer):
        super().__init__()
        self.playerType = playerType
        self.database = database
        self.player = player
        self.initTag = player.getInfo("Tag")

    def showDialog(self):
        self.setWindowTitle("修改玩家")
        self.pushButton.setText("修改玩家")
        self.lineEditTag.setText(self.player.getInfo("Tag"))
        if self.playerType == PlayerType.MY_PLAYER:
            self.dateEdit.setDate(QDate.currentDate())
            self.radioButtonTag.setChecked(True)
            self.radioButtonTag.setEnabled(False)
            self.labelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.lineEditEmail.setEnabled(False)
            self.dateEdit.setEnabled(False)
            self.lineEditEmail.setText(self.player.getInfo("Email"))
            date = self.player.getInfo("Bind Date")
            if date is not None:
                self.dateEdit.setDate(QDate(date.year, date.month, date.day))
            self.radioButtonEmail.clicked.connect(self.emailButtonClicked)
            self.radioButtonBindDate.clicked.connect(self.dateButtonClicked)
        else:
            self.radioButtonTag.setHidden(True)
            self.radioButtonEmail.setHidden(True)
            self.radioButtonBindDate.setHidden(True)
            self.lineEditEmail.setHidden(True)
            self.dateEdit.setHidden(True)
        self.pushButton.clicked.connect(self.editPlayer)

    def editPlayer(self):
        playerDict = dict()
        tag = self.lineEditTag.text()
        if tag == "":
            self.labelResult.setText('必须填写标签！')
            return
        elif tag[0] != "#":
            self.labelResult.setText('标签必须以"#"开头！')
            return
        playerDict["tag"] = tag
        playerDict["initTag"] = self.initTag
        if self.playerType == PlayerType.MY_PLAYER:
            if self.radioButtonEmail.isChecked():
                email = self.lineEditEmail.text()
                if email == "":
                    self.labelResult.setText("请填写邮箱")
                    return
                playerDict["email"] = email
            if self.radioButtonBindDate.isChecked():
                date = self.dateEdit.date().toString("yyyy-MM-dd")
                playerDict["bind_date"] = date
        try:
            print(playerDict)
            self.database.editPlayer(playerDict, self.playerType)
        except Exception as e:
            self.labelResult.setText("标签重复！")
        self.labelResult.setText("修改成功！")

    def emailButtonClicked(self):
        if self.radioButtonEmail.isChecked():
            self.lineEditEmail.setEnabled(True)
        else:
            self.lineEditEmail.setEnabled(False)

    def dateButtonClicked(self):
        if self.radioButtonBindDate.isChecked():
            self.dateEdit.setEnabled(True)
        else:
            self.dateEdit.setEnabled(False)