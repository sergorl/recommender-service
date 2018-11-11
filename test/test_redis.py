import asyncio
import os
from aredis import StrictRedis


async def example():
    client = StrictRedis(host='127.0.0.1', port=6379, db=0)
    await client.flushdb()
    await client.set('foo', 1)
    assert await client.exists('foo') is True
    await client.incr('foo', 100)

    assert int(await client.get('foo')) == 101
    await client.expire('foo', 10)

    await client.incr('foo', 100)

    # await asyncio.sleep(0.1)
    # await client.ttl('foo')
    # await asyncio.sleep(1)
    # assert not await client.exists('foo')


if __name__ == '__main__':

    # os.system('redis-server')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
