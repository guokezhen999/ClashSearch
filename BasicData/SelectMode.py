from enum import Enum

class PlayerType(Enum):
    NO_TYPE = 0
    MY_PLAYER = 1
    CLAN_PLAYER = 2
    FOCUS_PLAYER = 3
    ROBOT = 4
    ONLINE_PLAYER = 5
    CLAN_FORM_PLAYER = 6

class WarState(Enum):
    NOT_IN_WAR = "notInWar",
    IN_WAR = "inWar",
    PREPARATION = "preparation",
    WAR_ENDED = "warEnded"

class ClanType(Enum):
    ONLINE = 0
    OFFLINE = 1