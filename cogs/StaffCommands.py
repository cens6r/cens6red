import discord
from discord.ext import commands

class StaffCommands(commands.Cog):

    def __init__(self , Client):
        self.Client = Client

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def rules(self, ctx):
    
      await ctx.message.delete()

      ruleEmbed = discord.Embed(title=ctx.guild.name, description="Rules of this server", color=discord.Colour.dark_red())
      ruleEmbed.set_thumbnail(url=ctx.guild.icon_url)

      ruleEmbed.add_field(name="1. No Spamming/Flooding", value="_ _", inline=False)
      ruleEmbed.add_field(name="2. Do not share other peoples personal information (No doxxing)", value="_ _", inline=False)
      ruleEmbed.add_field(name="3. Don't send any NSFW or contain nsfw in your server profile", value="_ _", inline=False)
      ruleEmbed.add_field(name="4. No threatening/blackmailing other people", value="_ _", inline=False)
      ruleEmbed.add_field(name="5. Have common sense", value="_ _", inline=False)
      ruleEmbed.add_field(name="6. Staff has the final choice", value="_ _", inline=False)
      ruleEmbed.set_image(url="https://i.pinimg.com/originals/c1/50/32/c150321cd8c27063d79a40d8b020aee6.gif")

      ruleEmbed.set_footer(text="https://discord.com/terms | https://discord.com/guidelines", icon_url="https://discord.com/assets/847541504914fd33810e70a0ea73177e.ico")
      
      await ctx.send(embed=ruleEmbed)

def setup(Client):
    Client.add_cog(StaffCommands(Client))
