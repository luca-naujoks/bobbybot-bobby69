import asyncio
import random as rnd
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

Map = ["Split", "Ascent", "Breeze", "Ice Box", "Haven"]
rnd.seed()
rnd.shuffle(Map)
members = []

class Valo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




    @commands.command(name="valo")
    async def valo_command(self, ctx: Context):
        if ctx.author.voice is None:
            await ctx.send("please connect to a voice channel")
            return
        else:
            await ctx.send("Teams und Map werden Gewählt...")
            await asyncio.sleep(0.5)
            await ctx.send("Es wird Gespielt:")
            await ctx.send(rnd.choice(Map))
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
    bot.add_cog(Valo(bot))
