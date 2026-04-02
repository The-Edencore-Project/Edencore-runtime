# Edencore Bot
# Represents a single runtime agent that will host an ESM mind.

class Bot:
    def __init__(self, name):
        self.name = name
        self.mind = None

    def load_mind(self, mind):
        self.mind = mind
        print(f"Mind loaded into bot: {self.name}")

    def start(self):
        print(f"Bot {self.name} starting...")

    def stop(self):
        print(f"Bot {self.name} stopping...")