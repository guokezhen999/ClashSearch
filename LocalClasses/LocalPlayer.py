from BasicData.Items import *
from LocalClasses import *

class LocalPlayer:
    def __init__(self):
        self.infos = {}
        self.heroes = {}
        self.troops = {}
        self.pets = {}
        self.spells = {}
        self.equipments = {}
        self.heroesBuilder = {}
        self.troopsBuilder = {}
        self.achievements = {}

    def setInfo(self, name: str, value: Any) -> None:
        self.infos[name] = value

    def setHero(self, name: str, value: Any) -> None:
        self.heroes[name] = value

    def setTroop(self, name: str, value: Any) -> None:
        self.troops[name] = value

    def setPet(self, name: str, value: Any) -> None:
        self.pets[name] = value

    def setSpell(self, name: str, value: Any) -> None:
        self.spells[name] = value

    def setEquipment(self, name: str, value: Any) -> None:
        self.equipments[name] = value

    def setHeroBuilder(self, name: str, value: Any) -> None:
        self.heroesBuilder[name] = value

    def setTroopBuilder(self, name: str, value: Any) -> None:
        self.troopsBuilder[name] = value

    def setAchievement(self, name: str, value: Any) -> None:
        self.achievements[name] = value

    def getInfo(self, name: str) -> Any:
        return self.infos[name]

    def getHero(self, name: str) -> Any:
        return self.heroes[name]

    def getTroop(self, name: str) -> Any:
        return self.troops[name]

    def getPet(self, name: str) -> Any:
        return self.pets[name]

    def getSpell(self, name: str) -> Any:
        return self.spells[name]

    def getEquipment(self, name: str) -> Any:
        return self.equipments[name]

    def getHeroBuilder(self, name: str) -> Any:
        return self.heroesBuilder[name]

    def getTroopBuilder(self, name: str) -> Any:
        return self.troopsBuilder[name]

    def getAchievement(self, name: str) -> Any:
        return self.achievements[name]

def playerToLocal(player: coc.Player) -> LocalPlayer:
    localPlayer = LocalPlayer()
    # 英雄等级
    heroLevels = []
    heroLevelsSum = 0
    for name in Items.heroes:
        if player.get_hero(name) is not None:
            heroLevels.append(player.get_hero(name).level)
            heroLevelsSum += player.get_hero(name).level
        else:
            heroLevels.append(0)

    # 兵种等级
    troopLevels = []
    for name in Items.troops:
        if player.get_troop(name, True) is not None:
            troopLevels.append(player.get_troop(name, True).level)
        else:
            troopLevels.append(0)

    # 法术等级
    spellLevels = []
    for name in Items.spells:
        if player.get_spell(name) is not None:
            spellLevels.append(player.get_spell(name).level)
        else:
            spellLevels.append(0)

    # 宠物等级
    petLevels = []
    for name in Items.pets:
        if player.get_pet(name) is not None:
            petLevels.append(player.get_pet(name).level)
        else:
            petLevels.append(0)

    # 装备等级
    equipmentLevels = []
    for name in Items.equipments1d:
        if player.get_equipment(name) is not None:
            equipmentLevels.append(player.get_equipment(name).level)
        else:
            equipmentLevels.append(0)

    # 夜世界英雄等级
    builderHeroLevels = []
    builderHeroLevelsSum = 0
    for name in Items.builderHeroes:
        if player.get_hero(name) is not None:
            builderHeroLevels.append(player.get_hero(name).level)
            builderHeroLevelsSum += player.get_hero(name).level
        else:
            builderHeroLevels.append(0)

    # 夜世界兵种等级
    builderTroopLevels = []
    for name in Items.builderTroops:
        if name == "Baby Dragon Builder":
            name = "Baby Dragon"
        if player.get_troop(name, False) is not None:
            builderTroopLevels.append(player.get_troop(name).level)
        else:
            builderTroopLevels.append(0)

    # 成就
    achievementValues = []
    for achievementName in Items.playerAchievementsDict.keys():
        if player.get_achievement(achievementName) is not None:
            achievementValues.append(player.get_achievement(achievementName).value)
        else:
            achievementValues.append(0)

    if player.clan is not None:
        clan = player.clan.name
        clanTag = player.clan.tag
        role = player.role.name
    else:
        role = None
        clan = None
        clanTag = None
    if player.legend_statistics is not None:
        lengendTrophies = player.legend_statistics.legend_trophies
    else:
        lengendTrophies = 0
    if player.town_hall_weapon is not None:
        weapon = player.town_hall_weapon
    else:
        weapon = 0

    infoValues = [
        player.name, player.tag, player.exp_level, player.town_hall, weapon, player.builder_hall,
        clan, clanTag, role, player.war_stars, player.trophies, player.best_trophies,
        lengendTrophies,
        player.builder_base_trophies, player.best_builder_base_trophies, player.donations, player.received,
        player.attack_wins, player.defense_wins, player.get_achievement("Most Valuable Clanmate").value,
        heroLevelsSum, builderHeroLevelsSum
    ]

    for i, value in enumerate(infoValues):
        localPlayer.setInfo(Items.playerInfos[i], value)
    for i, value in enumerate(heroLevels):
        localPlayer.setHero(Items.heroes[i], value)
    for i, value in enumerate(troopLevels):
        localPlayer.setTroop(Items.troops[i], value)
    for i, value in enumerate(spellLevels):
        localPlayer.setSpell(Items.spells[i], value)
    for i, value in enumerate(petLevels):
        localPlayer.setPet(Items.pets[i], value)
    for i, value in enumerate(equipmentLevels):
        localPlayer.setEquipment(Items.equipments1d[i], value)
    for i, value in enumerate(builderHeroLevels):
        localPlayer.setHeroBuilder(Items.builderHeroes[i], value)
    for i, value in enumerate(builderTroopLevels):
        localPlayer.setTroopBuilder(Items.builderTroops[i], value)
    keys = list(Items.playerAchievementsDict.keys())
    for i, value in enumerate(achievementValues):
        localPlayer.setAchievement(keys[i], value)
    print(localPlayer.achievements, localPlayer.pets)
    return localPlayer

def playersToLocal(players: list[coc.Player]) -> list[LocalPlayer]:
    localPlayers = []
    for player in players:
        localPlayer = playerToLocal(player)
        localPlayers.append(localPlayer)
    return localPlayers


