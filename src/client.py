import discord
from discord import Message
from dotenv import load_dotenv
import re
from handler import Handler
from testing import Testing

from os import getenv
import sys

pattern1 = re.compile("\%((\d*[mhdy])*)")
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
             # check if user provided regex match string $6d
            matches = pattern1.findall(message.content)
            tstamp = int(round(message.created_at.timestamp(), 0))
            
            if len(matches) == 0:
                    return

            for x in matches:
                duration_to_add = 0
                captured_group = x[0]

                groups = pattern2.split(captured_group)
                
                for i, x in enumerate(groups):
                    if not i % 2 == 0:
                        #print(x)
                        if not len(x) >= 2:
                            await message.channel.send("invalid grouping!")
                            break 
                        try:
                            x_as_int = int(x[:-1])
                        except:
                            await message.channel.send("Cannot typecast x into an integer, did you format wrong?")
                            break
                        match x[-1]:
                            case "m":
                                tstamp += x_as_int * 60
                            case "h":
                                tstamp += x_as_int * 3600
                            case "d":
                                tstamp += x_as_int * 24 * 3600
                            case "y":
                                tstamp += x_as_int * 365 * 24 * 3600
                            case _:
                                await message.channel.send("Invalid timestamp format!!!")
                                break
                await message.channel.send(f"<t:{tstamp}> TIMESTAMP")
            return
        else:
            #split message into component parts
            message_split = message.content.split(" ")
            #take command name
            c_name = message_split[0][1:]
            #split args
            args = message_split[1:]

            #handler.find_and_run command
            result = await self.handler.find_and_run(c_name, message, args)

            match result: 
                case "NCF":
                    await message.channel.send("That command doesn't exist!")
                case "Errored":
                    await message.channel.send("The command errored for some reason!")
                case _:
                    print(f"{c_name} was ran by {message.author.display_name}")
        
        return