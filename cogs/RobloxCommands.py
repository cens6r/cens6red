import discord
import requests

from discord.ext import commands

class RobloxCommands(commands.Cog):

    def __init__(self, Client):
        self.Client = Client
        self.userApi = 'https://users.roblox.com/v1'
        self.ThumbnailApi = 'https://thumbnails.roblox.com/v1'

    @commands.command()
    async def user(self, ctx, uuid):
        channel = ctx.message.channel

        ID = int(uuid)
        url = self.userApi+f'/users/{ID}'

        request = requests.get(url)
        get = request.json()

        request2 = requests.get(self.ThumbnailApi+'/users/avatar-headshot?userIds={ID}&size=48x48&format=Png&isCircular=false')
        get2 = request2.json()

        displayName = get['displayName']
        username = get['name']
        creationdata = get['created'][10:]

        headshot = get2['data'][0]['imageUrl']

        embed = discord.Embed(title=f"{displayName} (@{username})", description="Roblox User Information", color=discord.Color.red)
        
        embed.set_thumbnail(url=headshot)
        
        embed.add_field(name="Username", value=username, inline=True)
        embed.add_field(name="Display Name", value=displayName, inline=True)
        embed.add_field(name="Creation Date", value=creationdata, inline=False)

        await channel.send(embed=embed)

def setup(Client):
    Client.add_cog(RobloxCommands(Client))
