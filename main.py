from email import contentmanager
import discord
import os
import requests

from dotenv import load_dotenv
from discord.ext import commands

bot = discord.Client()

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BIBLE_HEADERS_KEY = os.getenv("BIBLE_HEADERS_KEY")
BIBLE_HEADERS_HOST = os.getenv("BIBLE_HEADERS_HOST")

bibleApi = 'https://ajith-holy-bible.p.rapidapi.com'
bibleHeaders = {"X-RapidAPI-Host" : BIBLE_HEADERS_HOST, "X-RapidAPI-Key" : BIBLE_HEADERS_KEY}

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    print("Bibly is in " + str(len(bot.guilds)) + " servers.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")
	elif message.content.split()[0] == "bible":
		# bible john 3:16
		book = message.content.split()[1]
		chapter = message.content.split()[2].split(':')[0]
		verse = message.content.split()[2].split(':')[1]
		queryParams = {"Book" : book, "chapter" : chapter, "Verse" : verse}
		print(queryParams)
		response = requests.request("GET", bibleApi + "/GetVerseOfaChapter", headers=bibleHeaders, params=queryParams)
		await message.channel.send(response.json().get("Output"))

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run(DISCORD_TOKEN)