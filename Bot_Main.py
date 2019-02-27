import logging
import os

import discord
import mongoengine

from discord.ext import commands

from Azure.Load_Azure import load_azure
from Mango.database_interface import add_exp, Users, Guilds, Custom_Command

bot_token = os.environ.get('BOT_TOKEN')

def connect():
    print(' Connecting to MongoDB...')
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')

    mongoengine.connect(db_name,
                        username=db_username,
                        password=db_password,
                        host=db_host)

    print(' Done.\n\n Loading Azure:')
    #load_azure()

    return mongoengine.connection


bot = commands.Bot(description="Ironic Bot by Perfect_Irony#5196", command_prefix="$", pm_help=False)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    guild_id = message.guild.id



    #if str(message).startswith()


    await add_exp(message, bot)

@bot.event
async def on_ready():
    print('Logged in as ' + str(bot.user.name) + ' (ID:' + str(bot.user.id) + ') | Connected to '
            + str(len(bot.guilds)) + ' servers | Connected to ' + str(len(set(bot.get_all_members())))
            + ' users')

    print('Loading users to DB...')
    if Users.objects.count() < len(set(bot.get_all_members())):
        for member in bot.get_all_members():

            try:
                Users(user_id=int(member.id), exp=0).save()
            except mongoengine.errors.OperationError as e:
                pass
            except Exception as e:
                print(e)
    else:
        print('     No new users, skipping.')

    print('Loading guilds to DB...')
    if Guilds.objects.count() < len(set(bot.guilds)):
        for guild in bot.guilds:

            try:
                Guilds(guild_id=int(guild.id), custom_commands=Custom_Command(command_name='foo', response='bar')).save()
            except mongoengine.errors.OperationError as e:
                pass
            except Exception as e:
                print(e)
    else:
        print('     No new guilds, skipping.')

    print('Done.')

    print('Loading guild settings...')

    for guild in bot.guilds:
        pass

    print('Done.')

    print("\nBot is now ready.")
    return await bot.change_presence(activity=discord.Game('with bits | $versioninfo'))

# Run the client using the built-in client.run. Clear restart is redundant, but keeping it just in case.
def run_client(*args, **kwargs):

    while True:
        print('\nConnecting to databases...')
        mongo_connection = connect()
        print("\n\nDone loading databases.\n")

        logging.basicConfig(level=logging.INFO)

        initial_extensions = ['Command_Cogs.Fun',
                              'Command_Cogs.Misc',
                              'Command_Cogs.Moderation']

        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}. error: ' + str(e.with_traceback()))

                bot.load_extension('Bot_Events.Misc_Events')

        try:
            bot.run(bot_token)
        finally:
            bot.clear()
            print('restarting')

run_client()
