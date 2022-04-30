import discord
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

import mysql.connector

mydb = mysql.connector.connect(
  host="server",
  user="bobby",
  password="08Kasper06!By",
  database="BobbyBot",
  port="3306"
)

class Casino(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="get_wallet", aliases=["w"])
    async def get_wallet_command(self, ctx):
        mycursor = mydb.cursor()
        sql1 = f"INSERT INTO CASINO (USER_ID, USER_NAME) VALUES('{ctx.message.author.id}', '{ctx.message.author.name}')"
        mycursor.execute(sql1)

        print(sql1)
        #sql2 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
        #mycursor.execute(sql2)

        await ctx.send(f"You now have a game wallet with  coins")

    @commands.command(name="wallet")
    async def wallet_command(self, ctx):
        mycursor = mydb.cursor()
        sql1 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
        mycursor.execute(sql1)
        result = mycursor.fetchall()
        await ctx.send(f"Your wallet contains {result} coins")


    @commands.command(name="t")
    async def t(self, ctx):
        mycursor = mydb.cursor()
        sql1 = f"UPDATE CASINO SET COINS = COINS+10WHERE USER_ID = '{ctx.message.author.id}'"
        mycursor.execute(sql1)
        result = mycursor.fetchall()
        await ctx.send(f"Your wallet contains {result} coins")


def setup(bot: BobbyBot):
    bot.add_cog(Casino(bot))