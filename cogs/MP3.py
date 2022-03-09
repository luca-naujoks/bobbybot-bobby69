import asyncio
import datetime
import random

from async_timeout import timeout
import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Context
from bot import BobbyBot

import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.178.32",
  user="bobby",
  password="08Kasper06!By",
  database="krautundrueben",
  port="3306"
)


FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }
class MP3(commands.Cog):
    def __init__(self, bot: BobbyBot):
        self.bot = bot

    @commands.command(name="mp3_output", aliases=["convert", "mp3"])
    async def mp3_converter(self, ctx: Context, *, url):
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
        ytdl = youtube_dl.YoutubeDL(ytdl_options)
        ytdl.download(url)





def setup(bot: BobbyBot):
    bot.add_cog(MP3(bot))