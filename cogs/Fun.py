import discord
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot
from discord import FFmpegPCMAudio

client = discord.Client

class Fun(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    def HEY(self):
        print("HEY")


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

    @commands.command(name="mc_server")
    async def mc_server(self, ctx):
        if 528982743623925781 == ctx.message.author.id:
            await ctx.send("@here")
            embed = discord.Embed(title="Mc Mod Server",
                                  description=f"Da Malte jetzt raus ist können wir auch ein nicht Skyblock Modpack spielen.\n Wenn ihr Vorschläge habt gerne her damit wenn wir ein nices Modpack oder so gefunden haben, dass allen zumindest etwas passt würde ich dann einen\n [g-portal server mit 6gb und Infinitive slots](https://www.g-portal.com/de/order/step/one/minecraft) hosten.\n Ihr braucht nichts dazuzugeben.\n Ich hatte bei dem modpack an sowas wie [FTB Infinity Evolved Reloaded](https://www.curseforge.com/minecraft/modpacks/infinityevolved-reloaded) gedacht.\nDas Spielt in der 1.12.2",
                                  color=discord.Color.purple())
            await ctx.send(embed=embed)
        else:
            return


    @commands.command(name="mc.server")
    async def mc_server(self, ctx):
        if 528982743623925781 == ctx.message.author.id:
            await ctx.send("@here")
            embed = discord.Embed(title="Mc Mod Server",
                                  description=f"Ich habe mich jetzt erstmal für das [FTB Infinity Reloaded](https://www.curseforge.com/minecraft/modpacks/infinityevolved-reloaded/files) Modpack entschieden.\nDafür müsst ihr aber die [CurseForge App](https://download.curseforge.com/) Herunterladen und das Modpack dort Installieren (Soweit ich das weiß).\nIch würde den server dann zu Freitag Mittag/Nachmittag dann Mieten.\nPasst das Jedem?\nIhr könnt gerne noch eins zwei weitere leute nach einladen müssen nur wegen der Performance Gucken",
                                  color=discord.Color.purple())
            await ctx.send(embed=embed)
        else:
            return


def setup(bot: BobbyBot):
    bot.add_cog(Fun(bot))
