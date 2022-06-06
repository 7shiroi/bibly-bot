from email import contentmanager
import discord
import os
import requests
import numpy as np

from dotenv import load_dotenv
from discord.ext import commands
from urllib.parse import urlencode, quote

bot = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BIBLE_HEADERS_KEY = os.getenv("BIBLE_HEADERS_KEY")

bibleApi = 'https://api.scripture.api.bible/v1'
bibleHeaders = {"api-key" : BIBLE_HEADERS_KEY}


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    print("Bibly is in " + str(len(bot.guilds)) + " servers.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	if message.content.split()[0] == "bible":
		response = ''

		reference = np.array(message.content.split())
		queryString = {'query' : " ".join(reference[1:])}
		print(urlencode(queryString, quote_via=quote))
		response = requests.request("GET", bibleApi + "/bibles/2dd568eeff29fb3c-02/search?" +urlencode(queryString, quote_via=quote), headers=bibleHeaders)

		print(response.json().get("data").get("passages")[0].get("content"))
		await message.channel.send(response.json().get("data").get("passages")[0].get("content"))

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN)