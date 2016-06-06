'''
Created on Jun 6, 2016

@author: eli
'''
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.httpclient import AsyncHTTPClient
import asyncio

# Tell Tornado to use the asyncio eventloop
AsyncIOMainLoop().install()
# get the loop
loop = asyncio.get_event_loop()
# the Tornado HTTP client
http_client = AsyncHTTPClient()

# wrap the Tornado callback in a asyncio.Future
def aio_fetch(client, url, **kwargs):
    fut = asyncio.Future()
    client.fetch(url, callback=fut.set_result, **kwargs)
    return fut

# enjoy
@asyncio.coroutine
def main():
    print("fetching my site")
    mysite = yield from aio_fetch(http_client, "http://pepijndevos.nl/")
    print("my site said", mysite.reason)
    print("hello httpbin")
    httpbin = yield from aio_fetch(http_client, "http://httpbin.org/get?code=%d" % mysite.code)
    print(httpbin.body.decode())

print(loop.run_until_complete(main()))