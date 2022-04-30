# Bobby Bot code
import discord
from discord.ext import commands

import os
import datetime
import time

client = discord.Client()


class BobbyBot(commands.Bot):

    def __init__(self, token: str):
        self.token = token
        super().__init__(command_prefix=commands.when_mentioned_or(""),
                         owner_id=528982743623925781,
                         case_insensitive=True,
                         intents=discord.Intents.all())

    def init_cogs(self):
        e = ""
        counter = 0
        files = os.listdir("cogs")
        cogs = []
        now = datetime.datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
        for f in files:
            if not f.startswith("__"):
                if f.endswith(".py"):
                    cogs.append(f[:-3])

        if not cogs:
            print("Couldn´t find any cogs to load")
        else:
            for cog in cogs:
                print("Loading Module: " + cog + "")
                try:
                    self.load_extension("cogs." + cog)
                except Exception as e:
                    print("Loading Module: '{}' failed\n{}: {}".format(cog, type(e).__name__, e))
                    counter += 1
        if counter == 0:
            e += "Modules"
        if counter == 1:
            e += "Module"
        if counter > 1:
            e += "Modules"

        print(f"\n----------------------------------------------------------\nLoading complete")
        print("----------------------------------------------------------")
        time.sleep(0.5)
        print(f"\nBasic Bot Systems are running and {counter} {e} Faild to load")
        time.sleep(0.1)
        print(f"\nBobbyBot was successfully logged in at {dt}\n\n")

    def run(self):
        self.remove_command("help")
        super().run(self.token)
