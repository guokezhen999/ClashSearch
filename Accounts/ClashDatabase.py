import datetime

from BasicData.AccountInfo import DatabaseInfo
from BasicData.Items import Items
from BasicData.SelectMode import PlayerType
from Accounts import *
from LocalClasses.LocalPlayer import LocalPlayer, playersToLocal
from LocalClasses.LocalClan import LocalClan, clansToLocal
from LocalClasses.LocalWarLog import LocalWarLog, warLogsToLocal

class ClashDatabase(DatabaseInfo):
    def __init__(self):
        super().__init__()
        self.login()

    def getPlayerTable(self, type: PlayerType) -> str:
        if type == PlayerType.MY_PLAYER:
            table = self.myPlayers
        elif type == PlayerType.FOCUS_PLAYER:
            table = self.focusPlayers
        elif type == PlayerType.ROBOT:
            table = self.robots
        elif type == PlayerType.CLAN_PLAYER:
            table = self.clanPlayers
        else:
            table = ""
        return table

    def downLoadClanFlags(self, urls: dict[str, str], file: str):
        oldUrls = {}
        with open(f'Accounts/databaseFiles/{file}', 'r') as f:
            lines = f.readlines()
            for line in lines:
                clan, url = line.split('=')
                oldUrls[clan] = url.replace('\n', '')
        newClans = urls.keys()
        oldClans = oldUrls.keys()
        # 保存图片
        for clan in newClans:
            if clan not in oldClans or (clan in oldClans and oldUrls[clan] != urls[clan]):
                url = urls[clan]
                try:
                    image = requests.get(url)
                    with open(f"pictures/clan/flags/{clan}.png", 'wb') as f:
                        f.write(image.content)
                    print(f"{clan}图片保存成功")
                except Exception as _:
                    print(f"{clan}图片保存失败")
                    urls.pop(clan)
        with open(f'Accounts/databaseFiles/{file}', 'w') as fp:
            for clan in urls.keys():
                url = urls[clan]
                fp.write(f"{clan}={url}\n")



    def login(self) -> None:
        self.connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username,
            database=self.database, password=self.password, charset=self.charset
        )
        self.cursor = self.connection.cursor()

    def addPlayer(self, playerDict: dict[str, object], type: PlayerType) -> None:
        keys = playerDict.keys()
        values = []
        sqlKeys = ""
        for key in keys:
            sqlKeys += f"{key}, "
            values.append(playerDict[key])
        sqlKeys = sqlKeys[:-2]
        sqlValues = ""
        for _ in values:
            sqlValues += "%s, "
        sqlValues = sqlValues[:-2]
        table = self.getPlayerTable(type)
        sql = f"INSERT INTO {table} ({sqlKeys}) VALUES ({sqlValues})"
        self.cursor.execute(sql, values)
        self.connection.commit()

    def addClan(self, tag: str) -> None:
        sql = f"INSERT INTO {self.clans}(tag) VALUES('{tag}')"
        self.cursor.execute(sql)
        self.connection.commit()

    def editPlayer(self, playerDict:dict, type: PlayerType) -> None:
        keys = playerDict.keys()
        values = []
        sqlKeys = ""
        for key in keys:
            if key != "initTag":
                sqlKeys += f"{key} = %s, "
                values.append(playerDict[key])
        sqlKeys = sqlKeys[:-2]
        values.append(playerDict["initTag"])
        table = self.getPlayerTable(type)
        sql = f"UPDATE {table} SET {sqlKeys} WHERE tag = %s"
        self.cursor.execute(sql, values)
        self.connection.commit()

    def getPlayersAll(self, flag: PlayerType) -> list[LocalPlayer] :
        infoSql = ""
        if flag == PlayerType.MY_PLAYER:
            infos = Items.playerInfos.copy()
        else:
            infos = Items.playerInfos[:-2]
        table = self.getPlayerTable(flag)
        for info in infos:
            infoSql += f"{info.lower().replace(' ', '_')}, "
        armySql = ""
        armies = Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d + Items.builderHeroes \
                 + Items.builderTroops
        for name in armies:
            armySql += f"{name.lower().replace(' ', '_').replace('.', '')}, "
        achievementsSql = ""
        for key in Items.playerAchievementsDict.keys():
            achievementsSql += f"{key.lower().replace(' ', '_').replace('!', '').replace('-', '_')}, "
        achievementsSql = achievementsSql[:-2]
        sql = f"SELECT {infoSql} {armySql} {achievementsSql} FROM {table} ORDER BY id ASC"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        players = []
        for data in results:
            data = list(data)
            player = LocalPlayer()
            for index, name in enumerate(infos):
                player.setInfo(name, data[index])
            startIndex = len(infos)
            for index, name in enumerate(Items.heroes):
                player.setHero(name, data[index + startIndex])
            startIndex += len(Items.heroes)
            for index, name in enumerate(Items.troops):
                player.setTroop(name, data[index + startIndex])
            startIndex += len(Items.troops)
            for index, name in enumerate(Items.spells):
                player.setSpell(name, data[index + startIndex])
            startIndex += len(Items.spells)
            for index, name in enumerate(Items.pets):
                player.setPet(name, data[index + startIndex])
            startIndex += len(Items.pets)
            for index, name in enumerate(Items.equipments1d):
                player.setEquipment(name, data[index + startIndex])
            startIndex += len(Items.equipments1d)
            for index, name in enumerate(Items.builderHeroes):
                if index == 1 and data[index + startIndex] == 1:
                    data[index + startIndex] = 16
                player.setHeroBuilder(name, data[index + startIndex])
            startIndex += len(Items.builderHeroes)
            for index, name in enumerate(Items.builderTroops):
                player.setTroopBuilder(name, data[index + startIndex])
            startIndex += len(Items.builderTroops)
            for index, name in enumerate(Items.playerAchievementsDict.keys()):
                player.setAchievement(name, data[index + startIndex])
            players.append(player)
        return players

    def getPlayersByClanTag(self, clanTag: str) -> list[LocalPlayer]:
        infoSql = ""
        infos = Items.playerInfos[:-2]
        for info in infos:
            infoSql += f"{info.lower().replace(' ', '_')}, "
        armySql = ""
        armies = Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d + Items.builderHeroes \
                 + Items.builderTroops
        for name in armies:
            armySql += f"{name.lower().replace(' ', '_').replace('.', '')}, "
        achievementsSql = ""
        for key in Items.playerAchievementsDict.keys():
            achievementsSql += f"{key.lower().replace(' ', '_').replace('!', '').replace('-', '_')}, "
        achievementsSql = achievementsSql[:-2]
        sql = f"SELECT {infoSql} {armySql} {achievementsSql} FROM {self.clanPlayers} WHERE clan_tag = '{clanTag}' ORDER BY id ASC"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        players = []
        for data in results:
            data = list(data)
            player = LocalPlayer()
            for index, name in enumerate(infos):
                player.setInfo(name, data[index])
            startIndex = len(infos)
            for index, name in enumerate(Items.heroes):
                player.setHero(name, data[index + startIndex])
            startIndex += len(Items.heroes)
            for index, name in enumerate(Items.troops):
                player.setTroop(name, data[index + startIndex])
            startIndex += len(Items.troops)
            for index, name in enumerate(Items.spells):
                player.setSpell(name, data[index + startIndex])
            startIndex += len(Items.spells)
            for index, name in enumerate(Items.pets):
                player.setPet(name, data[index + startIndex])
            startIndex += len(Items.pets)
            for index, name in enumerate(Items.equipments1d):
                player.setEquipment(name, data[index + startIndex])
            startIndex += len(Items.equipments1d)
            for index, name in enumerate(Items.builderHeroes):
                if index == 1 and data[index + startIndex] == 1:
                    data[index + startIndex] = 16
                player.setHeroBuilder(name, data[index + startIndex])
            startIndex += len(Items.builderHeroes)
            for index, name in enumerate(Items.builderTroops):
                player.setTroopBuilder(name, data[index + startIndex])
            startIndex += len(Items.builderTroops)
            for index, name in enumerate(Items.playerAchievementsDict.keys()):
                player.setAchievement(name, data[index + startIndex])
            players.append(player)
        return players

    def updatePlayers(self, players: list[coc.Player], flag: PlayerType) -> None:
        infoSql = ""
        for info in Items.playerInfos:
            if info not in ["Tag", "Email", "Bind Date"]:
                infoSql += f"{info.lower().replace(' ', '_')} = %s, "
        armySql = ""
        armies = Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d + Items.builderHeroes \
                 + Items.builderTroops
        for name in armies:
            armySql += f"{name.lower().replace(' ', '_').replace('.', '')} = %s, "
        achievementSql = ""
        achievementNames = Items.playerAchievementsDict.keys()
        for name in achievementNames:
            achievementSql += f"{name.lower().replace(' ', '_').replace('!', '').replace('-', '_')} = %s, "
        achievementSql = achievementSql[:-2]
        table = self.getPlayerTable(flag)
        sql = f"UPDATE {table} SET {infoSql} {armySql} {achievementSql} WHERE tag = %s"
        urls = {}
        for player in players:
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
                    if name == "Battle Copter" and player.get_hero(name).level == 1:
                        builderHeroLevels.append(15)
                    else:
                        builderHeroLevels.append(player.get_hero(name).level)
                    builderHeroLevelsSum += player.get_hero(name).level
                    if name == "Battle Copter" and player.get_hero(name).level == 1:
                        builderHeroLevelsSum += 14
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

            if player.clan is not None:
                clan = player.clan.name
                clanTag = player.clan.tag
                urls[clanTag] = player.clan.badge.url
                role = player.role.name
            else:
                clan = None
                clanTag = None
                role = None
            if player.legend_statistics is not None:
                lengendTrophies = player.legend_statistics.legend_trophies
            else:
                lengendTrophies = 0
            if player.town_hall_weapon is not None:
                weapon = player.town_hall_weapon
            else:
                weapon = 0

            # 成就
            achievementValues = []
            for name in achievementNames:
                if player.get_achievement(name) is not None:
                    achievementValues.append(player.get_achievement(name).value)
                else:
                    achievementValues.append(0)

            infoValues = [
                player.name, player.exp_level, player.town_hall, weapon, player.builder_hall,
                clan, clanTag, role, player.war_stars, player.trophies, player.best_trophies, lengendTrophies,
                player.builder_base_trophies, player.best_builder_base_trophies, player.donations, player.received,
                player.attack_wins, player.defense_wins, player.get_achievement("Most Valuable Clanmate").value,
                heroLevelsSum, builderHeroLevelsSum
            ]
            values = infoValues + heroLevels + troopLevels + spellLevels + petLevels + equipmentLevels \
                     + builderHeroLevels + builderTroopLevels + achievementValues + [player.tag]
            self.cursor.execute(sql, values)
        self.connection.commit()
        # 保存部落图标
        print(urls)
        self.downLoadClanFlags(urls, f'newestClanTag_{table}.txt')
        # 删除脚本
        # if flag == PlayerType.ROBOT:
        #     tags = [player.tag for player in players]
        #     localPlayers = self.getPlayersAll(flag)
        #     localTags = [player.getInfo('Tag') for player in localPlayers]
        #     for tag in localTags:
        #         if tag not in tags:
        #             self.cursor.execute(f"DELETE FROM {table} WHERE tag = %s", tag)
        #     self.connection.commit()


    def updateClanPlayers(self, players: list[coc.Player]):
        # 清空数据库
        achievementNames = list(Items.playerAchievementsDict.keys())
        self.cursor.execute(f"DELETE FROM {self.clanPlayers}")
        self.connection.commit()
        itemSql = "("
        infos = [info for info in Items.playerInfos if info not in ["Email", "Bind Date"]]
        allInfos = [info for info in Items.playerInfos if info not in ["Email", "Bind Date"]]
        allInfos = allInfos + Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d + \
                   Items.builderHeroes + Items.builderTroops + achievementNames
        for name in allInfos:
            itemSql += f"{name.lower().replace(' ', '_').replace('.','').replace('!', '').replace('-', '_')}, "
        itemSql = itemSql[:-2] + ")"
        players = playersToLocal(players)
        dupliacateSql = ""
        dupliacateInfos = [info for info in allInfos if info not in ["Tag"]]
        for info in dupliacateInfos:
            if info != "Tag":
                dupliacateSql += f"{info.replace(' ', '_').lower().replace('.','').replace('!', '').replace('-', '_')}=" \
                                 f"values({info.replace(' ', '_').replace('.','').lower().replace('!', '').replace('-', '_')}), "
        dupliacateSql = dupliacateSql[:-2]
        valueSql = "VALUES("
        for i in range(len(allInfos)):
            valueSql += "%s, "
        valueSql = valueSql[:-2]
        valueSql += ")"
        sql = f"INSERT INTO {self.clanPlayers} {itemSql} {valueSql} ON DUPLICATE KEY UPDATE {dupliacateSql}"
        for player in players:
            values = []
            for name in infos:
                values.append(player.getInfo(name))
            for name in Items.heroes:
                values.append(player.getHero(name))
            for name in Items.troops:
                values.append(player.getTroop(name))
            for name in Items.spells:
                values.append(player.getSpell(name))
            for name in Items.pets:
                values.append(player.getPet(name))
            for name in Items.equipments1d:
                values.append(player.getEquipment(name))
            for name in Items.builderHeroes:
                values.append(player.getHeroBuilder(name))
            for name in Items.builderTroops:
                values.append(player.getTroopBuilder(name))
            for name in achievementNames:
                values.append(player.getAchievement(name))
            self.cursor.execute(sql, values)
        self.connection.commit()

    def updateClans(self, clans: list[coc.Clan]):
        infoSql = ""
        for info in Items.clanInfos:
            if info not in ["Tag"]:
                infoSql += f"{info.lower().replace(' ', '_')} = %s, "
        infoSql = infoSql[:-2]
        sql = f"UPDATE {self.clans} SET {infoSql} WHERE tag = %s"
        urls = {}
        for clan in clans:
            urls[clan.tag] = clan.badge.url
            warLeague = clan.war_league.name if clan.war_league is not None else None
            if len(clan.capital_districts) > 0:
                capitalPeak = clan.capital_districts[0].hall_level
            else:
                capitalPeak = 0
            if clan.location is not None:
                location = clan.location.name
            else:
                location = ""
            values = [
                clan.name, clan.level, clan.member_count, warLeague, clan.points, clan.builder_base_points,
                capitalPeak, clan.capital_points, clan.war_frequency, clan.war_win_streak, clan.war_wins,
                clan.war_losses, clan.war_ties, location, clan.type, clan.required_trophies,
                clan.required_builder_base_trophies, clan.required_townhall, clan.public_war_log, clan.description,
                clan.tag
            ]
            self.cursor.execute(sql, values)
        self.connection.commit()
        self.downLoadClanFlags(urls, "newestClanTag_clans.txt")

    def getClansAll(self) -> list[LocalClan]:
        infoSql = ""
        for info in Items.clanInfos:
            infoSql += f"{info.lower().replace(' ', '_')}, "
        infoSql = infoSql[:-2]
        sql = f"SELECT {infoSql} FROM {self.clans} ORDER BY id ASC"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        clans = []
        for data in results:
            clan = LocalClan()
            for index, name in enumerate(Items.clanInfos):
                clan.setInfo(name, data[index])
            clans.append(clan)
        return clans

    def addRobots(self, tags: list[str]):
        num = 0
        for tag in tags:
            sql = f"INSERT IGNORE INTO {self.robots}(tag) VALUES('{tag}')"
            num += self.cursor.execute(sql)
        self.connection.commit()
        return num

    def createPlayerDailyTable(self, playerType: PlayerType):
        date = datetime.datetime.now().date()
        strDate = date.strftime('%Y_%m_%d')
        file = 'Accounts/databaseFiles/playerInfos.txt'
        table = f'{self.getPlayerTable(playerType)}_{strDate}'
        sql = f"CREATE TABLE IF NOT EXISTS {table} ("
        lineInfo = ""
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                lineInfo += line.replace('\n', ', ')
        sql += lineInfo
        sql += ', '
        itemList = Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d \
                   + Items.builderHeroes + Items.builderTroops
        for name in itemList:
            name = name.replace(' ', '_').replace('.', '').lower()
            sql += f" {name} INT UNSIGNED, "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)
        self.connection.commit()

    def createClanDailyTable(self):
        date = datetime.datetime.now().date()
        strDate = date.strftime('%Y_%m_%d')
        file = 'Accounts/databaseFiles/clanInfos.txt'
        table = f'{self.clans}_{strDate}'
        sql = f"CREATE TABLE IF NOT EXISTS {table} ("
        lineInfo = ""
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                lineInfo += line.replace('\n', ', ')
        sql += lineInfo
        sql += ', '
        itemList = Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d \
                   + Items.builderHeroes + Items.builderTroops
        for name in itemList:
            name = name.replace(' ', '_').replace('.', '').lower()
            sql += f" {name} SMALLINT UNSIGNED, "
        sql = sql[:-2] + ")"
        self.cursor.execute(sql)
        self.connection.commit()

    def updatePlayerDailyTable(self, players: list[coc.Player], playerType: PlayerType):
        itemSql = "("
        date = datetime.datetime.now().date()
        strDate = date.strftime('%Y_%m_%d')
        table = f'{self.getPlayerTable(playerType)}_{strDate}'
        infos = [info for info in Items.playerInfos if info not in ["Email", "Bind Date"]]
        allInfos = [info for info in Items.playerInfos if info not in ["Email", "Bind Date"]]
        achievements = list(Items.playerAchievementsDict.keys())
        allInfos = allInfos + Items.heroes + Items.troops + Items.spells + Items.pets + Items.equipments1d + \
                   Items.builderHeroes + Items.builderTroops + achievements
        for name in allInfos:
            itemSql += f"{name.lower().replace(' ', '_').replace('.', '').replace('-', '_').replace('!', '')}, "
        itemSql = itemSql[:-2] + ")"
        players = playersToLocal(players)
        dupliacateSql = ""
        dupliacateInfos = [info for info in allInfos if info not in ["Tag"]]
        for info in dupliacateInfos:
            if info != "Tag":
                dupliacateSql += f"{info.replace(' ', '_').lower().replace('.', '').replace('-', '_').replace('!', '')}=" \
                                 f"values({info.replace(' ', '_').replace('.', '').replace('-', '_').replace('!', '').lower()}), "
        dupliacateSql = dupliacateSql[:-2]
        valueSql = "VALUES("
        for i in range(len(allInfos)):
            valueSql += "%s, "
        valueSql = valueSql[:-2]
        valueSql += ")"
        sql = f"INSERT INTO {table} {itemSql} {valueSql} ON DUPLICATE KEY UPDATE {dupliacateSql}"
        for player in players:
            values = []
            for name in infos:
                values.append(player.getInfo(name))
            for name in Items.heroes:
                values.append(player.getHero(name))
            for name in Items.troops:
                values.append(player.getTroop(name))
            for name in Items.spells:
                values.append(player.getSpell(name))
            for name in Items.pets:
                values.append(player.getPet(name))
            for name in Items.equipments1d:
                values.append(player.getEquipment(name))
            for name in Items.builderHeroes:
                values.append(player.getHeroBuilder(name))
            for name in Items.builderTroops:
                values.append(player.getTroopBuilder(name))
            for name in achievements:
                values.append(player.getAchievement(name))
            self.cursor.execute(sql, values)
        self.connection.commit()

    def updateClanDailyTable(self, clans: list[coc.Clan]):
        itemSql = "("
        date = datetime.datetime.now().date()
        strDate = date.strftime('%Y_%m_%d')
        table = f'{self.clans}_{strDate}'
        infos = [info for info in Items.clanInfos]
        for name in infos:
            itemSql += f"{name.lower().replace(' ', '_').replace('.', '')}, "
        itemSql = itemSql[:-2] + ")"
        players = clansToLocal(clans)
        dupliacateSql = ""
        dupliacateInfos = [info for info in infos if info not in ["Tag"]]
        for info in dupliacateInfos:
            dupliacateSql += f"{info.replace(' ', '_').lower().replace('.', '')}=" \
                             f"values({info.replace(' ', '_').replace('.', '').lower()}), "
        dupliacateSql = dupliacateSql[:-2]
        valueSql = "VALUES("
        for i in range(len(infos)):
            valueSql += "%s, "
        valueSql = valueSql[:-2]
        valueSql += ")"
        sql = f"INSERT INTO {table} {itemSql} {valueSql} ON DUPLICATE KEY UPDATE {dupliacateSql}"
        for player in players:
            values = []
            for name in infos:
                values.append(player.getInfo(name))
            self.cursor.execute(sql, values)
        self.connection.commit()

    def deletePlayer(self, tag: str, playerType: PlayerType):
        table = self.getPlayerTable(playerType)
        sql = f"DELETE FROM {table} WHERE tag = %s"
        print(sql, tag)
        self.cursor.execute(sql, tag)
        self.connection.commit()

    def getPlayerInfoTrack(self, playerType: PlayerType, tags: list[str], infos: list[str]) -> dict[str, list[list]]:
        startDate = self.startDate
        endDate = datetime.datetime.now().date()
        delta = datetime.timedelta(days=1)
        basicTable = self.getPlayerTable(playerType)
        dates = []
        tables = []
        for date in range(int((endDate - startDate).days) + 1):
            currentDate = startDate + delta * date
            dateStr = currentDate.strftime('%Y_%m_%d')
            table = f'{basicTable}_{dateStr}'
            # 检验表是否存在
            sql = 'SHOW TABLES LIKE %s'
            if self.cursor.execute(sql, table) == 1:
                tables.append(table)
                dates.append(currentDate)
        infos = [info.lower().replace('.', '').replace(' ', '_') for info in infos]
        infoSql = ""
        for info in infos:
            infoSql += f"{info}, "
        infoSql = infoSql[:-2]
        resultDict = {}
        for tag in tags:
            infoList = []
            for date, table in zip(dates, tables):
                sql = f"SELECT {infoSql} FROM {table} WHERE tag = %s"
                if self.cursor.execute(sql, tag) == 1:
                    results = self.cursor.fetchall()
                    infoList.append([date] + list(results[0]))
                    print(results, infoList)
            resultDict[tag] = infoList
        return resultDict

    def updateWarLog(self, warLogs: dict[str, list[LocalWarLog]]):
        clanTags = warLogs.keys()
        itemSql = "("
        for name in Items.warLogInfos:
            itemSql += f"{name.lower().replace(' ', '_')}, "
        itemSql = itemSql[:-2] + ")"
        valueSql = "VALUES("
        for i in range(len(Items.warLogInfos)):
            valueSql += "%s, "
        valueSql = valueSql[:-2]
        valueSql += ")"
        dupliacateSql = ""
        dupliacateInfos = [info for info in Items.warLogInfos if info not in ["Tag", "End Time"]]
        for info in dupliacateInfos:
            dupliacateSql += f"{info.replace(' ', '_').lower()}=" \
                             f"values({info.replace(' ', '_').replace('.', '').lower()}), "
        dupliacateSql = dupliacateSql[:-2]
        sql = f"INSERT INTO {self.warLog} {itemSql} {valueSql} ON DUPLICATE KEY UPDATE {dupliacateSql}"
        for clanTag in clanTags:
            logs = warLogs[clanTag]
            for log in logs:
                values = []
                for info in Items.warLogInfos:
                    values.append(log.getInfo(info))
                self.cursor.execute(sql, values)
        self.connection.commit()

    def getWarLogs(self, tag: str) -> list[LocalWarLog]:
        logs = []
        itemSql = ""
        infos = [info for info in Items.warLogInfos if info not in ["Tag"]]
        for name in infos:
            itemSql += f"{name.lower().replace(' ', '_')}, "
        itemSql = itemSql[:-2]
        sql = f"SELECT {itemSql} FROM {self.warLog} WHERE tag = %s"
        self.cursor.execute(sql, tag)
        results = self.cursor.fetchall()
        for data in results:
            log = LocalWarLog()
            for i, info in enumerate(infos):
                log.setInfo(info, data[i])
            logs.append(log)
        return logs







    

