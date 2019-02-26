import asyncio
import os

import mongoengine
import discord
from discord.ext import commands

from Bot_Commands.Fun import FunCog
from Bot_Commands.Misc import Misc
from Bot_DB.Azure.Load_Azure import load_azure
from Bot_Events.Misc_Events import MiscEvents

import logging



import sys, traceback

bot_token = os.environ.get('BOT_TOKEN')

startup_extensions = ['Fun', 'Misc', 'Moderation', 'Misc_Events']

# Connect to the mongodb using mongoengine

def connect():
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')

    mongoengine.connect(db_name,
                        username=db_username,
                        password=db_password,
                        host=db_host)

    return mongoengine.connection

# Run the client using the built-in client.run
def run_client(*args, **kwargs):

    while True:
        bot = commands.Bot(description="Ironic Bot by Perfect_Irony#5196", command_prefix="$", pm_help=False)

        mongo_connection = connect()
        print('\nLoading Azure:')
        load_azure()

        logging.basicConfig(level=logging.INFO)

        initial_extensions = ['Bot_Commands.Fun',
                              'Bot_Commands.Misc',
                              'Bot_Commands.Moderation']

        for extension in initial_extensions:
            try:
                print('here 1')
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}. error: ' + str(e.with_traceback()))

        bot.add_cog(MiscEvents(bot,mongo_connection))

        try:
            bot.run('NDk0MDE4NTI0MDM4MDM3NTA0.DyFEFA.Qhy5mWCIMBpHbk-bZmunCjidFEM')
        finally:
            bot.clear()
            print('restarting')


run_client()
