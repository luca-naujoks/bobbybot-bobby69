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
            discord.Activity(type=discord.ActivityType.listening, name='Mareike <3')
        ]
        self.activity.start()

    @tasks.loop(seconds=300)
    async def activity(self):
        current_activity = self.activities.pop(0)
        self.activities.append(current_activity)
        await self.bot.change_presence(activity=current_activity)
        vc = self.bot.get_channel(864516823739269140)
        await vc.edit(name="♡Rotlichtviertel♡")

    @activity.before_loop
    async def before_activity(self):
        await self.bot.wait_until_ready()

    @client.event
    async def on_member_join(member):
        guild = client.get_guild()
        await member.send("Hi herzlich willkommen auf dem server")
        channel = await client.fetch_channel(866252599668768798)
        await channel.send(f"Wilkommen {member.mention}")
        role = discord.utils.get(guild.roles, name="Member")
        await member.add_roles(role)

    @client.event
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_ready(self):
        print("Bot is ready to go.")




# info command

    @commands.command(name="info")
    async def info_command(self, ctx: Context):
        await ctx.send("Bot Status= online\n---------------------\nBefehle Benötigen kein Präfix")
        await ctx.send("-valo\n-clear xxx\n-bot\n-csgo\n-play oder p\n-lonely\n")
        await ctx.send("Bitte keine unnötigen pings\nUnd erstrecht keine rollen oder everyone pingen\nDanke <3")



def setup(bot: BobbyBot):
    bot.add_cog(Status(bot))
