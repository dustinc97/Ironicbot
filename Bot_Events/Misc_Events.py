
import discord


from Bot_DB.Azure.Load_Azure import load_azure


class MiscEvents:

    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print('Logged in as ' + self.client.user.name + ' (ID:' + self.client.user.id + ') | Connected to ' + str(
            len(self.client.servers)) + ' servers | Connected to ' + str(len(set(self.client.get_all_members()))) + ' users')

        print('Loading Twice from Azure...', end=' ')
        await load_azure()
        print('Done')

        return await self.client.change_presence(game=discord.Game(name='with bits | $versioninfo'))
