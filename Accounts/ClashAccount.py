import coc

from BasicData.AccountInfo import ClashAccountInfo
from Accounts import *

class ClashAccount(ClashAccountInfo):
    def __init__(self):
        super().__init__()
        self.client = coc.Client()

    async def login(self):
        try:
            await self.client.login(self.email, self.password)
        except coc.InvalidCredentials as error:
            exit(error)

    async def close(self):
        await self.client.close()

    async def searchPlayer(self, tag: str):
        # 根据标签查询玩家
        player = await self.client.get_player(tag)
        return player

    async def searchPlayers(self, tags: list[str]):
        players = []
        async for player in self.client.get_players(tags):
            players.append(player)
        return players

    async def searchClan(self, tag: str):
        clan = await self.client.get_clan(tag)
        return clan

    async def searchClans(self, tags: list[str]):
        clans = []
        async for clan in self.client.get_clans(tags):
            clans.append(clan)
        return clans

    async def searchWar(self, tag: str):
        war = await self.client.get_current_war(tag)
        return war

    async def searchWars(self, tags: list[str]):
        wars = []
        async for war in self.client.get_current_wars(tags):
            wars.append(war)
        return wars

    async def searchLeague(self, tag: str):
        league = await self.client.get_league_group(tag)
        return league

    async def searchWarLog(self, tag: str, limit: int = 0):
        warLog = await self.client.get_war_log(tag, limit=limit)
        return warLog

    async def verifyToken(self, tag: str, token: str):
        await self.client.verify_player_token(tag, token)

async def main_1():
    account = ClashAccount()
    await account.login()
    player = await account.searchPlayer("#QRYU2892P")
    for troop in player.builder_troops:
        print(troop.name)
    for spell in player.heroes:
        print(spell.name)

async def main_2():
    account = ClashAccount()
    await account.login()
    players = await account.searchPlayers(["#QRYU2892P", "#8YCG2P2YV"])
    print(players)
    for achevement in players[0].achievements:
        print(achevement.name, achevement.value)
    await account.close()

async def main_3():
    tag = "#2J29JJC20"
    account = ClashAccount()
    await account.login()
    clan = await account.searchClan(tag)
    print(clan)
    await account.close()

async def main4():
    tag = "#2GYCCL8U9"
    tag2 = "#Y90CVR2J"
    account = ClashAccount()
    await account.login()
    war1 = await account.searchWar(tag)
    war2 = await account.searchWar(tag2)
    league = await account.searchLeague(tag2)
    await account.close()

async def main5():
    tag = "#QRYU2892P"
    token = "c2d8jx4m"
    account = ClashAccount()
    await account.login()
    # await account.verifyToken(tag, token)
    await account.close()

async def clanWarTest():
    tag = "#2GUGRRLR0"
    account = ClashAccount()
    await account.login()
    war = await account.searchWar(tag)
    await account.close()

async def warLeagueTest():
    tag = "#2GUGRRLR0"
    account = ClashAccount()
    await account.login()
    clanWar = await account.searchWar("2RPCV9LQJ")
    war = await account.searchLeague(tag)
    war2 = await account.client.get_league_war('#8PGPU8RJC')
    warLog = await account.searchWarLog(tag)
    await account.close()


if __name__ == "__main__":
    asyncio.run(main_1())

# _init_logs : list[dict]