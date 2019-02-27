import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):

        self.client = client




def setup(bot):
    bot.add_cog(Moderation(bot))
