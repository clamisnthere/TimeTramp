from base_command import BaseCommand

class Help(BaseCommand):
    name = "help"
    description = "Shows all commands that TimeTramp can run!"

    async def run(self, client, message, args):
        help_message = ""

        for x in client.handler.commands.values():
            help_message += f"{client.prefix}{x.name   } : **{x.description}\n**"
        
        
        await message.channel.send(help_message)
        return