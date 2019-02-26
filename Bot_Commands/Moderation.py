import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):

        self.client = client

    async def on_message_delete(self, message):
        pass

    # @commands.command()
    # @commands.has_permissions(kick_members=True)
    # async def mute(self, user : discord.User, time : int, reason : str):


def setup(bot):
    bot.add_cog(Moderation(bot))
