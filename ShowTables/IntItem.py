from ShowTables import *

class IntItem(QStandardItem):
    def __lt__(self, other):
        return int(self.text()) < int(other.text())