import discord
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot



class Itx2(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="stundenplan", aliases=["plan"])
    async def stundenplan_command(self, ctx):
        await ctx.send(file=discord.File('images/plan.png'))

    @commands.command(name="key", aliases=["key?", "k?"])
    async def moodle_key_command(self, ctx,):
        async with ctx.typing():
            embed = (discord.Embed(title="Moodle Einschreib Schlüssel",
                                   colour=discord.Color.purple(),
                                  description="get (user_id course_id)"))
        await ctx.send(embed=embed)





def setup(bot: BobbyBot):
    bot.add_cog(Itx2(bot))