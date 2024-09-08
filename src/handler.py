from discord import Message
from testing import Testing
from help import Help
from xkcd_c import Xkcd

class Handler():
    def __init__(self, client):
        self.commands = {}
        self.client = client

    def register_command(self, Command):
        self.commands[Command.name] = Command
    
    async def find_and_run(self, command_name: str, message: Message, args: list[str]) -> str:
        if command_name not in self.commands.keys():
            return "NCF"
        
        c = self.commands[command_name]
        try:
            #output is a currently unused variable but sometimes commands may return something
            output = await c.run(self, self.client, message, args)

            #  every command has run method taking arguments handler, client, message, and args
            return output
        except Exception as e:
            print(f"{command_name} errored {str(e)} for {message.author.display_name}")
            return "Errored"

    def register_commands(self):
        self.register_command(Testing)
        self.register_command(Help)
        self.register_command(Xkcd)
        return "Successfully registered all commands"