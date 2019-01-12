import asyncio
import discord
from discord.ext import commands
import platform
from Bot_DB.Mango.database_models import Users
class Misc:

    def __init__(self, client, db_connection):
        self.client = client

    @commands.command(pass_context=True)
    async def versioninfo(self):
        """Gives some info on the Bot."""

        tmp = discord.Embed(title='Bot Version Info', type='rich',
                            description='Python Ver: ' + platform.python_version() + ' | '
                                        + 'Discord.py Ver: ' + discord.__version__ + '\n\n' + 'Ironic Bot Ver: 1.3 Stable\n\n' +
                                        'Created with weeb love by Perfect Irony')

        await self.client.say(embed=tmp)
        await asyncio.sleep(100)

    @commands.command()
    async def joined(self, member : discord.Member):
        """Says when a member joined."""
        await self.client.say('{0.name} joined in {0.joined_at}'.format(member))

    @commands.command()
    async def exp(self, member : discord.Member):
        """Check someone's exp"""
        description = "**{0.name}** has `{1}` exp".format(member, Users.objects(user_id=member.id).get().exp)

        tmp = discord.Embed(description=description)
        tmp.set_thumbnail(url=member.avatar_url)

        await self.client.say(embed=tmp)


