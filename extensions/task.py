import random
from datetime import datetime, timedelta

import discord
from discord.ext import tasks, commands


class TaskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.change_bot_activity.start()
        self.send_message_when_user_no_role.start()

    @tasks.loop(minutes=10.0)
    async def change_bot_activity(self):
        activity = random.choice(self.bot.config["discord"]["bot_activity"])
        await self.bot.change_presence(
            activity=discord.Game(activity), status=discord.Status.online
        )

    @change_bot_activity.before_loop
    async def before_send(self):
        await self.bot.wait_until_ready()

        return

    @tasks.loop(seconds=10)
    async def send_message_when_user_no_role(self):
        """
        When user has no role after a certain amount of time
        Send a PM to tell him to take a role
        """
        for m in self.bot.get_all_members():
            if m.bot == False:
                if (
                    m.joined_at
                    >= datetime.now()
                    - timedelta(days=self.bot.config["user_no_role_reminder"]["days"])
                    and len(m.roles) == 0
                ):
                    await m.send(self.bot.config["user_no_role_reminder"]["message"])


def setup(bot):
    bot.add_cog(TaskCog(bot))
