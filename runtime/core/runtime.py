# Edencore Runtime - Core Lifecycle
# This file connects all runtime components together.

from runtime.bots.orchestrator import BotOrchestrator
from runtime.bots.bot import Bot
from runtime.esm.loader import ESMLoader
from runtime.mindcore.interface import MindcoreInterface

def start_runtime():
    print("Edencore Runtime starting...")

    # Create components
    orchestrator = BotOrchestrator()
    mindcore = MindcoreInterface()
    loader = ESMLoader()

    # Create a bot
    bot = Bot(name="Alpha")

    # Load a placeholder mind
    mind = loader.load("path/to/mind")

    # Check permission before loading
    if mindcore.check_permission("load_mind"):
        bot.load_mind(mind)

    # Start orchestrator and bot
    orchestrator.start()
    bot.start()

    print("Runtime initialisation complete.")