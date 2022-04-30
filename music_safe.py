import asyncio
import datetime as dt
import typing as t
import aiohttp
from async_timeout import timeout
import discord
import youtube_dl

"from PyLyrics import *"
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

LYRICS_URL = "https://some-random-api.ml/lyrics?title="

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn',
}


class NoLyricsFound(commands.CommandError):
    pass


class InvalidRepeatMode(commands.CommandError):
    pass


class SongSource(discord.PCMVolumeTransformer):

    def __init__(self, ctx, source, *, data):
        super().__init__(source)

        self.requester = ctx.author
        self.data = data


class Player:

    def __init__(self, bot, ctx):
        self.bot = bot
        self._ctx = ctx
        self._guild = ctx.guild
        self._cog = ctx.cog
        self._channel = ctx.channel

        self.queue = asyncio.Queue()
        self.next = asyncio.Event()
        self.loop = False
        self.voice_client = None
        self.current = None

        self.player_task = bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            if not self.loop:
                self.current = None
                try:
                    async with timeout(999):  # 2 Minutes timeout
                        self.current = await self.queue.get()
                except TimeoutError:
                    self.destroy(self._guild)

            source = self.current
            try:
                self._guild.voice_client.play(source, after=self.play_next_song)
            except Exception as e:
                print(e, e.__traceback__)
            info = source.data
            seconds = int(info["duration"]) % 3600
            embed = discord.Embed(title=info["title"], color=discord.Color.blurple())
            embed.set_author(name="Now playing", icon_url=source.requester.avatar_url)
            embed.set_thumbnail(url=info["thumbnail"])
            embed.add_field(name='Duration', value="{}:{:0>2}".format(seconds // 60, seconds % 60), inline=True)
            try:
                await self._ctx.send(embed=embed)
            except Exception as e:
                print(e, e.__traceback__)

            await self.next.wait()

    def play_next_song(self, error=None):
        self.next.set()

    def skip(self):
        self._guild.voice_client.stop()

    def stop(self):
        del self.queue
        self.queue = asyncio.Queue()
        self._guild.voice_client.stop()

    def destroy(self, guild):
        return self.bot.loop.create_task(self._cog.cleanup(guild))

    @commands.command(name="leave")
    async def leave_command(self, ctx: Context):
        await ctx.voice_client.disconnect()
        self.destroy(self._guild)


class Music(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass

        try:
            del self.players[guild.id]
        except KeyError:
            pass

    def get_player(self, ctx):
        """Retrieve the guild player, or generate one."""
        try:
            player = self.players[ctx.guild.id]
        except KeyError:
            player = Player(self.bot, ctx)
            self.players[ctx.guild.id] = player

        return player

    @commands.command(name="play", aliases=["p"])
    async def play_command(self, ctx: Context, *, url):
        ytdl_options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'restrictfilenames': True,
            'noplaylist': False,
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'logtostderr': False,
            'quiet': True,
            'no_warnings': True,
            'default_search': 'auto',
            'source_address': '0.0.0.0',
        }

        vc = ctx.voice_client
        if not vc:
            await ctx.invoke(self.join_command)

        ytdl = youtube_dl.YoutubeDL(ytdl_options)
        data = ytdl.extract_info(url, download=False, process=False)

        if "entries" not in data:
            process_info = data
        else:
            process_info = None
            for entry in data["entries"]:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise Exception("YTDL: No Matches")

        webpage_url = process_info['webpage_url']
        processed_info = ytdl.extract_info(webpage_url, download=False)

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise Exception("YTDL: No matches")

        """
        if ctx.author.voice is None:
            # TODO: not in vc msg
            return
        channel = ctx.author.voice.channel
        """

        player = self.get_player(ctx)
        source = SongSource(ctx, discord.FFmpegPCMAudio(info["url"], **FFMPEG_OPTIONS), data=info)
        if (not player.queue.empty()) or (player.current is not None and player.queue.empty()):
            await ctx.send("Added to queue: {}".format(info["title"]))
        await player.queue.put(source)

        """
        if player is not None:
            player.queue.append(song)
            # TODO: added song msg
            return

        if ctx.voice_client:
            voice_client = ctx.voice_client
        else:
            voice_client = await channel.connect()


        player = Player()
        player.voice_client = voice_client
        player.queue.append(song)
        self.players[ctx.guild.id] = player
        """

        """
        source = discord.FFmpegPCMAudio(info["url"], **FFMPEG_OPTIONS)
        voicec = ctx.author.voice
        channel = voicec.channel
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client is None:
            voice_client = await channel.connect()
        voice_client.play(source,)
        seconds = int(info["duration"]) % 3600
        embed = discord.Embed(title=info["title"], color=discord.Color.blurple())
        embed.set_author(name="Now playing", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=info["thumbnail"])
        embed.add_field(name='Duration', value="{}:{:0>2}".format(seconds // 60, seconds % 60), inline=True)
        await ctx.send(embed=embed)
        """

    #######################################################################################################################

    @commands.command(name="lyrics")
    async def lyrics_command(self, ctx, name: t.Optional[str]):
        player = self.get_player(ctx)
        name = name or player.player_track.title

        async with ctx.typing():
            async with aiohttp.request("GET", LYRICS_URL + name, headers={}) as r:
                if not 200 < r.status < 299:
                    raise NoLyricsFound

                data = await r.json()

                if len(data["lyrics"]) > 2000:
                    return await ctx.send(f"<{data['links']['genius']}>")

                embed = discord.Embed(
                    title=data["title"],
                    description=data["lyrics"],
                    colour=ctx.author.colour,
                    timestamp=dt.datatime.uncnow(),
                )
                embed.set_thumbnail(url=data["thumbnail"]["genius"])
                embed.set_author(name=data["author"])
                await ctx.send(embed=embed)

    @lyrics_command.error
    async def lyrics_command_error(self, ctx, exc):
        if isinstance(exc, NoLyricsFound):
            await ctx.send("No Lyrics could be found.")

    @commands.command(name="join")
    async def join_command(self, ctx: Context):
        if ctx.author.voice is None:
            await ctx.send("Please connect to a voice channel")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(name="undo")
    async def undo_command(self, ctx):
        vc = ctx.voice_client

        if not vc.is_connected():
            await ctx.send("What did you think i can undo?")

        if vc.is_playing():
            vc.pause()
        else:
            vc.resume()

    @commands.command(name="pause")
    async def qause_command(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.pause()
        await ctx.send("paused")
        print("paused")

    @commands.command(name="resume")
    async def resume_command(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client
        voice_channel.resume()
        await ctx.send("resumed")
        print("resumed")

    @commands.command(name="stop")
    async def stop_command(self, ctx):
        player = self.get_player(ctx)
        player.stop()

    @commands.command(name="skip")
    async def skip_cpmmand(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel",
                                  color=discord.Color.green())
            return await ctx.send(embed=embed)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        player = self.get_player(ctx)
        player.skip()

    @commands.command(name='now', aliases=['np', 'currentsong'],
                      description="shows the current playing song")
    async def now_playing_(self, ctx):
        # Display information about the currently playing song.
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title="", description="I'm not connected to a voice channel",
                                  color=discord.Color.green())
            return await ctx.send(embed=embed)

        player = self.get_player(ctx)
        if not player.current:
            embed = discord.Embed(title="", description="I am currently not playing anything",
                                  color=discord.Color.green())
            return await ctx.send(embed=embed)

        seconds = int(vc.source.data["duration"]) % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        if hour > 0:
            duration = "%dh %02dm %02ds" % (hour, minutes, seconds)
        else:
            duration = "%02dm %02ds" % (minutes, seconds)

        embed = discord.Embed(title="",
                              description=f"[{vc.source.data['title']}] [{vc.source.requester.mention}] | `{duration}`",
                              color=discord.Color.green())
        embed.set_author(icon_url=self.bot.user.avatar_url, name=f"Now Playing 🎶")
        await ctx.send(embed=embed)


def setup(bot: BobbyBot):
    bot.add_cog(Music(bot))
