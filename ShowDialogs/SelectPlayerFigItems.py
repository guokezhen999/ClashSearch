from ShowDialogs import *

from UI.SelectPlayerItemsDialog import Ui_SelectPlayItemsDialog
from MakeFigs.MakePlayerFigs import MakePlayerFigs
from BasicData.SelectMode import PlayerType
from BasicData.Items import Items
from Utils.CreateUI import CreateUI
from ShowForms.ShowFiguresForm import ShowFiguresForm

class SelectPlayerFigItems(QDialog, Ui_SelectPlayItemsDialog):
    def __init__(self, figMaker: MakePlayerFigs, playerType: PlayerType):
        super().__init__()
        self.setupUi(self)
        self.figMaker = figMaker
        self.playerType = playerType
        self.showSelectPlayerItems()

    def showSelectPlayerItems(self):
        self.pushButtonCommit.clicked.connect(self.commit)
        # 基本信息
        infoVboxAll = QVBoxLayout(self.groupBoxInfo)
        self.infos = [info for info in Items.playerFigInfos]
        self.infoCheckBoxes, _, infoVbox = CreateUI.createCheckboxesVbox(8, len(self.infos))
        for i, name in enumerate(self.infos):
            self.infoCheckBoxes[i].setText(Items.playerInfosDict[name])
        infoVboxAll.addLayout(infoVbox)
        hLayoutInfoButton, pushButtonInfo1, pushButtonInfo2 = CreateUI.createSelectButton()
        infoVbox.addLayout(hLayoutInfoButton)
        self.groupBoxInfo.setLayout(infoVbox)
        pushButtonInfo1.clicked.connect(lambda: self.selectAll(self.infoCheckBoxes))
        pushButtonInfo2.clicked.connect(lambda: self.disSelectAll(self.infoCheckBoxes))

        # 英雄
        self.heroCheckBoxes, _, heroVbox = CreateUI.createCheckboxesVbox(12, len(Items.heroes))
        heroVboxAll = QVBoxLayout(self.groupBoxHero)
        for i, name in enumerate(Items.heroes):
            self.heroCheckBoxes[i].setIconSize(QSize(25, 25))
            self.heroCheckBoxes[i].setIcon(QIcon(f"pictures/army/heroes/hero-{i}.png"))

        heroVboxAll.addLayout(heroVbox)
        hLayoutHeroButton, pushButtonHero1, pushButtonHero2 = CreateUI.createSelectButton()
        heroVbox.addLayout(hLayoutHeroButton)
        self.groupBoxHero.setLayout(heroVbox)
        pushButtonHero1.clicked.connect(lambda: self.selectAll(self.heroCheckBoxes))
        pushButtonHero2.clicked.connect(lambda: self.disSelectAll(self.heroCheckBoxes))

        # 兵种
        self.troopCheckBoxes, _, troopVbox = CreateUI.createCheckboxesVbox(12, len(Items.troops))
        troopVboxAll = QVBoxLayout(self.groupBoxTroop)
        for i, name in enumerate(Items.troops):
            self.troopCheckBoxes[i].setIconSize(QSize(25, 25))
            self.troopCheckBoxes[i].setIcon(QIcon(f"pictures/army/troops/{name}.png"))

        troopVboxAll.addLayout(troopVbox)
        hLayoutTroopButton, pushButtonTroop1, pushButtonTroop2 = CreateUI.createSelectButton()
        troopVbox.addLayout(hLayoutTroopButton)
        self.groupBoxTroop.setLayout(troopVbox)
        pushButtonTroop1.clicked.connect(lambda: self.selectAll(self.troopCheckBoxes))
        pushButtonTroop2.clicked.connect(lambda: self.disSelectAll(self.troopCheckBoxes))

        # 法术
        self.spellCheckBoxes, _, spellVbox = CreateUI.createCheckboxesVbox(12, len(Items.spells))
        spellVboxAll = QVBoxLayout(self.groupBoxSpell)
        for i, name in enumerate(Items.spells):
            self.spellCheckBoxes[i].setIconSize(QSize(25, 25))
            self.spellCheckBoxes[i].setIcon(QIcon(f"pictures/army/spells/{name}.png"))

        spellVboxAll.addLayout(spellVbox)
        hLayoutSpellButton, pushButtonSpell1, pushButtonSpell2 = CreateUI.createSelectButton()
        spellVbox.addLayout(hLayoutSpellButton)
        self.groupBoxSpell.setLayout(spellVbox)
        pushButtonSpell1.clicked.connect(lambda: self.selectAll(self.spellCheckBoxes))
        pushButtonSpell2.clicked.connect(lambda: self.disSelectAll(self.spellCheckBoxes))

        # 宠物
        self.petCheckBoxes, _, petVbox = CreateUI.createCheckboxesVbox(12, len(Items.pets))
        petVboxAll = QVBoxLayout(self.groupBoxPet)
        for i, name in enumerate(Items.pets):
            self.petCheckBoxes[i].setIconSize(QSize(25, 25))
            self.petCheckBoxes[i].setIcon(QIcon(f"pictures/army/pets/pet-{i}.png"))

        petVboxAll.addLayout(petVbox)
        hLayoutPetButton, pushButtonPet1, pushButtonPet2 = CreateUI.createSelectButton()
        petVbox.addLayout(hLayoutPetButton)
        self.groupBoxPet.setLayout(petVbox)
        pushButtonPet1.clicked.connect(lambda: self.selectAll(self.petCheckBoxes))
        pushButtonPet2.clicked.connect(lambda: self.disSelectAll(self.petCheckBoxes))

        # 装备
        self.equipmentCheckBoxes, _, equipmentVbox = CreateUI.createCheckboxesVbox(12, len(Items.equipments1d))
        equipmentVboxAll = QVBoxLayout(self.groupBoxEquipment)
        for i, name in enumerate(Items.equipments1d):
            self.equipmentCheckBoxes[i].setIconSize(QSize(25, 25))
            self.equipmentCheckBoxes[i].setIcon(QIcon(f"pictures/army/equipments/{name}.png"))

        equipmentVboxAll.addLayout(equipmentVbox)
        hLayoutEquipmentButton, pushButtonEquipment1, pushButtonEquipment2 = CreateUI.createSelectButton()
        equipmentVbox.addLayout(hLayoutEquipmentButton)
        self.groupBoxEquipment.setLayout(equipmentVbox)
        pushButtonEquipment1.clicked.connect(lambda: self.selectAll(self.equipmentCheckBoxes))
        pushButtonEquipment2.clicked.connect(lambda: self.disSelectAll(self.equipmentCheckBoxes))

        # 夜世界
        builderNames = Items.builderHeroes + Items.builderTroops
        self.builderCheckBoxes, _, builderVbox = CreateUI.createCheckboxesVbox(12, len(builderNames))
        builderVboxAll = QVBoxLayout(self.groupBoxBuilder)
        for i, name in enumerate(Items.builderHeroes):
            self.builderCheckBoxes[i].setIconSize(QSize(25, 25))
            self.builderCheckBoxes[i].setIcon(QIcon(f"pictures/army/builderHeroes/{name}.png"))
        index = len(Items.builderHeroes)
        for i, name in enumerate(Items.builderTroops):
            self.builderCheckBoxes[i + index].setIconSize(QSize(25, 25))
            self.builderCheckBoxes[i + index].setIcon(QIcon(f"pictures/army/builderTroops/{name}.png"))

        builderVboxAll.addLayout(builderVbox)
        hLayoutBuilderButton, pushButtonBuilder1, pushButtonBuilder2 = CreateUI.createSelectButton()
        pushButtonBuilder1.clicked.connect(lambda : self.selectAll(self.builderCheckBoxes))
        pushButtonBuilder2.clicked.connect(lambda : self.disSelectAll(self.builderCheckBoxes))
        builderVbox.addLayout(hLayoutBuilderButton)
        self.groupBoxBuilder.setLayout(builderVbox)

        # 成就
        achievements = list(Items.playerAchievementsDict.keys())
        self.achivementCheckBoxes, _, achivementVbox = CreateUI.createCheckboxesVbox(12, len(achievements))
        achivementVboxAll = QVBoxLayout(self.groupBoxAchievements)
        for i, name in enumerate(achievements):
            self.achivementCheckBoxes[i].setText(Items.playerAchievementsDict[name])
        achivementVboxAll.addLayout(achivementVbox)
        hLayoutAchivementButton, pushButtonAchivement1, pushButtonAchivement2 = CreateUI.createSelectButton()
        achivementVbox.addLayout(hLayoutAchivementButton)
        self.groupBoxAchievements.setLayout(achivementVbox)
        pushButtonAchivement1.clicked.connect(lambda: self.selectAll(self.achivementCheckBoxes))
        pushButtonAchivement2.clicked.connect(lambda: self.disSelectAll(self.achivementCheckBoxes))

    def selectAll(self, checkboxes: list[QCheckBox]) -> None:
        for button in checkboxes:
            if button.text() != Items.playerInfosDict["Name"]:
                button.setChecked(True)

    def disSelectAll(self, checkboxes: list[QCheckBox]) -> None:
        for button in checkboxes:
            if button.text() != Items.playerInfosDict["Name"]:
                button.setChecked(False)

    def commit(self):
        self.figMaker.infos = []
        for button in self.infoCheckBoxes:
            if button.isChecked():
                self.figMaker.infos.append(Items.playerInfosDictInv[button.text()])
        for i, button in enumerate(self.heroCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(Items.heroes[i])
        for i, button in enumerate(self.troopCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(Items.troops[i])
        for i, button in enumerate(self.spellCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(Items.spells[i])
        for i, button in enumerate(self.petCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(Items.pets[i])
        for i, button in enumerate(self.equipmentCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(Items.equipments1d[i])
        for i, button in enumerate(self.builderCheckBoxes[:len(Items.builderHeroes)]):
            if button.isChecked():
                self.figMaker.infos.append(Items.builderHeroes[i])
        for i, button in enumerate(self.builderCheckBoxes[len(Items.builderHeroes):]):
            if button.isChecked():
                self.figMaker.infos.append(Items.builderTroops[i])
        achievements = list(Items.playerAchievementsDict.keys())
        for i, button in enumerate(self.achivementCheckBoxes):
            if button.isChecked():
                self.figMaker.infos.append(achievements[i])
        self.sender().parent().close()
        filePaths = self.figMaker.makeFig()
        showFigureForm = ShowFiguresForm(filePaths)
        showFigureForm.exec()


