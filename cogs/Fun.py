import discord
import aiohttp
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot
from waifuim import WaifuAioClient
from pytube import YouTube
import os
from discord import FFmpegPCMAudio

client = discord.Client

class Fun(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="lonely")
    async def lonely_command(self, ctx):
        selected_tag1 = ""
        slected_tag2 = ""


        await ctx.message.add_reaction('❤')
        await ctx.send(f'Heyy hoffentlich jetzt nicht mehr =D\n Btw Brauchst du eine waifu?')
        message = await self.bot.wait_for('message',
                                          check=lambda m: m.author == ctx.author and m.channel == ctx.channel,
                                          timeout=30.0)
        if message.content.lower() == "ja":
            HEADERS = {'User-Agent': f'aiohttp/{aiohttp.__version__}; YourAppName'}
            url = "https://api.waifu.im/random/?excluded_files=4401.jpeg" \
                  "&excluded_files=3133" \
                  "&gif=false" \
                  "&included_tags=maid" \
                  "&included_tags=oppai" \
                  "&included_tags=ass" \
                  "&is_nsfw=true"

            session = aiohttp.ClientSession()

            async with session.get(url, headers=HEADERS) as resp:
                api = await resp.json()
                if resp.status in {200, 201}:
                    url = api['images'][0]['url']
                    await ctx.send(url)
                else:
                    error = api['detail']
            await session.close()




    @commands.command(name="Bot")
    async def botinfo(self, ctx: Context):
        await ctx.send("\nIch bin Bobby.\nIch kann einiege befehle, welche du mit info einsehen kannst.")

    @commands.command(name="whereAmI", aliases=["where"])
    async def whereAmI_command(self, ctx):
        message = f'You are in {ctx.message.guild.name} in the {ctx.message.channel.mention} channel'
        await ctx.message.author.send(message)

    @commands.command(name="moveme", aliases=["move"])
    async def move_command(self, ctx, member: discord.Member, channel: discord.VoiceChannel):
        await member.move_to(channel)

    @commands.command(name="Scottie!!!", aliases=["beammeup"])
    async def move_command(self, ctx):
        user = ctx.message.author
        Gott = discord.utils.get(ctx.guild.roles, name="Bobby Gott")
        captain = discord.utils.get(ctx.guild.roles, name="Captain")
        if Gott or captain in user.roles:
            await ctx.send(f"I Beam you up {ctx.message.author.name}")
            channel = ctx.bot.get_channel(953024165340921886)
            member = ctx.message.author
            await member.move_to(channel)
        else:
            await ctx.send(f"You have to be a Captain to order a teleport {ctx.message.author.name}")

    @commands.command(name="Texturlotlys", aliases=["Texturepack"])
    async def texture_pack(self, ctx):
        await ctx.send("You can Download the Texture Pack from my OndeDrive\nhttps://1drv.ms/f/s!Ak8D0N35yzURgfdbUwznzh5qAeEgDA")


    @commands.command(name="kick")
    async def kick(self, ctx, user: discord.Member, *, reason="Deine verbindung ist unsicher und dein Client weißt Schädliche strukturen auf"):
        if 528982743623925781 == ctx.message.author.id:
            await user.kick(reason=reason)
            kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}",
                                 colour=discord.Color.purple())
            await ctx.message.delete()
            await ctx.channel.send(embed=kick)
            await user.send(embed=kick)
        else:
            await ctx.message.delete()

    @commands.command(name="nsfw")
    async def nfsw_command(self, ctx):
        if ctx.channel.is_nsfw():
            await ctx.send("yes")
        else:
            await ctx.send("no")
    @commands.command(name="LUNA", aliases=["LUNA?"])
    async def WAS_IST_LUNA(self, ctx):
        luna = "Was LUNA ist?\n"
        luna1 = "LUNA ist ein KI versuch von Bobby. Sie Soll metadaten überwachen das Smarthome steuern usw. :)"
        await ctx.send(luna + luna1)


def setup(bot: BobbyBot):
    bot.add_cog(Fun(bot))
