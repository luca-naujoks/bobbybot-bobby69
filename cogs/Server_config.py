import discord
from discord.ext import commands
from bot import BobbyBot
import mysql.connector

mydb = mysql.connector.connect(
  host="server",
  user="bobby",
  password="08Kasper06!By",
  database="BobbyBot",
  port="3306"
)

class Server_config(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    def create_embed_de(self):
        embed = discord.Embed(title="**__Einstellungen:__**", color=0x4e00ff)
        embed.add_field(name="1. Language", value="", inline=False)
        embed.add_field(name="2. Roles", value="", inline=False)

    def create_embed_eng(self):
        embed = discord.Embed(title="**__Settings:__**", color=0x4e00ff)
        embed.add_field(name="1. Language", value="", inline=False)
        embed.add_field(name="2. Roles", value="", inline=False)

    @commands.command(name="Einstellungen", aliases=["Einstellung", "Settings", "⚙"])
    @commands.is_owner()
    async def settings(self, ctx):
        mycursor = mydb.cursor()
        language = f"SELECT LANGUAGE FROM Server_Config WHERE Server_Config.ServerID = '{ctx.message.guild.id}'"
        mycursor.execute(language)
        language_result = (mycursor.fetchone()[0])
        if language_result == "DE":
            await ctx.send("__**Einstellungen:**__\n\n__1. Sprache\n2. Rollen__")
        else:
            await ctx.send("__**Settings:**__\n\n__1. Language\n2. Role__")





def setup(bot: BobbyBot):
    bot.add_cog(Server_config(bot))