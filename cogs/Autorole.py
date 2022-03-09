import discord
from discord import guild, member, Guild
from discord.ext import commands
from bot import BobbyBot

client = discord.Client()


class Autorole(commands.Cog):




    def __init__(self, bot):
        self.bot = bot







def setup(bot: BobbyBot):
    bot.add_cog(Autorole(bot))

