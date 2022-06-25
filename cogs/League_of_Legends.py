from discord.ext import commands
import random as rnd
from bot import BobbyBot

members = []

class League_of_Legends(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="lol", aliasses=["LoL", "League"])
    async def Leauge_command(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("please connect to a voice channel")
            return
        else:
            await ctx.send("Teams will be drawn...")
            if ctx.author.voice is not None:
                member = ctx.author.voice.channel.members
                for m in member:
                    members.append(str(m))
                rnd.shuffle(members)
                print(members)
                try:
                    members.remove('Bobby69#5219')
                    members.remove('Bobby Cam#0554')
                    members.remove('BobbyPad69#9749')
                    members.remove('Nice Mareice#5499')
                    members.remove('vani#2205')
                    members.remove('')
                finally:
                    length = len(members)
                    midddle_index = length//2
                    first_team = members[:midddle_index]
                    second_team = members[midddle_index:]
                    await ctx.send(f"Team 1: {', '.join(first_team)}")
                    await ctx.send(f"Team 2: {', '.join(second_team)}")



def setup(bot: BobbyBot):
    bot.add_cog(League_of_Legends(bot))