
import discord
import mongoengine
from random import randint
import datetime

from Bot_DB.Azure.Load_Azure import load_azure
from Bot_DB.Mango.database_interface import database_connection
from Bot_DB.Mango.database_models import Users


class MiscEvents:

    def __init__(self, client, database):
        self.client = client
        self.database = database

    async def on_ready(self):
        print('Logged in as ' + self.client.user.name + ' (ID:' + self.client.user.id + ') | Connected to ' + str(
            len(self.client.servers)) + ' servers | Connected to ' + str(len(set(self.client.get_all_members()))) + ' users')

        print('Loading Azure...')
        await load_azure()
        print('Done')

        for member in self.client.get_all_members():
            try:
                Users(user_id=int(member.id), exp=0).save()
            except:
                pass

        return await self.client.change_presence(game=discord.Game(name='with bits | $versioninfo'))

    async def on_member_join(self, member: discord.Member):
        try:
            User_tmp = Users(user_id=int(member.id), exp=0).save()
        except mongoengine.NotUniqueError:
            pass

    async def on_message(self, message: discord.Message):
        try:
            m_author = message.author
            author_id = m_author.id

            user_entry = Users.objects(user_id=author_id).get()
            current_exp = user_entry.exp
            elapsedTime = datetime.datetime.utcnow() - user_entry.time_stamp

            print(elapsedTime.total_seconds())

            if int(elapsedTime.total_seconds()) > 30:
                print("Adding points")
                multi = 1

                if int(elapsedTime.total_seconds()) < 600:
                    multi = 2

                if int(elapsedTime.total_seconds()) < 120:
                    multi = 3

                Users.objects(user_id=author_id).modify(upsert=True, new=True, exp=((randint(10, 30) + current_exp) * multi),
                                                        time_stamp=datetime.datetime.utcnow())

        except mongoengine.NotUniqueError:
            pass
