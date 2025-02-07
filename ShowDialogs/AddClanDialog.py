from ShowDialogs import *
from UI.AddClanDialog import Ui_AddClanDialog
from Accounts.ClashDatabase import ClashDatabase

class AddClanDialog(Ui_AddClanDialog, QDialog):
    def __init__(self, database: ClashDatabase):
        super().__init__()
        self.database = database

    def showDialog(self):
        self.setWindowTitle("添加部落")
        self.pushButtonAddClan.clicked.connect(self.addClan)

    def addClan(self):
        tag = self.lineEditTag.text()
        if tag == "":
            self.labelResult.setText('必须填写标签！')
            return
        elif tag[0] != "#":
            self.labelResult.setText('标签必须以"#"开头！')
            return
        try:
            self.database.addClan(tag)
            self.label.setText("添加成功！")
        except Exception as e:
            self.label.setText("标签重复！")
        self.lineEditTag.setText("")