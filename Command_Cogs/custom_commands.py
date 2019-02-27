import discord

from Mango.database_interface import Guilds


async def handle_msg(message: discord.Message):

    commands_list = Guilds.objects(guild_id=message.guild.id).get().custom_commands
    com = message.content.split(' ', maxsplit=1)[0]

    try:
        for command in commands_list:
            if command.command_name == com:
                await message.channel.send(command.response)
                return True
    except KeyError:
        pass
    except Exception as e:

        print('ERROR: ' + str(e))
