import discord
from dotenv import load_dotenv
import re

from os import getenv
import sys

pattern1 = re.compile("\$((\d*[mhdy])*)")
pattern2 = re.compile("(\d*[mhdy])")
class ExtClient(discord.Client):

    async def on_ready(self):
        print(f"Pogged in as {self.user}")
    
    async def on_message(self, message):
        # check if user provided regex match string $6d
        matches = pattern1.findall(message.content)
        tstamp = int(round(message.created_at.timestamp(), 0))
        
        if len(matches) == 0:
                return

        print(f"tstamp before alteration {tstamp}")
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
                            print(f"Adding {x[0]} minutes")
                            tstamp += x_as_int * 60
                        case "h":
                            print(f"Adding {x[0]} hours")
                            tstamp += x_as_int * 3600
                        case "d":
                            print(f"Adding {x[0]} days")
                            tstamp += x_as_int * 24 * 3600
                        case "y":
                            print(f"Adding {x[0]} years")
                            tstamp += x_as_int * 365 * 3600
                        case _:
                            await message.channel.send("Invalid timestamp format!!!")
                            break
        print(f"new timestamp {tstamp}")
        await message.channel.send(f"<t:{tstamp}> TIMESTAMP")