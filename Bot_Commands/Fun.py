import asyncio
import hashlib
import random
import time
import discord
import re
from discord.ext import commands

from Bot_DB.Azure.Load_Azure import member_dict


class Fun:

    def __init__(self, client, db_connection):
        self.client = client

    async def member_pic(self, member_name, group_name):
        try:
            max_num = member_dict[group_name][str.lower(member_name)]
            member_name = str.lower(member_name)
            image_url = 'https://ironicbot2.azureedge.net/{}/{}/{}.jpg'.format(group_name, member_name,
                                                                               random.randrange(1, max_num))

            messages = ["Literally best girl", "I love you " + member_name + "!", "But does starry know who that is?",
                        "Lets be honest, you love her too", group_name + " just wouldn't be the same"]

            tmp = discord.Embed()
            tmp.set_image(url=image_url)
            tmp.set_footer(text=random.choice(messages))

            await self.client.say(embed=tmp)
        except Exception as exception:
            print("Oops! Something went wrong... " + str(exception))
            await self.client.say("Oops! Something went wrong... " + str(exception))

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def twice(self,ctx, arg):
        """Give it a name, Get a picture."""

        await self.member_pic(arg, 'twice')
        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def redvelvet(self, arg):
        """Give it a name, Get a picture."""
        await self.member_pic(arg, 'redvelvet')

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def nice(self):

        """Just says nice."""

        await self.client.say("Nice.")

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def dab(self, message: discord.Message):

        """Summon Momo to dab on them haters."""

        author = str(self.message.author.mention)

        target = self.message.content[5:]

        if target == '':
            tmp = discord.Embed(description=author + ' DABBED')
        else:
            tmp = discord.Embed(description=author + ' DABBED ON ' + target)

        tmp.set_image(url='https://ironicbot2.azureedge.net/twice/gif/momodab.gif')
        tmp.set_footer(text='Powered by Memes')
        await self.client.say(embed=tmp)

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def karma(self, ctx):

        """Karma comes back to bite ya."""

        author = str(ctx.message.author.mention)

        target = ctx.message.content[7:]

        if target == '':
            tmp = discord.Embed(description="WASTED!")
        else:
            tmp = discord.Embed(description=target + ' is WASTED!')

        tmp.set_image(url='https://ironicbot2.azureedge.net/twice/gif/ezgif-1-073e5fd8fe.gif')
        tmp.set_footer(text='Powered by Memes')
        await self.client.say(embed=tmp)

        await asyncio.sleep(100)

    @commands.command(pass_context=True)
    async def cutecat(self, ctx):

        """Lookit this cutie"""

        tmp = discord.Embed(description="CUTE CAT DETECTED")

        tmp.set_image(url='https://thumbs.gfycat.com/AgileHardtofindBug-small.gif')
        tmp.set_footer(text='Powered by Memes')
        await self.client.say(embed=tmp)

        await asyncio.sleep(100)
