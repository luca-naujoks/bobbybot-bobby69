# start datei für BobbyBot
from bot import BobbyBot
from Secrets import BOT_TOKEN

bot = BobbyBot(BOT_TOKEN)
bot.init_cogs()




bot.run()
