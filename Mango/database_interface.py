import datetime
import math
from random import randint

import mongoengine


class User(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.IntField()


class Users(mongoengine.Document):
    user_id = mongoengine.IntField(unique=True)
    exp = mongoengine.LongField()
    multiplier = mongoengine.IntField(min_value=1, max_value=3, default=1)
    time_stamp = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    level = mongoengine.IntField(default=1,min_value=1)

class Custom_Command(mongoengine.EmbeddedDocument):
    command_name = mongoengine.StringField(max_length=20, unique=True)
    response = mongoengine.StringField(max_length=140)

class Guilds(mongoengine.Document):
    guild_id = mongoengine.IntField(unique=True)
    custom_commands = mongoengine.EmbeddedDocumentListField(Custom_Command)
    mod_channel = mongoengine.IntField(unique=True)
    disabled_channels = mongoengine.ListField(field=mongoengine.IntField(unique=True))

async def add_exp(message, client):

    if message.author is not client.user:
        try:
            author_id = message.author.id

                # Get the user's info from the DB
            user_entry = Users.objects(user_id=author_id).get()
            current_exp = user_entry.exp

                # Get the time since their last message
            elapsedTime = datetime.datetime.utcnow() - user_entry.time_stamp

            if int(elapsedTime.total_seconds()) > 5:

                print('Adding xp')

                level = int(.9 * math.sqrt(current_exp))

                if level == 0:
                        level = 1

                multi = 1

                if int(elapsedTime.total_seconds()) < 600:
                    multi = 2

                if int(elapsedTime.total_seconds()) < 120:
                    multi = 3

                Users.objects(user_id=author_id).modify(upsert=True, new=True, exp=((randint(10, 30)*multi) + current_exp),
                                                            time_stamp=datetime.datetime.utcnow(), level=level)
            else:
                Users.objects(user_id=author_id).modify(upsert=True, new=True, time_stamp=datetime.datetime.utcnow())

        except mongoengine.errors.NotUniqueError:
            pass
        except Exception as error:
            print('\n Something happened while adding EXP to user: ' + str(error))

def add_command(content, client, ctx):

    print(content)
    split_str = content.split(' ', maxsplit=1)

    try:
        guild = Guilds()

        guild = Guilds.objects(guild_id=ctx.guild.id).get()

        guild.custom_commands.append(Custom_Command(command_name=split_str[0], response=split_str[1]))
        guild.save()
        return True

    except Exception as e:
        print(e)
        return e
