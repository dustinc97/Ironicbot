import asyncio
import os

from azure.storage.blob import BlockBlobService
from discord.ext.commands import Bot

from Bot_Commands.Fun import Fun
from Bot_Commands.Misc import Misc
from Bot_Events.Misc_Events import MiscEvents

bot_token = os.environ.get('BOT_TOKEN')

startup_extensions = ['Fun', 'Misc', 'Moderation', 'Misc_Events']


# Run the client using the built-in client.run
def run_client(*args, **kwargs):

    while True:
        client = Bot(description="Ironic Bot by Perfect_Irony#5196", command_prefix="$", pm_help=False)

        client.add_cog(Fun(client))
        client.add_cog(Misc(client))
        client.add_cog(MiscEvents(client))

        client.run(bot_token)

        asyncio.sleep(250)


run_client()
