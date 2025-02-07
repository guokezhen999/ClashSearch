from BasicData import *

# clash of clans 账号
class ClashAccountInfo:
    def __init__(self):
        self.email = "guokezhen999@gmail.com"
        self.password = "juju200207"

# 数据库信息
class DatabaseInfo:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.username = "root"
        self.password = "juju200207"
        self.database = "clashofclans_qt"
        self.charset = "utf8mb4"

        self.myPlayers = "my_players"
        self.robots = "robots"
        self.clans = "clans"
        self.clanPlayers = "clan_players"
        self.focusPlayers = "focus_players"
        self.warLog = "clan_war_log"

        self.startDate = datetime.date(2024, 9, 17)

