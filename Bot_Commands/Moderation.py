import discord
from discord.ext import commands


class Moderation:
    def __init__(self, client):
        self.client = client

    async def on_message_delete(self, message):
        pass


def setup(client):
    client.add_cog(Moderation(client))
