class BaseCommand():
    def __init__(self):
        self.name = ""
    
    def run(self, client, message, args):
        return "This is not a real command, do not register it please, only use this to extend for future commands!"