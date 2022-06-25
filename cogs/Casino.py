import asyncio
import random


from discord.ext import commands
from bot import BobbyBot
import mysql.connector

client = commands.Bot


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

    @commands.command(name="get_wallet", aliases=["new"])
    async def get_wallet_command(self, ctx):
        if ctx.channel.name == "casino":
            mycursor = mydb.cursor()
            exsist = f"SELECT COUNT(*) FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
            mycursor.execute(exsist)
            exsist_result = float(mycursor.fetchone()[0])

            if exsist_result == 0:
                sql1 = f"INSERT INTO CASINO (USER_ID, USER_NAME) VALUES('{ctx.message.author.id}', '{ctx.message.author.name}')"
                mycursor.execute(sql1)
                get_coins = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
                mycursor.execute(get_coins)
                wallet = float(mycursor.fetchone()[0])
                await ctx.send(f"You now have a game wallet with {wallet} coins")
            else:
                get_coins = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
                mycursor.execute(get_coins)
                wallet = float(mycursor.fetchone()[0])
                if wallet < 200:
                    await ctx.send("Your Wallet is below the 200 coin mark, you cannot reset your Wallet.\nI will contact an admin to clear it")
                    await asyncio.sleep(5)
                    dm = "Your wallet has been reset. You now have 200 starter coins in your wallet"
                    await ctx.send(
                        f"@{ctx.message.author.name} Your wallet has been reset. You now have 200 starter coins in your wallet GLHF =D")
                    await ctx.author.send(dm)
                    sql = f"UPDATE CASINO SET COINS = 200 WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(sql)
                else:
                    get_coins = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(get_coins)
                    wallet = float(mycursor.fetchone()[0])
                    await ctx.send(f"You already have a Wallet with {wallet} coins\nDo you want to reset the wallet?(Yes/No)")

                    try:
                        message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=60.0)
                    except asyncio.TimeoutError:
                        await ctx.send("Ignoring me is not nice. Your wallet continues to exist!")
                    else:
                        if message.content.lower() == "yes" or "no":
                            if message.content.lower() == "yes":
                                dm = "Your wallet has been reset. You now have 200 starter coins in your wallet"
                                await ctx.send(f"@{ctx.message.author.name} Your wallet has been reset. You now have 200 starter coins in your wallet GLHF =D")
                                await ctx.author.send(dm)
                                sql = f"UPDATE CASINO SET COINS = 200 WHERE USER_ID = '{ctx.message.author.id}'"
                                mycursor.execute(sql)
                            if message.content.lower() == "no":
                                await ctx.send(f"@{ctx.message.author.name} wallet reset canceled")
            mydb.commit()
            mycursor.close()

    @commands.command(name="wallet")
    async def wallet_command(self, ctx):
        if ctx.channel.name == "casino":
            mycursor = mydb.cursor()
            print(ctx.message.author.id)
            sql1 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
            mycursor.execute(sql1)
            wallet = float(mycursor.fetchone()[0])
            await ctx.send(f"Your wallet contains {wallet} coins")
            mydb.commit()
            mycursor.close()



    @commands.command(name="hurensohn")
    async def kopfoderzahl(self, ctx):
        """if ctx.channel.name == "casino":"""
        win_list = ["Good Job", "Wow Nice Cock"]
        lose_list = ["u hava a small pp like ur purse", "oh no u lose NOOB", "maybe next time you're also on the winning team", "maybe nextime du hurensohn"]
        ergebnise = ("kopf", "zahl")
        ergebnis = (random.choice(ergebnise))
        await ctx.send("you against the bank\nChose your side: **Kopf** or **Zahl**")

        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.channel.send("You didn't choose. Your 10 coins go to the bank")
            mycursor = mydb.cursor()
            sql1 = f"UPDATE CASINO SET COINS = COINS {-10} WHERE USER_ID = '{ctx.message.author.id}'"
            mycursor.execute(sql1)
            sql2 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
            mycursor.execute(sql2)
            wallet = float(mycursor.fetchone()[0])
            await ctx.send(f"Your wallet now contains {wallet} coins")
            mydb.commit()
            mycursor.close()
        else:
            if message.content.lower() == "kopf" or "zahl":

                if message.content.lower() == ergebnis:
                    await ctx.send("Win")
                    await ctx.send(random.choice(win_list))
                    mycursor = mydb.cursor()
                    sql1 = f"UPDATE CASINO SET COINS = COINS {+20} WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(sql1)

                    sql2 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(sql2)
                    wallet = float(mycursor.fetchone()[0])
                    await ctx.send(f"Your wallet now contains {wallet} coins")
                    mydb.commit()
                    mycursor.close()
                else:
                    await ctx.send("Lose")
                    await ctx.send(random.choice(lose_list))
                    mycursor = mydb.cursor()
                    sql1 = f"UPDATE CASINO SET COINS = COINS {-10} WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(sql1)
                    sql2 = f"SELECT COINS FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
                    mycursor.execute(sql2)
                    wallet = float(mycursor.fetchone()[0])
                    await ctx.send(f"Your wallet now contains {wallet} coins")
                    mydb.commit()
                    mycursor.close()
            else:
                await ctx.send("Are you stupid or something? **Heads** or **tails**")

        mycursor = mydb.cursor()
        sql1 = f"UPDATE CASINO SET GAMES = GAMES+1 WHERE USER_ID = '{ctx.message.author.id}'"
        mycursor.execute(sql1)
        mydb.commit()

        sql2 = f"SELECT GAMES FROM CASINO WHERE USER_ID = '{ctx.message.author.id}'"
        mycursor.execute(sql2)
        games = float(mycursor.fetchone()[0])
        print(games)
        if 1 < games > 20:
            await ctx.send("noob")
        mycursor.close()






def setup(bot: BobbyBot):
    bot.add_cog(Casino(bot))
