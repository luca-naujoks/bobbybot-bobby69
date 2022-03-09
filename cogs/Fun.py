from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot
from discord import FFmpegPCMAudio


class Fun(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="lonely")
    async def lonely_command(self, ctx):
        await ctx.send(f'Ich auch {ctx.message.author} Ich auch =(')


    # info über den Bot (you command)
    @commands.command(name="Bot")
    async def botinfo(self, ctx: Context):
        await ctx.send("\nIch bin Bobby.\nIch kann einiege befehle, welche du mit info einsehen kannst.")


    # rick role command
    @commands.command()
    async def rick(self, ctx: Context):
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Rickrole.mp3')
        player = voice.play(source)

    @commands.command()
    async def whereAmI(self, ctx):

        message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention} channel'
        await ctx.message.author.send(message)












def setup(bot: BobbyBot):
    bot.add_cog(Fun(bot))
