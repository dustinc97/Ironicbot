import asyncio
import os

from azure.storage.blob import BlockBlobService

member_dict = {
    'twice': {'momo': 0, 'sana': 0, 'dahyun': 0, 'mina': 0, 'nayeon': 0, 'jeongyeon': 0,
              'chaeyoung': 0, 'jihyo': 0, 'tzuyu': 0},
    'redvelvet': {'wendy': 0, 'joy': 0, 'irene': 0, 'seulgi': 0, 'yeri': 0}
}

azure_account_name = os.environ.get('AZURE_ACCOUNT_NAME')
azure_account_key = os.environ.get('ACCOUNT_KEY')


async def load_azure():
    block_blob_service = BlockBlobService(account_name=azure_account_name,
                                          account_key=azure_account_key)

    groups = ['twice', 'redvelvet']

    for group in groups:
        for member in member_dict[group]:
            generator = block_blob_service.list_blobs(group, prefix=member)
            count = 0

            for blob in generator:
                count += 1

            member_dict[group][member] = count

    await asyncio.sleep(100)
