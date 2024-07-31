import asyncio
import time as ti
import os
import inspect

async def handle_echo(reader, writer):
    tasks=asyncio.all_tasks()
    for task in tasks:
        print('handling...task.all_tasks() ',end='')
        print(task.all_tasks())
        print('handling... indiv task',end='')
        print(task)
    t=ti.time()
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    # os.system(message) # onlyworks with exit 1

    print(f"{ti.time()-t} server_Received {message!r} from {addr!r}")

    t=ti.time()
    writer.write(data)
    await writer.drain()
    tasks=asyncio.all_tasks()
    for task in tasks:
        print('written ',end='')
        print(task.all_tasks())
    print(f"{ti.time()-t} server_Sent: {message!r}")
    t=ti.time()

    writer.close()
    print(f"{ti.time()-t} server_Closed the connection")
    tasks=asyncio.all_tasks()
    for task in tasks:
        print('closed ',end='')
        print(task)

async def main():
    t=ti.time()
    loop=asyncio.get_running_loop()
    print(loop)
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'{ti.time()-t} server_Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
