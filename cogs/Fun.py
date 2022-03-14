import discord
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot
from discord import FFmpegPCMAudio

client = discord.Client

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

    @commands.command(name="whereAmI", aliases=["where"])
    async def whereAmI_command(self, ctx):
        message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention} channel'
        await ctx.message.author.send(message)

    @commands.command(name="moveme", aliases=["move"])
    @commands.has_any_role("Bobby Gott", "Dick")
    async def move_command(self, ctx, member: discord.Member, channel: discord.VoiceChannel):
        await member.move_to(channel)

    @commands.command(name="Scottie!!!", aliases=["beammeup"])
    async def move_command(self, ctx):
        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="Bobby Gott")
        if role in user.roles:
            await ctx.send(f"I Beam you up {ctx.message.author.name}")
            channel = ctx.bot.get_channel(953024165340921886)
            member = ctx.message.author
            await member.move_to(channel)
        else:
            await ctx.send(f"You have to be a Captain for that {ctx.message.author.name}")













def setup(bot: BobbyBot):
    bot.add_cog(Fun(bot))
