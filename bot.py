import logging
import os

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


class DinoBot(commands.Bot):
    def __init__(self, config):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            command_prefix=config["discord"]["command_prefix"],
            description="DinoBot is a discord bot manager for Lyon 2",
            intents=intents,
        )

        self.root_dir = os.path.dirname(os.path.abspath(__file__))

        self.config = config

    async def on_ready(self):
        logger.info(f"Logged in as: {self.user.name} - {self.user.id}")
        logger.info("Successfully logged in and booted...!")
