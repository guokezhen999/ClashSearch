import coc

from UI.ClanWarForm import Ui_ClanWar
from ShowForms import *
from BasicData.SelectMode import PlayerType, WarState
from BasicData.Items import Items

clanPlayers = dict[str, list[str]]
clanWars = list[coc.ClanWar]

class ShowClanWar(Ui_ClanWar, QDialog):
    def __init__(self, playerType: PlayerType, wars: list[coc.ClanWar], playerTags: list[str]):
        super().__init__()
        self.playerType = playerType
        self.wars = wars
        self.playerTags = playerTags
        self.warDict = self.generateWarDict(self.wars)
        self.setupUi(self)
        self.showPlayerClanWar()

    def showPlayerClanWar(self):
        inWars, endedWars, preWars = self.classifyClans(self.wars)
        clanPlayerDict1 = self.generateClanPlayerDict(inWars, self.playerTags)
        clanPlayerDict2= self.generateClanPlayerDict(preWars, self.playerTags)
        clanPlayerDict3 = self.generateClanPlayerDict(endedWars, self.playerTags)
        gridLayout = QGridLayout()
        startRows = 0
        frames = []
        for clanTag in clanPlayerDict1.keys():
            war = self.warDict[clanTag]
            playerTags = clanPlayerDict1[clanTag]
            frame = self.generateFormUnit(war, playerTags)
            frames.append(frame)
        for clanTag in clanPlayerDict2.keys():
            war = self.warDict[clanTag]
            playerTags = clanPlayerDict2[clanTag]
            frame = self.generateFormUnit(war, playerTags)
            frames.append(frame)
        for clanTag in clanPlayerDict3.keys():
            war = self.warDict[clanTag]
            playerTags = clanPlayerDict3[clanTag]
            frame = self.generateFormUnit(war, playerTags)
            frames.append(frame)
        for i, frame in enumerate(frames):
            gridLayout.addWidget(frame, i, 0, 1, 1)
        self.scrollAreaWidgetContents.setLayout(gridLayout)

    def classifyClans(self, wars: clanWars) -> tuple[clanWars, clanWars, clanWars]:
        inWars, warEndeds, preparations = [], [], []
        for war in wars:
            if war.state.value == WarState.IN_WAR.value[0]:
                inWars.append(war)
            elif war.state.value == WarState.PREPARATION.value[0]:
                warEndeds.append(war)
            elif war.state.value == WarState.WAR_ENDED.value[0]:
                preparations.append(war)
        return inWars, preparations, warEndeds

    def generateClanPlayerDict(self, wars: list[coc.ClanWar], playerTags: list[str]) -> clanPlayers:
        clanPlayerDict = {}
        for war in wars:
            players = []
            for tag in playerTags:
                if war.get_member(tag) is not None:
                    players.append(tag)
                    clanPlayerDict[war.clan_tag] = players
        print(clanPlayerDict)
        return clanPlayerDict

    def generateWarDict(self, wars: list[coc.ClanWar]) -> dict[str, coc.ClanWar]:
        warDict = {}
        for war in wars:
            warDict[war.clan_tag] = war
        return warDict

    def generateFormUnit(self, war: coc.ClanWar, playerTags: list[str]) -> QFrame:
        # 部落图标
        gridLayout = QGridLayout()
        clan1Url = war.clan.badge.url.split('/')[-1]
        clan2Url = war.opponent.badge.url.split('/')[-1]
        try:
            if os.path.exists(f"pictures/clan/warLogFlags/{clan1Url}") == False:
                image = requests.get(war.clan.badge.url)
                with open(f'pictures/clan/warLogFlags/{clan1Url}', 'wb') as f:
                    f.write(image.content)
                print(f"{clan1Url}保存成功")
            if os.path.exists(f"pictures/clan/warLogFlags/{clan2Url}") == False:
                image = requests.get(war.opponent.badge.url)
                with open(f'pictures/clan/warLogFlags/{clan2Url}', 'wb') as f:
                    f.write(image.content)
                print(f"{clan2Url}保存成功")
        except Exception as e:
            print("加载图片失败")
        graphicsView1 = QGraphicsView()
        graphicsView1.setMinimumSize(QSize(120, 120))
        graphicsView1.setMaximumSize(QSize(120, 120))
        item1 = QGraphicsPixmapItem(QPixmap(f"pictures/clan/warLogFlags/{clan1Url}"))
        item1.setScale(0.5)
        scene1 = QGraphicsScene()
        scene1.addItem(item1)
        graphicsView1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        graphicsView1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        graphicsView1.setScene(scene1)

        graphicsView2 = QGraphicsView()
        graphicsView2.setMinimumSize(QSize(120, 120))
        graphicsView2.setMaximumSize(QSize(120, 120))
        item2 = QGraphicsPixmapItem(QPixmap(f"pictures/clan/warLogFlags/{clan2Url}"))
        item2.setScale(0.5)
        scene2 = QGraphicsScene()
        scene2.addItem(item2)
        graphicsView2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        graphicsView2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        graphicsView2.setScene(scene2)

        # 部落名称
        font = QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        labelClan1 = QLabel(war.clan.name)
        labelClan1.setFont(font)
        labelClan2 = QLabel(war.opponent.name)
        labelClan2.setFont(font)
        labelClan1.setWordWrap(True)
        labelClan2.setWordWrap(True)

        # 对战情况
        font = QFont()
        font.setPointSize(14)
        starIcon = QIcon("pictures/war/star.png")
        toolButtonStar1 = QToolButton()
        toolButtonStar1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonStar1.setFont(font)
        toolButtonStar1.setText(str(war.clan.stars))
        toolButtonStar1.setIcon(starIcon)
        toolButtonStar2 = QToolButton()
        toolButtonStar2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonStar2.setFont(font)
        toolButtonStar2.setText(str(war.opponent.stars))
        toolButtonStar2.setIcon(starIcon)

        percentIcon = QIcon("pictures/war/percent.png")
        toolButtonPercent1 = QToolButton()
        toolButtonPercent1.setFont(font)
        toolButtonPercent1.setText(str(round(war.clan.destruction, 2)))
        toolButtonPercent1.setIcon(percentIcon)
        toolButtonPercent1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonPercent2 = QToolButton()
        toolButtonPercent2.setFont(font)
        toolButtonPercent2.setText(str(round(war.opponent.destruction, 2)))
        toolButtonPercent2.setIcon(percentIcon)
        toolButtonPercent2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        attackIcon = QIcon("pictures/war/attack.png")
        toolButtonAttack1 = QToolButton()
        toolButtonAttack1.setFont(font)
        toolButtonAttack1.setIcon(attackIcon)
        toolButtonAttack1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toolButtonAttack2 = QToolButton()
        toolButtonAttack2.setFont(font)
        toolButtonAttack2.setIcon(attackIcon)
        toolButtonAttack2.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        if war.state.value == WarState.PREPARATION.value[0]:
            toolButtonAttack1.setText(f'0/{war.team_size * war.attacks_per_member}')
            toolButtonAttack2.setText(f'0/{war.team_size * war.attacks_per_member}')
        else:
            toolButtonAttack1.setText(f'{war.clan.attacks_used}/{war.team_size * war.attacks_per_member}')
            toolButtonAttack2.setText(f'{war.opponent.attacks_used}/{war.team_size * war.attacks_per_member}')
        horizontalLayoutClan1 = QHBoxLayout()
        horizontalLayoutClan2 = QHBoxLayout()
        horizontalLayoutClan1.addWidget(toolButtonStar1)
        horizontalLayoutClan1.addWidget(toolButtonPercent1)
        horizontalLayoutClan1.addWidget(toolButtonAttack1)
        horizontalLayoutClan2.addWidget(toolButtonStar2)
        horizontalLayoutClan2.addWidget(toolButtonPercent2)
        horizontalLayoutClan2.addWidget(toolButtonAttack2)

        # 对战状态
        toolButtonState = QToolButton()
        toolButtonState.setFont(font)
        labelTime = QLabel()
        labelTime.setFont(QFont("Heiti SC", 14))
        timeEdit = QTimeEdit()
        timeEdit.setDisplayFormat('hh:mm:ss')
        timeEdit.setReadOnly(True)
        timeEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        if war.state.value == WarState.IN_WAR.value[0]:
            toolButtonState.setText("对 战 日")
            labelTime.setText("距离结束时间：")
            time = war.end_time.time + datetime.timedelta(hours=Items.timeZone) - datetime.datetime.now()
            seconds = int(time.total_seconds())
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            dateTime = QTime(hours, minutes, seconds)
            timeEdit.setTime(dateTime)
        elif war.state.value == WarState.WAR_ENDED.value[0]:
            toolButtonState.setText("对 战 结 束")
            labelTime.setHidden(True)
            timeEdit.setHidden(True)
        elif war.state.value == WarState.PREPARATION.value[0]:
            toolButtonState.setText("准 备 日")
            labelTime.setText("距离开战时间：")
            time = war.start_time.time + datetime.timedelta(hours=Items.timeZone) - datetime.datetime.now()
            seconds = int(time.total_seconds())
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60
            dateTime = QTime(hours, minutes, seconds)
            timeEdit.setTime(dateTime)

        # gridLayout加入对战信息
        gridLayout.addWidget(graphicsView1, 0, 0, 3, 1)
        gridLayout.addWidget(labelClan1, 0, 1, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        gridLayout.addWidget(labelClan2, 0, 4, 1, 3, Qt.AlignmentFlag.AlignHCenter)
        gridLayout.addWidget(graphicsView2, 0, 7, 3, 1)
        gridLayout.addLayout(horizontalLayoutClan1, 1, 1, 1, 3)
        gridLayout.addLayout(horizontalLayoutClan2, 1, 4, 1, 3)
        if war.state.value == WarState.IN_WAR.value[0] or war.state.value == WarState.PREPARATION.value[0]:
            horizontalLayoutTime = QHBoxLayout()
            horizontalLayoutTime.setAlignment(Qt.AlignmentFlag.AlignLeft)
            horizontalLayoutTime.addWidget(labelTime)
            horizontalLayoutTime.addWidget(timeEdit)
            gridLayout.addWidget(toolButtonState, 2, 1, 1, 2)
            gridLayout.addLayout(horizontalLayoutTime, 2, 3, 1, 4)
        else:
            gridLayout.addWidget(toolButtonState, 2, 1, 1, 6)

        # 成员信息
        font = QFont()
        font.setPointSize(14)
        gridLayoutAttacks = QGridLayout()
        maxAttacks = 0
        for row, tag in enumerate(playerTags):
            member = war.get_member(tag)
            toolButtonPosition = QToolButton()
            toolButtonPosition.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
            toolButtonPosition.setFont(font)
            toolButtonPosition.setText(str(member.map_position))
            style = "border-style: flat; background: transparent"
            toolButtonPosition.setStyleSheet(style)
            gridLayoutAttacks.addWidget(toolButtonPosition, row, 0, 1, 1)

            toolButtonTownhall = QToolButton()
            toolButtonTownhall.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            toolButtonTownhall.setFont(font)
            icon = QIcon(f"pictures/player/townHall/th-{member.town_hall}.png")
            toolButtonTownhall.setIcon(icon)
            toolButtonTownhall.setText(str(member.name))
            gridLayoutAttacks.addWidget(toolButtonTownhall, row, 1, 1, 1)

            attacks = member.attacks
            if len(attacks) > maxAttacks:
                maxAttacks = len(attacks)
            for i in range(len(attacks)):
                labelAttack1 = QLabel(f"第{i+1}次进攻：")
                labelAttack1.setFont(font)
                gridLayoutAttacks.addWidget(labelAttack1, row, 2 + 4 * i, 1, 1)

                toolButtonEnemyPosition1 = QToolButton()
                toolButtonEnemyPosition1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
                toolButtonEnemyPosition1.setFont(font)
                toolButtonEnemyPosition1.setStyleSheet(style)
                enemy1 = war.get_member(attacks[i].defender_tag)
                toolButtonEnemyPosition1.setText(str(enemy1.map_position))
                gridLayoutAttacks.addWidget(toolButtonEnemyPosition1, row, 4 * i + 3, 1, 1)

                toolButtonEnermyName1 = QToolButton()
                toolButtonEnermyName1.setFont(font)
                toolButtonEnermyName1.setIcon(QIcon(f'pictures/player/townHall/th-{enemy1.town_hall}.png'))
                toolButtonEnermyName1.setText(str(enemy1.name))
                toolButtonEnermyName1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                gridLayoutAttacks.addWidget(toolButtonEnermyName1, row, 4 * i + 4, 1, 1)

                toolButtonResult1 = QToolButton()
                toolButtonResult1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                toolButtonResult1.setFont(font)
                stars = attacks[i].stars
                percent = attacks[i].destruction
                toolButtonResult1.setIconSize(QSize(72, 24))
                toolButtonResult1.setIcon(QIcon(f'pictures/war/{stars}star.png'))
                toolButtonResult1.setText(f'{percent}%')
                gridLayoutAttacks.addWidget(toolButtonResult1, row, 4 * i + 5, 1, 1)

        gridLayout.addLayout(gridLayoutAttacks, 3, 0, len(playerTags), maxAttacks * 4 + 3)
        frame = QFrame()  # 创建实例
        frame.setFrameStyle(QFrame.Shape.Box)  # 框架样式
        frame.setLayout(gridLayout)

        return frame





