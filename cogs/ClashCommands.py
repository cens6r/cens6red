import discord, requests
from discord.ext import commands

headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRkNGI2YTdjLTg4ZDAtNDlmMy05NzJiLWMwMDIxNDU2ZGM1NyIsImlhdCI6MTY0OTQwOTQ0Niwic3ViIjoiZGV2ZWxvcGVyLzI4NTcyYTAzLWMxOTQtZjZiNi02YTg2LWQyNzg5MzZhM2M5YiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0NS43OS4yMTguNzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.LKrrziKt4bsfN-9ic8T-ZU8A54_gjelTmuohTmMFqG6GbSAE0n76V18bCMXB4VXienH0h4Qb1HcNjwMsA8Fx8w"}
api = 'https://proxy.royaleapi.dev'

class ClashCommands(commands.Cog):

    def __init__(self , Client):
        self.Client = Client

    @commands.command()
    @commands.guild_only()
    async def cr(self, ctx, tag: str):
        playerTag = tag.replace('#', '%23')
        r = requests.get(f'{api}/players/{playerTag}', headers=headers)
        json = r.json()

        name = json['name']
        level = json['expLevel']
        trophies = json['trophies']
        bestTrophies = json['bestTrophies']
        wins = json['wins']
        losses = json['losses']
        battleCount = json['battleCount']
        threeCrowns = json['threeCrownWins']
        challengeCardsWon = json['challengeCardsWon']
        challengeMaxWins = json['challengeMaxWins']
        tournamentCardsWon = json['tournamentCardsWon']
        tournamentBattleCount = json['tournamentBattleCount']
        clanRole = json['role']
        clanDonations = json['donations']
        clanDonationsRecieved = json['donationsRecieved']
        clanTotalDonations = json['totalDonations']
        clanWarDayWins = json['warDayWins']
        clanCardsCollected = json['clanCardsCollected']
        clanName = json['clan']['name']
        arena = json['arena']['name']

        nonMasteryBadges = []

        for i in json['badges']:
            if 'Mastery' not in i['name']:
                nonMasteryBadges.append({
                    "name": str(i['name']),
                    "level": str(i['level']),
                    "maxLevel": str(i['maxLevel'])
                })

        favoriteCard = json['currentFavouriteCard']['name']

        embed = discord.Embed(name=f'Stats for {name}', description=f'clash royale information search: {playerTag}', color=discord.Colour.blurple())
        embed.add_field(name='Username', value=name)
        embed.add_field(name='Level', value=str(level))
        embed.add_field(name='Trophies', value=f'{str(trophies)}/{str(bestTrophies)}')
        embed.add_field(name='Battles', value=f'Played: {str(battleCount)} matches, Won: {str(wins)}, Three Crowned: {str(threeCrowns)}, Lost: {str(losses)}')
        embed.add_field(name='Challenges', value=f'Max Wins: {str(challengeMaxWins)}, Earned: {str(challengeCardsWon)} cards')
        embed.add_field(name='Tournaments', value=f'Battle Count: {str(tournamentBattleCount)}, Earned: {str(tournamentCardsWon)} cards')
        embed.add_field(name='Clan', value=f'Name: {clanName}\nRole: {clanRole}\nDonations: Donated {str(clanDonations)}, Recieved {str(clanDonationsRecieved)}, Total Donations {str(clanTotalDonations)}, War Day Wins: {str(clanWarDayWins)}\nClan Cards Collected: {str(clanCardsCollected)}')
        embed.add_field(name='Arena', value=arena)
        embed.add_field(name='Favorite Card', value=favoriteCard)

        for d in nonMasteryBadges:
            n = d['name']
            l = d['level']
            m = d['maxLevel']

            embed.add_field(name=n, value=f'Level: {l}/{m}')

        await ctx.send(embed=embed)


def setup(Client):
    Client.add_cog(ClashCommands(Client))