import random
from datetime import datetime, timedelta

# from io import BytesIO

import discord
from discord.ext import tasks, commands

from utils.pdf import get_events


class TaskCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.change_bot_activity.start()
        self.send_message_when_user_no_role.start()
        self.check_event.start()

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

    @tasks.loop(hours=24)
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

    @tasks.loop(hours=24)
    async def check_event(self):
        # Not implemented in ilovepdf atm
        """
        auth = requests.post(
            f"{self.bot.config['ilovepdf']['base_url']}{self.bot.config['ilovepdf']['auth_endpoint']}",
            data={ "public_key": self.bot.config['ilovepdf']['public_key'] }
        )
        c_task = requests.get(
            f"{self.bot.config['ilovepdf']['base_url']}{self.bot.config['ilovepdf']['start_endpoint']}/extract",
            headers={ "Authorization": f"Bearer {auth.json()['token']}" }
        )
        requests.post(
            f"{self.bot.config['ilovepdf']['base_url']}{self.bot.config['ilovepdf']['upload_endpoint']}",
            params={ "task": c_task.json()["task"],"cloud_file": self.bot.config['event_pdf_link'] },
            headers={ "Authorization": f"Bearer {auth.json()['token']}" }
        )
        g_task = None
        while g_task is None or g_task.json()["status"] in ["TaskWaiting", "TaskProcessing"]:
            g_task = requests.get(
                f"{self.bot.config['ilovepdf']['base_url']}{self.bot.config['ilovepdf']['task_endpoint']}/{c_task.json()['task']}",
                headers={ "Authorization": f"Bearer {auth.json()['token']}" }
            )
            time.sleep(5)

        file = requests.get(
            f"{self.bot.config['ilovepdf']['base_url']}{self.bot.config['ilovepdf']['download_endpoint']}/{c_task.json()['task']}",
            headers={ "Authorization": f"Bearer {auth.json()['token']}" }
        )
        get_events(BytesIO(file.content))
        """
        events = get_events(
            self.bot.config["lyon2_event"]["file"],
            self.bot.config["lyon2_event"]["max_days_to_check"],
        )
        embed = discord.Embed(
            title="Lyon 2 calendrier universitaire",
            description=f"Evénements dans les {self.bot.config['lyon2_event']['max_days_to_check']} prochains jours",
            color=0xFF0000,
        )
        embed.set_footer(
            text=f"Dernière mise à jour le {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"
        )
        for event in events:
            embed.add_field(
                name=event["title"],
                value=f"Du {event['start']} au {event['end']}",
                inline=False,
            )
        for g in self.bot.config["lyon2_event"]["guilds"]:
            channel = self.bot.get_channel(g["channel_id"])
            msg = await channel.fetch_message(g["message_id"])
            await msg.edit(embed=embed, content="")

    @check_event.before_loop
    async def before_check_event(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(TaskCog(bot))
