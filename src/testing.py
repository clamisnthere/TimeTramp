from base_command import BaseCommand

class Testing(BaseCommand):
    name = "testing"

    def run(self, client, message, args):
        print("testing the command handler")
        return "Errored"