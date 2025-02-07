from ShowDialogs import *

from UI.ExportRobotsDialog import Ui_ExportRobotsDialog
from Accounts.ClashDatabase import ClashDatabase

class ImportRobotsDialog(Ui_ExportRobotsDialog, QDialog):
    def __init__(self, database: ClashDatabase):
        super().__init__()
        self.database = database
        self.filename = ""
        self.setupUi(self)
        self.pushButtonChooseFile.clicked.connect(lambda : self.chooseFile())
        self.pushButtonCommit.clicked.connect(lambda : self.commit(self.database))

    def chooseFile(self):
        file, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "文本文件(*.txt)")
        self.lineEdit.setText(file)
        self.tags = []
        with open(file, 'r') as fp:
            lines = fp.readlines()
            for line in lines:
                tag = line.split('-')[-1].replace('\n', '')
                if tag != "" and tag[0] == "#":
                    self.tags.append(tag)

    def commit(self, database: ClashDatabase):
        print(self.tags)
        try:
            nums = database.addRobots(self.tags)
            QMessageBox.about(self.sender(), "添加脚本号", f"共添加{nums}个脚本")
        except Exception as _:
            QMessageBox.about(self.sender(), "添加脚本号", "添加失败！")




