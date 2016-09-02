#!/usr/bin/env python
# coding:utf-8
import asyncio
import orm
import sys
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop,user='www-data', password='Wd_151617', database='awesome')

    u = User(id=1, name='Test2', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()

if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)