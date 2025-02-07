import os.path

from ShowForms import *
from UI.WarLogForm import Ui_WarLogForm
from LocalClasses.LocalWarLog import LocalWarLog

class ShowWarLogForm(QDialog, Ui_WarLogForm):
    def __init__(self, warLogs: list[LocalWarLog]):
        super().__init__()
        self.setupUi(self)
        self.warLogs = warLogs
        self.warLogs.reverse()

        self.downloadFlags()
        self.showLogs()

    def showLogs(self):
        gridLayout = QGridLayout()
        units = []
        for log in self.warLogs:
            units.append(self.generateUnit(log))
        for i, unit in enumerate(units):
            gridLayout.addWidget(unit, i // 2, i % 2, 1, 1)
        self.scrollAreaWidgetContents.setLayout(gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    def downloadFlags(self):
        flagUrls = set()
        for log in self.warLogs:
            flagUrls.add(log.getInfo("Badge Url"))
            flagUrls.add(log.getInfo("Opponent Badge Url"))
        print(flagUrls)
        for url in flagUrls:
            if os.path.exists(f"pictures/clan/warLogFlags/{url}") == False:
                print(f"https://api-assets.clashofclans.com/badges/200/{url}下载中")
                try:
                    image = requests.get(f"https://api-assets.clashofclans.com/badges/200/{url}")
                    with open(f"pictures/clan/warLogFlags/{url}", 'wb') as fp:
                        fp.write(image.content)
                except Exception as e:
                    print(f"下载图片{url}失败!")

    def generateUnit(self, log: LocalWarLog) -> QFrame:
        teamSize = log.getInfo("Team Size")
        labelTeamSize = QLabel(f"{teamSize} VS {teamSize}")

        date: datetime.date = log.getInfo("End Time")
        dateEdit = QDateEdit(QDate(date.year, date.month, date.day))
        dateEdit.setCalendarPopup(False)
        dateEdit.setDisplayFormat("yyyy-MM-dd")
        dateEdit.setReadOnly(True)
        dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)

        toolButtonResult = QToolButton()
        toolButtonResult.setFont(QFont("Heiti sc", 14))
        toolButtonResult.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        toolButtonResult.setMinimumSize(200, 0)
        if log.getInfo("Result") == "win":
            toolButtonResult.setText("胜利")
            toolButtonResult.setStyleSheet("background: green;")
        elif log.getInfo("Result") == "lose":
            toolButtonResult.setText("失败")
            toolButtonResult.setStyleSheet("background: red;")
        else:
            toolButtonResult.setText("平局")
            toolButtonResult.setStyleSheet("background: gray;")

        font = QFont()
        font.setPointSize(14)
        gridLayoutClanInfo1 = QGridLayout()
        labelClanFlag1 = QLabel()
        labelClanFlag1.setPixmap(QPixmap(f"pictures/clan/warLogFlags/{log.getInfo('Badge Url')}"))
        labelClanFlag1.setScaledContents(True)
        labelClanFlag1.setMaximumSize(QSize(80, 80))
        labelClan1 = QLabel()
        labelClan1.setFont(font)
        labelClan1.setWordWrap(True)
        labelClan1.setText(str(log.getInfo("Name")))
        labelClanLevel1 = QLabel(f"等级：{log.getInfo('Clan Level')}")
        gridLayoutClanInfo1.addWidget(labelClanFlag1, 0, 0, 2, 1)
        gridLayoutClanInfo1.addWidget(labelClan1, 0, 1, 1, 1)
        gridLayoutClanInfo1.addWidget(labelClanLevel1, 1, 1, 1, 1)

        gridLayoutClanInfo2 = QGridLayout()
        labelClanFlag2 = QLabel()
        labelClanFlag2.setPixmap(QPixmap(f"pictures/clan/warLogFlags/{log.getInfo('Opponent Badge Url')}"))
        labelClanFlag2.setScaledContents(True)
        labelClanFlag2.setMaximumSize(QSize(80, 80))
        labelClan2 = QLabel()
        labelClan2.setFont(font)
        labelClan2.setWordWrap(True)
        labelClan2.setText(str(log.getInfo("Opponent Name")))
        labelClanLevel2 = QLabel(f"等级：{log.getInfo('Opponent Clan Level')}")
        gridLayoutClanInfo2.addWidget(labelClanFlag2, 0, 0, 2, 1)
        gridLayoutClanInfo2.addWidget(labelClan2, 0, 1, 1, 1)
        gridLayoutClanInfo2.addWidget(labelClanLevel2, 1, 1, 1, 1)

        horizontalLayoutStarPercent1 = QHBoxLayout()
        toolButtonStar1 = QToolButton()
        toolButtonStar1.setFont(font)
        toolButtonStar1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonStar1.setText(str(log.getInfo('Stars')))
        toolButtonStar1.setIcon(QIcon("pictures/war/star.png"))
        toolButtonPercent1 = QToolButton()
        toolButtonPercent1.setFont(font)
        toolButtonPercent1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonPercent1.setText(str(log.getInfo('Destruction Percentage')))
        toolButtonPercent1.setIcon(QIcon("pictures/war/percent.png"))
        horizontalLayoutStarPercent1.addWidget(toolButtonStar1)
        horizontalLayoutStarPercent1.addWidget(toolButtonPercent1)
        horizontalLayoutStarPercent1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        horizontalLayoutStarPercent2 = QHBoxLayout()
        toolButtonStar2 = QToolButton()
        toolButtonStar2.setFont(font)
        toolButtonStar2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonStar2.setText(str(log.getInfo('Opponent Stars')))
        toolButtonStar2.setIcon(QIcon("pictures/war/star.png"))
        toolButtonPercent2 = QToolButton()
        toolButtonPercent2.setFont(font)
        toolButtonPercent2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonPercent2.setText(str(log.getInfo('Opponent Destruction Percentage')))
        toolButtonPercent2.setIcon(QIcon("pictures/war/percent.png"))
        horizontalLayoutStarPercent2.addWidget(toolButtonStar2)
        horizontalLayoutStarPercent2.addWidget(toolButtonPercent2)
        horizontalLayoutStarPercent2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        toolButtonAttacks = QToolButton()
        toolButtonAttacks.setFont(font)
        toolButtonAttacks.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonAttacks.setText(f"{log.getInfo('Attacks')} / {log.getInfo('Team Size') * 2}")
        toolButtonAttacks.setIcon(QIcon("pictures/war/attack.png"))

        gridLayout = QGridLayout()
        gridLayout.addWidget(labelTeamSize, 0, 0, 1, 1)
        gridLayout.addWidget(dateEdit, 0, 1, 1, 1)
        gridLayout.addWidget(toolButtonResult, 1, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        gridLayout.addLayout(gridLayoutClanInfo1, 2, 0, 1, 1)
        gridLayout.addLayout(gridLayoutClanInfo2, 2, 1, 1, 1)
        gridLayout.addLayout(horizontalLayoutStarPercent1, 3, 0, 1, 1)
        gridLayout.addLayout(horizontalLayoutStarPercent2, 3, 1, 1, 1)
        gridLayout.addWidget(toolButtonAttacks, 4, 0, 1, 1, Qt.AlignmentFlag.AlignCenter)

        frame = QFrame()  # 创建实例
        frame.setFrameStyle(QFrame.Shape.Box)  # 框架样式
        frame.setLayout(gridLayout)

        return frame





