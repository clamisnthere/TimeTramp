import discord
from client import ExtClient
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True
load_dotenv("./src/.env")

client = ExtClient(intents = intents)
client.token = os.getenv("TOKEN")
client.run(client.token)

