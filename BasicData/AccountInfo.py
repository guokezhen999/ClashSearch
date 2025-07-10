import os

from BasicData import *
from dotenv import load_dotenv

load_dotenv()

# clash of clans 账号
class ClashAccountInfo:
    def __init__(self):
        self.email = os.environ['EMAIL']
        self.password = os.environ['PASSWORD']

# 数据库信息
class DatabaseInfo:
    def __init__(self):
        self.host = os.environ['DB_HOST']
        self.port = os.environ['DB_PORT']
        self.username = os.environ['DB_USERNAME']
        self.password = os.environ['DB_PASSWORD']
        self.database = os.environ['DB_NAME']
        self.charset = "utf8mb4"

        self.myPlayers = "my_players"
        self.robots = "robots"
        self.clans = "clans"
        self.clanPlayers = "clan_players"
        self.focusPlayers = "focus_players"
        self.warLog = "clan_war_log"

        self.startDate = datetime.date(2024, 9, 17)

