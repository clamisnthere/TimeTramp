import discord
from discord import Message
from dotenv import load_dotenv
import re
from handler import Handler
from testing import Testing

from os import getenv
import sys

pattern1 = re.compile("\$((\d*[mhdy])*)")
pattern2 = re.compile("(\d*[mhdy])")
class ExtClient(discord.Client):
    

    async def on_ready(self):
        self.handler = Handler(self)
        self.excluded_ids = []
        self.prefix = "$"
        self.handler.register_commands()

        print(f"Pogged in as {self.user}")
    
    async def on_message(self, message: Message):
        #check if user should be excluded
        if message.author.bot:
            return
        if not message.content.startswith(self.prefix):
            return
        if message.author.id in self.excluded_ids:
            message.channel.send("You have been banned from using commands, for more info go fuck yourself")
        
        #split message into component parts
        message_split = message.content.split(" ")
        #take command name
        c_name = message_split[0][1:]
        #split args
        args = message_split[1:]

        #handler.find_and_run command
        result = self.handler.find_and_run(c_name, message, args)

        match result: 
            case "NCF":
                await message.channel.send("That command doesn't exist!")
            case "Errored":
                await message.channel.send("The command errored for some reason!")
            case "Success":
                print(f"{c_name} was ran by {message.author.display_name}")
        
        return