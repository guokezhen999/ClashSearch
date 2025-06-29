# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.splitter = QtWidgets.QSplitter(parent=self.tab)
        self.splitter.setGeometry(QtCore.QRect(320, 150, 560, 360))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPlayerTag = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelPlayerTag.setFont(font)
        self.labelPlayerTag.setObjectName("labelPlayerTag")
        self.horizontalLayout.addWidget(self.labelPlayerTag)
        self.lineEditPlayerTag = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEditPlayerTag.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditPlayerTag.setFont(font)
        self.lineEditPlayerTag.setObjectName("lineEditPlayerTag")
        self.horizontalLayout.addWidget(self.lineEditPlayerTag)
        self.pushButtonSearchPlayer = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonSearchPlayer.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchPlayer.setFont(font)
        self.pushButtonSearchPlayer.setObjectName("pushButtonSearchPlayer")
        self.horizontalLayout.addWidget(self.pushButtonSearchPlayer)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelClanTag = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelClanTag.setFont(font)
        self.labelClanTag.setObjectName("labelClanTag")
        self.horizontalLayout_2.addWidget(self.labelClanTag)
        self.lineEditClanTag = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.lineEditClanTag.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditClanTag.setFont(font)
        self.lineEditClanTag.setObjectName("lineEditClanTag")
        self.horizontalLayout_2.addWidget(self.lineEditClanTag)
        self.pushButtonSearchClanByTag = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.pushButtonSearchClanByTag.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchClanByTag.setFont(font)
        self.pushButtonSearchClanByTag.setObjectName("pushButtonSearchClanByTag")
        self.horizontalLayout_2.addWidget(self.pushButtonSearchClanByTag)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelClanName = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelClanName.setFont(font)
        self.labelClanName.setObjectName("labelClanName")
        self.horizontalLayout_3.addWidget(self.labelClanName)
        self.lineEditClanName = QtWidgets.QLineEdit(parent=self.layoutWidget_2)
        self.lineEditClanName.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditClanName.setFont(font)
        self.lineEditClanName.setObjectName("lineEditClanName")
        self.horizontalLayout_3.addWidget(self.lineEditClanName)
        self.pushButtonSearchClanByName = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        self.pushButtonSearchClanByName.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchClanByName.setFont(font)
        self.pushButtonSearchClanByName.setObjectName("pushButtonSearchClanByName")
        self.horizontalLayout_3.addWidget(self.pushButtonSearchClanByName)
        self.labelResult = QtWidgets.QLabel(parent=self.splitter)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableViewMyPlayers = QtWidgets.QTableView(parent=self.tab_2)
        self.tableViewMyPlayers.setObjectName("tableViewMyPlayers")
        self.verticalLayout_2.addWidget(self.tableViewMyPlayers)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonAddMyPlayer = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAddMyPlayer.setFont(font)
        self.pushButtonAddMyPlayer.setObjectName("pushButtonAddMyPlayer")
        self.horizontalLayout_4.addWidget(self.pushButtonAddMyPlayer)
        self.pushButtonSelectItemsMyPlayers = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSelectItemsMyPlayers.setFont(font)
        self.pushButtonSelectItemsMyPlayers.setObjectName("pushButtonSelectItemsMyPlayers")
        self.horizontalLayout_4.addWidget(self.pushButtonSelectItemsMyPlayers)
        self.pushButtonUpdateMyPlayers = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateMyPlayers.setFont(font)
        self.pushButtonUpdateMyPlayers.setObjectName("pushButtonUpdateMyPlayers")
        self.horizontalLayout_4.addWidget(self.pushButtonUpdateMyPlayers)
        self.pushButtonUpdateMyPlayersWar = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateMyPlayersWar.setFont(font)
        self.pushButtonUpdateMyPlayersWar.setObjectName("pushButtonUpdateMyPlayersWar")
        self.horizontalLayout_4.addWidget(self.pushButtonUpdateMyPlayersWar)
        self.pushButtonSearchMyPlayers = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchMyPlayers.setFont(font)
        self.pushButtonSearchMyPlayers.setObjectName("pushButtonSearchMyPlayers")
        self.horizontalLayout_4.addWidget(self.pushButtonSearchMyPlayers)
        self.pushButtonMakeFigMyPlayer = QtWidgets.QPushButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMakeFigMyPlayer.setFont(font)
        self.pushButtonMakeFigMyPlayer.setObjectName("pushButtonMakeFigMyPlayer")
        self.horizontalLayout_4.addWidget(self.pushButtonMakeFigMyPlayer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableViewClans = QtWidgets.QTableView(parent=self.tab_4)
        self.tableViewClans.setObjectName("tableViewClans")
        self.verticalLayout_4.addWidget(self.tableViewClans)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonAddClan = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAddClan.setFont(font)
        self.pushButtonAddClan.setObjectName("pushButtonAddClan")
        self.horizontalLayout_6.addWidget(self.pushButtonAddClan)
        self.pushButtonSelectItemsClans = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSelectItemsClans.setFont(font)
        self.pushButtonSelectItemsClans.setObjectName("pushButtonSelectItemsClans")
        self.horizontalLayout_6.addWidget(self.pushButtonSelectItemsClans)
        self.pushButtonUpdateClans = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateClans.setFont(font)
        self.pushButtonUpdateClans.setObjectName("pushButtonUpdateClans")
        self.horizontalLayout_6.addWidget(self.pushButtonUpdateClans)
        self.pushButtonUpdateClanWar = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateClanWar.setFont(font)
        self.pushButtonUpdateClanWar.setObjectName("pushButtonUpdateClanWar")
        self.horizontalLayout_6.addWidget(self.pushButtonUpdateClanWar)
        self.pushButtonUpdateClanWarLeague = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateClanWarLeague.setFont(font)
        self.pushButtonUpdateClanWarLeague.setObjectName("pushButtonUpdateClanWarLeague")
        self.horizontalLayout_6.addWidget(self.pushButtonUpdateClanWarLeague)
        self.pushButtonSearchClan = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchClan.setFont(font)
        self.pushButtonSearchClan.setObjectName("pushButtonSearchClan")
        self.horizontalLayout_6.addWidget(self.pushButtonSearchClan)
        self.pushButtonMakeFigMyPlayer_2 = QtWidgets.QPushButton(parent=self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMakeFigMyPlayer_2.setFont(font)
        self.pushButtonMakeFigMyPlayer_2.setObjectName("pushButtonMakeFigMyPlayer_2")
        self.horizontalLayout_6.addWidget(self.pushButtonMakeFigMyPlayer_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableViewFocusPlayers = QtWidgets.QTableView(parent=self.tab_5)
        self.tableViewFocusPlayers.setObjectName("tableViewFocusPlayers")
        self.verticalLayout_3.addWidget(self.tableViewFocusPlayers)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonAddFocusPlayer = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAddFocusPlayer.setFont(font)
        self.pushButtonAddFocusPlayer.setObjectName("pushButtonAddFocusPlayer")
        self.horizontalLayout_5.addWidget(self.pushButtonAddFocusPlayer)
        self.pushButtonSelectItemsFocusPlayers = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSelectItemsFocusPlayers.setFont(font)
        self.pushButtonSelectItemsFocusPlayers.setObjectName("pushButtonSelectItemsFocusPlayers")
        self.horizontalLayout_5.addWidget(self.pushButtonSelectItemsFocusPlayers)
        self.pushButtonUpdateFocusPlayers = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateFocusPlayers.setFont(font)
        self.pushButtonUpdateFocusPlayers.setObjectName("pushButtonUpdateFocusPlayers")
        self.horizontalLayout_5.addWidget(self.pushButtonUpdateFocusPlayers)
        self.pushButtonFocusPlayerWar = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonFocusPlayerWar.setFont(font)
        self.pushButtonFocusPlayerWar.setObjectName("pushButtonFocusPlayerWar")
        self.horizontalLayout_5.addWidget(self.pushButtonFocusPlayerWar)
        self.pushButtonSearchFocusPlayer = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchFocusPlayer.setFont(font)
        self.pushButtonSearchFocusPlayer.setObjectName("pushButtonSearchFocusPlayer")
        self.horizontalLayout_5.addWidget(self.pushButtonSearchFocusPlayer)
        self.pushButtonMakeFigFocusPlayer = QtWidgets.QPushButton(parent=self.tab_5)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMakeFigFocusPlayer.setFont(font)
        self.pushButtonMakeFigFocusPlayer.setObjectName("pushButtonMakeFigFocusPlayer")
        self.horizontalLayout_5.addWidget(self.pushButtonMakeFigFocusPlayer)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_5, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tableViewRobots = QtWidgets.QTableView(parent=self.widget)
        self.tableViewRobots.setObjectName("tableViewRobots")
        self.verticalLayout_6.addWidget(self.tableViewRobots)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButtonAddRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAddRobots.setFont(font)
        self.pushButtonAddRobots.setObjectName("pushButtonAddRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonAddRobots)
        self.pushButtonSelectItemsRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSelectItemsRobots.setFont(font)
        self.pushButtonSelectItemsRobots.setObjectName("pushButtonSelectItemsRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonSelectItemsRobots)
        self.pushButtonUpdateRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateRobots.setFont(font)
        self.pushButtonUpdateRobots.setObjectName("pushButtonUpdateRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonUpdateRobots)
        self.pushButtonWarRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonWarRobots.setFont(font)
        self.pushButtonWarRobots.setObjectName("pushButtonWarRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonWarRobots)
        self.pushButtonSearchRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearchRobots.setFont(font)
        self.pushButtonSearchRobots.setObjectName("pushButtonSearchRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonSearchRobots)
        self.pushButtonMakeFigMyRobots = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonMakeFigMyRobots.setFont(font)
        self.pushButtonMakeFigMyRobots.setObjectName("pushButtonMakeFigMyRobots")
        self.horizontalLayout_11.addWidget(self.pushButtonMakeFigMyRobots)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.tabWidget.addTab(self.widget, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clash Search"))
        self.labelPlayerTag.setText(_translate("MainWindow", "玩家标签："))
        self.pushButtonSearchPlayer.setText(_translate("MainWindow", "查询"))
        self.labelClanTag.setText(_translate("MainWindow", "部落标签："))
        self.pushButtonSearchClanByTag.setText(_translate("MainWindow", "查询"))
        self.labelClanName.setText(_translate("MainWindow", "部落名称："))
        self.pushButtonSearchClanByName.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "即时查询"))
        self.pushButtonAddMyPlayer.setText(_translate("MainWindow", "增加玩家"))
        self.pushButtonSelectItemsMyPlayers.setText(_translate("MainWindow", "选择属性"))
        self.pushButtonUpdateMyPlayers.setText(_translate("MainWindow", "更新信息"))
        self.pushButtonUpdateMyPlayersWar.setText(_translate("MainWindow", "部落战查询"))
        self.pushButtonSearchMyPlayers.setText(_translate("MainWindow", "查找玩家"))
        self.pushButtonMakeFigMyPlayer.setText(_translate("MainWindow", "绘制图表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "我的玩家"))
        self.pushButtonAddClan.setText(_translate("MainWindow", "增加部落"))
        self.pushButtonSelectItemsClans.setText(_translate("MainWindow", "选择属性"))
        self.pushButtonUpdateClans.setText(_translate("MainWindow", "更新信息"))
        self.pushButtonUpdateClanWar.setText(_translate("MainWindow", "部落战查询"))
        self.pushButtonUpdateClanWarLeague.setText(_translate("MainWindow", "联赛查询"))
        self.pushButtonSearchClan.setText(_translate("MainWindow", "查找部落"))
        self.pushButtonMakeFigMyPlayer_2.setText(_translate("MainWindow", "绘制图表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "关注部落"))
        self.pushButtonAddFocusPlayer.setText(_translate("MainWindow", "增加玩家"))
        self.pushButtonSelectItemsFocusPlayers.setText(_translate("MainWindow", "选择属性"))
        self.pushButtonUpdateFocusPlayers.setText(_translate("MainWindow", "更新信息"))
        self.pushButtonFocusPlayerWar.setText(_translate("MainWindow", "部落战查询"))
        self.pushButtonSearchFocusPlayer.setText(_translate("MainWindow", "查找玩家"))
        self.pushButtonMakeFigFocusPlayer.setText(_translate("MainWindow", "绘制图表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "关注玩家"))
        self.pushButtonAddRobots.setText(_translate("MainWindow", "导入标签"))
        self.pushButtonSelectItemsRobots.setText(_translate("MainWindow", "选择属性"))
        self.pushButtonUpdateRobots.setText(_translate("MainWindow", "更新信息"))
        self.pushButtonWarRobots.setText(_translate("MainWindow", "部落战查询"))
        self.pushButtonSearchRobots.setText(_translate("MainWindow", "查找玩家"))
        self.pushButtonMakeFigMyRobots.setText(_translate("MainWindow", "绘制图表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "脚本号"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
