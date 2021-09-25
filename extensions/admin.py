from datetime import datetime
from dateutil.relativedelta import relativedelta

from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Le bot répond au ping en envoyant pong")
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command(
        help="Envoie un message aux utilisateurs qui sont présents sur le discord depuis plus de X mois"
    )
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def level_up(self, ctx, month: int):
        for m in ctx.guild.members:
            if m.bot == False:
                if m.joined_at <= datetime.now() - relativedelta(months=month):
                    await m.send(self.bot.config["user_level_up_reminder"]["message"])

    @commands.command(help="Reporter un bug")
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def bug(self, ctx):
        await ctx.send(
            "Vous pouvez ouvrir un ticket sur github https://github.com/M0NsTeRRR/dinobot ou me contacter via l'email renseigné sur github"
        )


def setup(bot):
    bot.add_cog(AdminCog(bot))
