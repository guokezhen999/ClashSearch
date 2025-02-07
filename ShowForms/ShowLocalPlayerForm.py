from UI.DisplayPlayerForm import Ui_ShowPlayerForm
from LocalClasses.LocalPlayer import LocalPlayer
from BasicData.SelectMode import PlayerType
from BasicData.Items import Items
from Accounts.ClashDatabase import ClashDatabase
from ShowForms import *
from Utils.Caculations import caculateLeague
from Utils.CreateUI import CreateUI

class ShowLocalPlayerForm(Ui_ShowPlayerForm, QDialog):
    def __init__(self, player: LocalPlayer, playerType: PlayerType, database: ClashDatabase = None):
        super().__init__()
        self.player = player
        self.playerType = playerType
        self.database = database

    def hiddenFocusButton(self) -> bool:
        if self.playerType == PlayerType.CLAN_FORM_PLAYER or self.playerType == PlayerType.CLAN_PLAYER \
                or self.playerType == PlayerType.ONLINE_PLAYER:
            focusPlayers = self.database.getPlayersAll(PlayerType.FOCUS_PLAYER)
            focusTags = [player.getInfo("Tag") for player in focusPlayers]
            if self.player.getInfo("Tag") in focusTags:
                return True
            return False
        return True

    def addFocusPlayer(self):
        playerDict = {"tag": self.player.getInfo("Tag")}
        self.database.addPlayer(playerDict, PlayerType.FOCUS_PLAYER)

    def showLocalPlayerForm(self):
        self.horizontalLayoutInfo1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayoutInfo2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayoutTitle.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayoutTitle.setSpacing(50)

        self.labelName.setText(self.player.getInfo("Name"))
        self.labelTag.setText(self.player.getInfo("Tag"))

        self.pushButtonFocus.setHidden(self.hiddenFocusButton())
        self.pushButtonFocus.clicked.connect(lambda : self.addFocusPlayer())

        self.toolButtonExp.setIcon(QIcon(f"pictures/player/info/exp_icon.png"))
        self.toolButtonExp.setText(str(self.player.getInfo("Exp Level")))
        self.toolButtonTownHall.setText(str(self.player.getInfo("Town Hall")))
        self.toolButtonTownHall.setIcon(QIcon(f"pictures/player/townHall/th-{self.player.getInfo('Town Hall')}.png"))

        if self.player.getInfo("Builder Hall") < 2:
            self.toolButtonBuilderHall.setHidden(True)
        else:
            self.toolButtonBuilderHall.setText(str(self.player.getInfo("Builder Hall")))
            self.toolButtonBuilderHall.setIcon(QIcon(f"pictures/player/builderHall/bh-{self.player.getInfo('Builder Hall')}.png"))
        clan = self.player.getInfo("Clan")
        self.toolButtonClan.setText(clan)
        # 显示部落图标
        if self.player.getInfo("Clan") is None:
            self.toolButtonClan.setHidden(True)
            self.toolButtonPosition.setHidden(True)
        else:
            self.toolButtonClan.setIcon(QIcon(QPixmap(f'pictures/clan/flags/{self.player.getInfo("Clan Tag")}.png')))
            self.toolButtonPosition.setText(Items.roleDict[self.player.getInfo("Role")])

        self.toolButtonWarStar.setIcon(QIcon("pictures/player/info/war_star_icon.png"))
        self.toolButtonWarStar.setText(str(self.player.getInfo("War Stars")))

        self.toolButtonTrophies.setIcon(QIcon(f"pictures/league/{caculateLeague(self.player.getInfo('Trophies'))}.png"))
        self.toolButtonTrophies.setText(str(self.player.getInfo('Trophies')))

        if self.player.getInfo("Legend Trophies") != 0:
            self.toolButtonLegendTrophies.setIcon(QIcon("pictures/player/info/legend_trophies.png"))
            self.toolButtonLegendTrophies.setText(str(self.player.getInfo("Legend Trophies")))
        else:
            self.toolButtonLegendTrophies.setHidden(True)

        self.toolButtonBuilderTrophies.setIcon(QIcon("pictures/player/info/builder_base_icon.png"))
        self.toolButtonBuilderTrophies.setText(str(self.player.getInfo("Builder Base Trophies")))

        self.toolButtonDonations.setIcon(QIcon("pictures/player/info/donation_icon.png"))
        self.toolButtonDonations.setText(str(self.player.getInfo("Donations")))

        self.toolButtonReceived.setIcon(QIcon("pictures/player/info/received_icon.png"))
        self.toolButtonReceived.setText(str(self.player.getInfo("Received")))

        self.toolButtonAttacks.setIcon(QIcon("pictures/player/info/attack_icon.png"))
        self.toolButtonAttacks.setText(str(self.player.getInfo("Attack Wins")))

        self.toolButtonDefences.setIcon(QIcon("pictures/player/info/defence_icon.png"))
        self.toolButtonDefences.setText(str(self.player.getInfo("Defense Wins")))

        self.toolButtonCapitalGold.setIcon(QIcon("pictures/player/info/capital_gold.png"))
        self.toolButtonCapitalGold.setText(str(self.player.getInfo("Capital Gold")))

        self.toolButtonTrophiesBest.setIcon(QIcon(f"pictures/league/{caculateLeague(self.player.getInfo('Best Trophies'))}.png"))
        self.toolButtonTrophiesBest.setText(str(self.player.getInfo("Best Trophies")))
        self.toolButtonBuilderTrophiesBest.setIcon(QIcon("pictures/player/info/builder_base_icon.png"))
        self.toolButtonBuilderTrophiesBest.setText(str(self.player.getInfo("Best Builder Base Trophies")))
        self.horizontalLayoutBest.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayoutBest.setContentsMargins(0, 0, 0, 0)
        self.groupBoxBest.setContentsMargins(0, 0, 0, 0)

        # 展示英雄信息
        hboxLayoutHeroes = QHBoxLayout()
        heroes = []
        for name in Items.heroes:
            hero = self.player.getHero(name)
            if hero != 0:
                heroes.append(hero)
        if len(heroes) == 0:
            self.groupBoxHeroes.setHidden(True)
        else:
            heroButtons = [QToolButton(parent=self.groupBoxHeroes) for i in range(len(heroes))]
            for i in range(len(heroes)):
                heroButtons[i].setMaximumSize(45, 30)
                heroButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                heroButtons[i].setIconSize(QSize(20, 20))
                heroButtons[i].setIcon(QIcon(QPixmap(f"pictures/army/heroes/hero-{i}.png")))
                heroButtons[i].setText(str(heroes[i]))
                hboxLayoutHeroes.addWidget(heroButtons[i])
            hboxLayoutHeroes.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.groupBoxHeroes.setLayout(hboxLayoutHeroes)

        # 展示宠物信息
        hboxLayouPets = QHBoxLayout()
        pets = []
        names = []
        for name in Items.pets:
            pet = self.player.getPet(name)
            if pet != 0:
                pets.append(pet)
                names.append(name)
        petButtons = [QToolButton(parent=self.groupBoxPets) for i in range(len(pets))]
        if len(pets) == 0:
            self.groupBoxPets.setHidden(True)
        else:
            for i in range(len(pets)):
                petButtons[i].setMaximumSize(45, 30)
                petButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                petButtons[i].setIconSize(QSize(20, 20))
                petButtons[i].setIcon(QIcon(QPixmap(f"pictures/army/pets/pet-{i}.png")))
                petButtons[i].setText(str(pets[i]))
                hboxLayouPets.addWidget(petButtons[i])
            hboxLayouPets.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.groupBoxPets.setLayout(hboxLayouPets)

        # 展示装备信息
        heroNum = 0
        hboxLayoutAllEquipments = QHBoxLayout(self.groupBoxEquipments)
        skipEquipments = True
        for i in range(len(Items.equipments)):
            equipments = []
            for j in range(len(Items.equipments[i])):
                equipment = self.player.getEquipment(Items.equipments[i][j])
                if equipment != 0:
                    equipments.append(equipment)
            if len(equipments) > 0:
                heroNum += 1
        for i in range(len(Items.equipments)):
            equipments = []
            names = []
            print(len(Items.equipments[i]))
            for j in range(len(Items.equipments[i])):
                equipment = self.player.getEquipment(Items.equipments[i][j])
                if equipment != 0:
                    equipments.append(equipment)
                    names.append(Items.equipments[i][j])
            if len(equipments) > 0:
                groupBoxEquipment = QGroupBox(parent=self.groupBoxEquipments)
                groupBoxEquipment.setTitle(Items.heroesCN[i])
                groupBoxEquipment.setWindowIcon(QIcon(QPixmap(f"pictures/army/heroes/hero-{i}.png")))
                skipEquipments = False
                equipmentButtons, _, vboxLayoutEquipment = CreateUI.createToolButtonsVbox(12 // heroNum, len(equipments))
                for j in range(len(equipments)):
                    equipmentButtons[j].setMaximumSize(45, 30)
                    equipmentButtons[j].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                    equipmentButtons[j].setIconSize(QSize(20, 20))
                    equipmentButtons[j].setIcon(QIcon(QPixmap(f"pictures/army/equipments/{names[j]}.png")))
                    equipmentButtons[j].setText(str(equipments[j]))
                groupBoxEquipment.setLayout(vboxLayoutEquipment)
                hboxLayoutAllEquipments.addWidget(groupBoxEquipment)
                self.groupBoxEquipments.setLayout(hboxLayoutAllEquipments)
        if skipEquipments == True:
            self.groupBoxEquipments.setHidden(True)

        # 展示兵种信息
        troops = []
        names = []
        for name in Items.troops:
            troop = self.player.getTroop(name)
            if troop != 0:
                troops.append(troop)
                names.append(name)
        troopButtons, _, vboxLayoutTroops = CreateUI.createToolButtonsVbox(16, len(troops))
        for i in range(len(troops)):
            troopButtons[i].setMaximumSize(45, 30)
            troopButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
            troopButtons[i].setIconSize(QSize(20, 20))
            troopButtons[i].setIcon(QIcon(QPixmap(f"pictures/army/troops/{names[i]}.png")))
            troopButtons[i].setText(str(troops[i]))
        self.groupBoxTroops.setLayout(vboxLayoutTroops)

        # 展示法术信息
        spells = []
        names = []
        for name in Items.spells:
            spell = self.player.getSpell(name)
            if spell != 0:
                spells.append(spell)
                names.append(name)
        if len(spells) > 0:
            spellButtons, _, vboxLayoutSpells = CreateUI.createToolButtonsVbox(15, len(spells))
            for i in range(len(spells)):
                spellButtons[i].setMaximumSize(45, 30)
                spellButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                spellButtons[i].setIconSize(QSize(20, 20))
                spellButtons[i].setIcon(QIcon(QPixmap(f"pictures/army/spells/{names[i]}.png")))
                spellButtons[i].setText(str(spells[i]))
            self.groupBoxSpells.setLayout(vboxLayoutSpells)

        # 展示夜世界英雄
        hboxLayoutHeroesBuilder = QHBoxLayout()
        heroesBuilder = []
        names = []
        for name in Items.builderHeroes:
            hero = self.player.getHeroBuilder(name)
            if hero != 0:
                heroesBuilder.append(hero)
                names.append(name)
        if len(heroesBuilder) == 0:
            self.groupBoxHeroesBuilder.setHidden(True)
        else:
            heroBuilderButtons = [QToolButton(parent=self.groupBoxHeroes) for i in range(len(heroesBuilder))]
            for i in range(len(heroesBuilder)):
                heroBuilderButtons[i].setMaximumSize(45, 30)
                heroBuilderButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                heroBuilderButtons[i].setIconSize(QSize(20, 20))
                heroBuilderButtons[i].setIcon(
                    QIcon(QPixmap(f"pictures/army/builderHeroes/{names[i]}.png")))
                heroBuilderButtons[i].setText(str(heroesBuilder[i]))
                hboxLayoutHeroesBuilder.addWidget(heroBuilderButtons[i])
            hboxLayoutHeroesBuilder.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.groupBoxHeroesBuilder.setLayout(hboxLayoutHeroesBuilder)

        # 展示夜世界兵种
        troopsBuilder = []
        names = []
        for name in Items.builderTroops:
            troop = self.player.getTroopBuilder(name)
            if troop != 0:
                troopsBuilder.append(troop)
                names.append(name)
        if len(troopsBuilder) == 0:
            self.groupBoxTroopsBuilder.setHidden(True)
        else:
            troopBuilderButtons, _, vboxLayoutTroopsBuilder = CreateUI.createToolButtonsVbox(16, len(troopsBuilder))
            for i in range(len(troopsBuilder)):
                troopBuilderButtons[i].setMaximumSize(45, 30)
                troopBuilderButtons[i].setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
                troopBuilderButtons[i].setIconSize(QSize(20, 20))
                troopBuilderButtons[i].setIcon(
                    QIcon(QPixmap(f"pictures/army/builderTroops/{names[i]}.png")))
                troopBuilderButtons[i].setText(str(troopsBuilder[i]))
            self.groupBoxTroopsBuilder.setLayout(vboxLayoutTroopsBuilder)