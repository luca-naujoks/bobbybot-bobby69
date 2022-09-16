import asyncio

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Context
from bot import BobbyBot

client = discord.Client()


class Status(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot
        self.activities = [


            discord.Game('Bobby Bot™'),
            discord.Game('mit deiner mudda =D'),
            discord.Activity(type=discord.ActivityType.watching, name='OBI-WAN KENOBI auf Disney+')

        ]
        self.activity.start()


    @tasks.loop(seconds=300)
    async def activity(self):
        current_activity = self.activities.pop(0)
        self.activities.append(current_activity)
        await self.bot.change_presence(activity=current_activity)

    @activity.before_loop
    async def before_activity(self):
        await self.bot.wait_until_ready()


# info command
    @commands.command(name="info", aliases=[])
    async def info_command(self, ctx: Context):
        await ctx.send("Wozu brauchst du infos/hilfe?(Bot/Casino)")
        try:
            message = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        except asyncio.TimeoutError:
            await ctx.send("Ignoring me is not nice!")
        else:
            if message.content.lower() == "bot" or "casino":
                if message.content.lower() == "bot":
                    await ctx.send("Bot Status= online\n---------------------\nBefehle Benötigen kein Präfix")
                    await ctx.send("-valo\n-clear xxx\n-bot\n-csgo\n-play oder p\n-lonely\n")
                    await ctx.send("Bitte keine unnötigen pings\nUnd erstrecht keine rollen oder everyone pingen\nDanke <3")
                else:
                    embed = (discord.Embed(title='How to use the Casino',
                                           color=discord.Color.purple())
                             .add_field(name='How to get a Wallet:',
                                        value='1. Use the "New" command to create a new game wallet\n2. You can use the "Wallet" to see how much coins you have. The account balance is\ndisplayed after each game\n\n**How to play:**\n3. With the "Hurensohn" command you can start the coin flip game\n\nMore games will follow =D'))
                    await ctx.send(embed=embed)



def setup(bot: BobbyBot):
    bot.add_cog(Status(bot))
