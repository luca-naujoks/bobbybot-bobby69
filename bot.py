# Bobby Bot code
import discord
from discord.ext import commands

import os


class BobbyBot(commands.Bot):


    def __init__(self, token: str):
        self.token = token
        super().__init__(command_prefix=commands.when_mentioned_or(""),
                         owner_id=528982743623925781,
                         case_insensitive=True,
                         intents=discord.Intents.all())

    def init_cogs(self):

        files = os.listdir("cogs")
        cogs = []
        for f in files:
            if not f.startswith("__"):
                if f.endswith(".py"):
                    cogs.append(f[:-3])

        if not cogs:
            print("Couldn´t find any cogs to load")
        else:
            for cog in cogs:
                print("Load: " + cog)
                try:
                    self.load_extension("cogs." + cog)
                except Exception as e:
                    print("Loading '{}' failed\n{}: {}".format(cog, type(e).__name__, e))







    def run(self):
        self.remove_command("help")
        super().run(self.token)
