import discord
import aiohttp
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

client = discord.Client

async def nsfw(ctx):
    HEADERS = {'User-Agent': f'aiohttp/{aiohttp.__version__}; YourAppName'}
    url = f"https://api.waifu.im/random/?excluded_files=4401.jpeg" \
          f"&excluded_files=3133" \
          f"&gif=false" \
          f"&included_tags=hentai" \
          f"&included_tags=oral" \
          f"&included_tags=oppai" \
          f"&included_tags=ass" \
          f"&is_nsfw=true"

    session = aiohttp.ClientSession()

    async with session.get(url, headers=HEADERS) as resp:
        api = await resp.json()
        if resp.status in {200, 201}:
            url = api['images'][0]['url']
            await ctx.send(url)
        else:
            error = api['detail']

    await session.close()

async def no_nsfw(ctx):
    HEADERS = {'User-Agent': f'aiohttp/{aiohttp.__version__}; YourAppName'}
    url = f"https://api.waifu.im/random/?excluded_files=4401.jpeg" \
          f"&excluded_files=3133" \
          f"&gif=false" \
          f"&included_tags=maid" \
          f"&included_tags=uniform" \
          f"&is_nsfw=false"

    session = aiohttp.ClientSession()

    async with session.get(url, headers=HEADERS) as resp:
        api = await resp.json()
        if resp.status in {200, 201}:
            url = api['images'][0]['url']
            await ctx.send(url)
        else:
            error = api['detail']

    await session.close()

class Waifu(commands.Cog):

    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="waifu")
    async def waifu_command(self, ctx):
        if ctx.channel.is_nsfw:
            await nsfw(ctx)
        else:
            await no_nsfw(ctx)





def setup(bot: BobbyBot):
    bot.add_cog(Waifu(bot))
