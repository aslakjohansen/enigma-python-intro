import asyncio
from aiohttp import web

async def handler (request):
    method  =         request.method
    path    = '/'+str(request.rel_url)[1:]
    payload =   await request.content.read()
    
    try:
        with open(path) as fo:
            return web.Response(status=200, text=''.join(fo.readlines()))
    except:
        return web.Response(status=500, text=str([method, path]))

async def main(interface, port):
    proto  = web.Server(handler)
    server = await loop.create_server(proto, interface, port)

loop = asyncio.get_event_loop()
asyncio.Task(main('0.0.0.0', 8080))

# enter service loop
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('')
    print('STATUS: Exiting ...')
    loop.close()
    exit(0)

