import asyncio
import time as t

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'{t.time()} client_Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'{t.time()} client_Received: {data.decode()!r}')

    print(f'{t.time()} client_Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client(f'{t.time()} client_Hello World!'))
