#import os module and discord.py that allows access to the Discord API
import os, discord

#import load_dotenv function from dotenv module
from dotenv import load_dotenv

#loads the .env file that resides on the same level as the script
load_dotenv()

#get the token from .env file
token = os.getenv("token")

#gets the Client object from discord.py
intents = discord.Intents.default()
intents.members = True
intents.dm_messages = True
bot = discord.Client(intents=intents)

#event listener for when the bot has switched from offline to online
@bot.event
async def on_ready():
    # creates a counter to keep track of the number of guilds the bot is being connected
    guild_count = 0
    # loops through all the guilds that are connected
    for guild in bot.guilds:
        # print the server's id and name
        print(f"- {guild.id} (name: {guild.name})")
        # increments the guild counter
        guild_count += 1
        
    #prints how many guilds/servers are connected to the bot
    print("SampleDiscordBot is in" + str(guild_count) + " guilds.")

#Event listener for when a new message is received by the channel
@bot.event
async def on_message(message):
    greetings = ["Hi", "hi", "hello", "Hello", "hi there", "Hi", "hey", "Hey", "Hola", "hola"]
    #checks if the message that was sent was equal to "Hello" or similar greetings
    if message.content in greetings:
        #replies with a message
        await message.channel.send("Hi there! How can I help you?")
    #random message
    if message.content == "Tell me about yourself" or message.content == "tell me about yourself":
        #replies with a message
        await message.channel.send("Hello, my name is Bot9078 and I am a Discord Bot that has been put up in MLH_Projects server in Discord by @Sia#4172.")
        await message.channel.send("Do you need any help? I am happy to help you.")

#Executes the bot with the specified token
bot.run(token)