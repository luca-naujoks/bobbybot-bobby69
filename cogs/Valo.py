import asyncio
import random as rnd
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

Map = ["Split", "Ascent", "Breeze", "Ice Box", "Haven"]
rnd.seed()
rnd.shuffle(Map)


class Valo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="valo")
    async def valo_command(self, ctx: Context):
        await ctx.send("Teams und Map werden konfiguriert...")
        await asyncio.sleep(0.5)
        await ctx.send("Please wait a second...")
        await asyncio.sleep(1)
        await ctx.send("Es wird Gespielt:")
        await ctx.send(rnd.choice(Map))
        if ctx.author.voice is not None:
            member = ctx.author.voice.channel.members
            members = []
            for m in member:
                members.append(str(m))
            rnd.shuffle(member)
            members.remove('Bobby Bot')
            members.remove('Anonymes luchs')
            members.remove('Anonymes Quagga')
            members.remove('Wombat ♡')
            length = len(members)
            midddle_index = length//2
            first_team = members[:midddle_index]
            second_team = members[midddle_index:]
            await ctx.send(f"Team 1: {', '.join(first_team)}")
            await ctx.send(f"Team 2: {', '.join(second_team)}")


def setup(bot: BobbyBot):
    bot.add_cog(Valo(bot))
