from base_command import BaseCommand

class Testing(BaseCommand):
    name = "testing"
    description = "Just a command for showing that the bot functions"
    async def run(self, client, message, args):
        await message.channel.send("Just testing dont mind me ")
        return "cumstack"