class Items:
    heroes = [
        "Barbarian King", "Archer Queen", "Minion Prince", "Grand Warden", "Royal Champion"
    ]

    heroesCN = [
        "野蛮人之王", "弓箭女皇", "亡灵王子", "大守护者", "飞盾战神"
    ]

    roleDict = {
        "member":"成员",
        "elder":"长老",
        "co_leader":"副首领",
        "leader":"首领"
    }

    troops = [
        "Barbarian", "Archer", "Goblin", "Giant", "Wall Breaker",
        "Balloon", "Wizard", "Healer", "Dragon", "P.E.K.K.A",
        "Baby Dragon", "Miner", "Electro Dragon", "Yeti", "Dragon Rider",
        "Electro Titan", "Root Rider", "Thrower",
        "Minion", "Hog Rider", "Valkyrie", "Golem", "Witch", "Lava Hound",
        "Bowler", "Ice Golem", "Headhunter", "Apprentice Warden", "Druid",
        "Wall Wrecker", "Battle Blimp", "Stone Slammer", "Siege Barracks",
        "Log Launcher", "Flame Flinger", "Battle Drill", "Troop Launcher"
    ]

    spells = [
        "Lightning Spell", "Healing Spell", "Rage Spell", "Jump Spell",
        "Freeze Spell", "Clone Spell", "Invisibility Spell", "Recall Spell",
        "Poison Spell", "Earthquake Spell", "Haste Spell", "Skeleton Spell",
        "Bat Spell", "Overgrowth Spell"
    ]

    pets = [
        "L.A.S.S.I", "Electro Owl", "Mighty Yak", "Unicorn", "Frosty",
        "Diggy", "Poison Lizard", "Phoenix","Spirit Fox", "Angry Jelly"
    ]

    equipments= [
        ["Barbarian Puppet", "Rage Vial", "Earthquake Boots", "Vampstache", "Giant Gauntlet", "Spiky Ball"],
        ["Archer Puppet", "Invisibility Vial", "Giant Arrow", "Healer Puppet", "Frozen Arrow", "Magic Mirror"],
        ["Henchmen Puppet", "Dark Orb"],
        ["Eternal Tome", "Life Gem", "Rage Gem", "Healing Tome", "Fireball", "Lavaloon Puppet"],
        ["Seeking Shield", "Royal Gem", "Hog Rider Puppet", "Haste Vial", "Rocket Spear", "Electro Boots"]
    ]

    equipments1d= [i for item in equipments for i in item]

    builderTroops = [
        "Raged Barbarian",
        "Sneaky Archer",
        "Boxer Giant",
        "Beta Minion",
        "Bomber",
        "Baby Dragon Builder",
        "Cannon Cart",
        "Night Witch",
        "Drop Ship",
        "Power P.E.K.K.A",
        "Hog Glider",
        "Electrofire Wizard"
    ]

    builderHeroes = [
        "Battle Machine", "Battle Copter"
    ]

    playerInfos = [
        "Name", "Tag", "Exp Level", "Town Hall", "Town Hall Weapon",
        "Builder Hall", "Clan", "Clan Tag", "Role", "War Stars",
        "Trophies", "Best Trophies", "Legend Trophies", "Builder Base Trophies",
        "Best Builder Base Trophies", "Donations", "Received", "Attack Wins",
        "Defense Wins", "Capital Gold", "Home Heroes Level Sum", "Builder Heroes Level Sum",
        "Email", "Bind Date"
    ]

    strPlayerInfos = [
        "Name", "Tag", "Clan", "Clan Tag", "Role", "Email", "Bind Date"
    ]

    intPlayerInfos = [
        "Exp Level", "Town Hall", "Town Hall Weapon", "Builder Hall", "War Stars",
        "Trophies", "Best Trophies", "Legend Trophies", "Builder Base Trophies",
        "Best Builder Base Trophies", "Donations", "Received", "Attack Wins",
        "Defense Wins", "Capital Gold", "Home Heroes Level Sum", "Builder Heroes Level Sum",
    ]

    playerFigInfos = [
        "Exp Level", "Town Hall", "Town Hall Weapon",
        "Builder Hall", "War Stars",
        "Trophies", "Best Trophies", "Legend Trophies", "Builder Base Trophies",
        "Best Builder Base Trophies", "Donations", "Received", "Attack Wins",
        "Defense Wins", "Capital Gold", "Home Heroes Level Sum", "Builder Heroes Level Sum"
    ]

    playerInfosDict = {
        "Name": "名称",
        "Tag": "标签",
        "Exp Level": "等级",
        "Town Hall": "大本",
        "Town Hall Weapon": "武器",
        "Builder Hall": "夜本",
        "Clan": "部落名",
        "Clan Tag": "部落标签",
        "Role": "职位",
        "War Stars": "战星",
        "Trophies": "奖杯",
        "Best Trophies": "最高奖杯",
        "Legend Trophies": "传奇奖杯",
        "Builder Base Trophies": "夜奖杯",
        "Best Builder Base Trophies": "夜最高奖杯",
        "Donations": "增援",
        "Received": "接收",
        "Attack Wins": "胜场",
        "Defense Wins": "防守",
        "Capital Gold": "都城币",
        "Home Heroes Level Sum": "英雄等级总和",
        "Builder Heroes Level Sum": "夜英雄等级总和",
        "Email": "邮箱",
        "Bind Date": "绑定日期"
    }

    playerInfosDictInv = {v:k for k, v in playerInfosDict.items()}

    clanInfos = [
        "Name", "Tag", "Level", "Member Count", "War League",
        "Points", "Builder Base Points", "Capital Peak Level",
        "Capital Points", "War Frequency", "War Win Streak",
        "War Wins", "War Losses", "War Ties", "Location",
        "Type", "Required Trophies", "Required Builder Base Trophies",
        "Required Townhall", "Public War Log", "Description"
    ]

    intClanInfos = [
        "Level", "Member Count", "Points", "Builder Base Points", "Capital Peak Level",
        "Capital Points", "War Win Streak",
        "War Wins", "War Losses", "War Ties", "Required Trophies", "Required Builder Base Trophies",
        "Required Townhall"
    ]

    clanInfosDict = {
        "Name":"名称",
        "Tag":"标签",
        "Level":"等级",
        "Member Count":"人数",
        "War League":"联赛",
        "Points":"积分",
        "Builder Base Points":"夜世界积分",
        "Capital Peak Level":"都城之巅",
        "Capital Points":"都城积分",
        "War Frequency":"对战频率",
        "War Win Streak":"连胜数",
        "War Wins":"胜利",
        "War Losses":"失败",
        "War Ties":"平局",
        "Location":"位置",
        "Type":"类型",
        "Required Trophies":"需要奖杯",
        "Required Builder Base Trophies":"夜世界奖杯",
        "Required Townhall":"需要大本",
        "Public War Log":"公开日志",
        "Description":"描述"
    }

    timeZone = 8

    warLogInfos = [
        "Name", "Tag", "Clan Level", "Badge Url",
        "Opponent Name", "Opponent Tag", "Opponent Clan Level", "Opponent Badge Url",
        "Result", "End Time", "Team Size", "Attacks",
        "Stars", "Destruction Percentage", "Opponent Stars", "Opponent Destruction Percentage",
        "Exp Earned"
    ]

    playerAchievementsDict = {
        'Gold Grab': '抢夺金币',
        'Elixir Escapade': '抢夺圣水',
        'Heroic Heist': '抢夺黑️油',
        'Well Seasoned': '月度挑战',
        'Nice and Tidy': '挖树',
        'Clan War Wealth': '城堡金币',
        'Friend in Need': '捐兵总数',
        'Sharing is caring': '捐法术数',
        'Siege Sharer': '攻城机器',
        'War League Legend': '联赛星',
        'Games Champion': '竞赛',
        'Unbreakable': '防守胜利',
        'Conqueror': '进攻胜利',
        'Humiliator': '摧毁大本',
        'Not So Easy This Time': '摧毁大本武器',
        'Union Buster': '建筑小屋',
        'Bust This!': '武器小屋',
        'Wall Buster': '摧毁城墙',
        'Mortar Mauler': '迫击炮',
        'X-Bow Exterminator': 'X连弩',
        'Firefighter': '地狱之塔',
        'Anti-Artillery': '鸟炮',
        'Shattered and Scattered': '投石炮',
        'Counterspell': '法术塔',
        'Monolith Masher': '擎天柱',
        'Superb Work': '超级兵',
        'Get even more Goblins!': '单人模式',
        'Un-Build It': '建筑大本',
        'Aggressive Capitalism': '都城突袭',
    }

