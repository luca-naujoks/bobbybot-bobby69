from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

#Message delite command(clear)
class ENTF(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="clear")
    async def clear_command(self, ctx: Context):
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            args = ctx.message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1

                    def is_not_pinned(mess):
                        return not mess.pinned
                    delitet = await ctx.channel.purge(limit=count, check=is_not_pinned)
                    await ctx.send("{} Nachrichten wurden erfolgreich gelöscht.".format(len(delitet)-1))





def setup(bot: BobbyBot):
    bot.add_cog(ENTF(bot))
