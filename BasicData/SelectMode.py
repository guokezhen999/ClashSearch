from enum import Enum

class PlayerType(Enum):
    NO_TYPE = 0
    MY_PLAYER = 1
    CLAN_PLAYER = 2
    FOCUS_PLAYER = 3
    ROBOT = 4
    ONLINE_PLAYER = 5
    CLAN_FORM_PLAYER = 6

playerTypeNames = ["无类型", "我的玩家", "部落成员", "关注玩家", "机器人", "在线查询玩家", "部落表单玩家"]

class WarState(Enum):
    NOT_IN_WAR = "notInWar",
    IN_WAR = "inWar",
    PREPARATION = "preparation",
    WAR_ENDED = "warEnded"

class ClanType(Enum):
    ONLINE = 0
    OFFLINE = 1