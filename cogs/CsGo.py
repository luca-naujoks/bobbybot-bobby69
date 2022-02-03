import random as rnd

from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot


class CsGo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
# cs go matchmaker
    @commands.command(name='csgo')
    async def csgo_command(self, ctx: Context):
        await ctx.send("Teams und map werden Gewählt")
        offline = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust II", "Vertigo"]
        wingman = ["Inferno", "Train", "cobblestone", "Rialto", "Lake", "Vertigo", "Calavera", "Overpass"]
        if ctx.author.voice is not None:
            member = ctx.author.voice.channel.members
            members = []
            for m in member:
                members.append(str(m))
            rnd.shuffle(member)
            if len(members) < 2:
                await ctx.send("Du gegen Bots")
            else:
                if len(members) < 5:
                    await ctx.send("es wird wingman gespielt")
                    await ctx.send(rnd.choice(wingman))
                else:
                    await ctx.send("es wird offline gespielt")
                    await ctx.send(rnd.choice(offline))
            length = len(members)
            midddle_index = length // 2
            first_team = members[:midddle_index]
            second_team = members[midddle_index:]
            await ctx.send(f"Team 1: {', '.join(first_team)}")
            await ctx.send(f"Team 2: {', '.join(second_team)}")




    @commands.command(name='cs_comp')
    async def csgo_competetive_command(self, ctx: Context):
        await ctx.send("CS GO Competetive wird vorbereitet")
        comp_map = ["Inferno", "Mirage", "Nuke", "Overpass", "Dust II", "Vertigo", "Ancient"]
        if ctx.author.voice is not None:
            member = ctx.author.voice.channel.members
            members = []
            for m in member:
                members.append(str(m))
            rnd.shuffle(member)
            length = len(members)
            midddle_index = length // 2
            first_team = members[:midddle_index]
            second_team = members[midddle_index:]
            await ctx.send(f"Team 1: {', '.join(first_team)}")
            await ctx.send(f"Team 2: {', '.join(second_team)}")


            await ctx.send(f"Team 1 {', '.join(first_team)} bitte bannt zwei maps")





def setup(bot: BobbyBot):
    bot.add_cog(CsGo(bot))
