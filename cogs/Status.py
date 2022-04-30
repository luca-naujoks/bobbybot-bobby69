import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from bot import BobbyBot

client = discord.Client()


class Status(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot
        self.activities = [
            discord.Game('Bobby Bot™'),


        ]
        self.activity.start()

    @tasks.loop(seconds=300)
    async def activity(self):
        current_activity = self.activities.pop(0)
        self.activities.append(current_activity)
        await self.bot.change_presence(activity=current_activity)

    @activity.before_loop
    async def before_activity(self):
        await self.bot.wait_until_ready()


# info command
    @commands.command(name="info")
    async def info_command(self, ctx: Context):
        await ctx.send("Bot Status= online\n---------------------\nBefehle Benötigen kein Präfix")
        await ctx.send("-valo\n-clear xxx\n-bot\n-csgo\n-play oder p\n-lonely\n")
        await ctx.send("Bitte keine unnötigen pings\nUnd erstrecht keine rollen oder everyone pingen\nDanke <3")



def setup(bot: BobbyBot):
    bot.add_cog(Status(bot))
