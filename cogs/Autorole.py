import discord
from discord.ext import commands
from bot import BobbyBot

client = discord.Client()


class Autorole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name="Legend")
        await client.add_role(member, role)

    @client.event
    async def on_member_join(self, member, ctx):
        ctx.send("We get a new member.")




def setup(bot: BobbyBot):
    bot.add_cog(Autorole(bot))

