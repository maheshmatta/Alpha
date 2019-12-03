''' This module contains the implementation of the server'''
import asyncio
from server_functions import *
async def handle_echo(reader, writer):
    '''
    Establishes the connection between sender and receive.
    Performs read and write operations.
    The given commands are preprocessed and respective functions are called.
    parameters:
    ---------------
    reader:
        Performs read operation from the stream.
    writer:
        Performs write operation to the stream.
    '''
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        print(f"Received {message} from {addr}")
        message = message.split(' ')
        if 'register' in message:
            message = register(message, addr)
        elif "login" in message:
            message = login(message, addr)
        elif "delete" in message:
            message = delete(message, addr)
        elif "list" in message:
            message = lists(addr)
        elif "create_folder" in message:
            message = create_folder(message, addr)
        elif "write_file" in message:
            message = write_file(message)
        elif "change_folder" in message:
            message = change_folder(message, addr)
        elif "read_file" in message:
            message = read_file(message, addr)
        elif "quit" in message:
            message = "Close the connection"
            try:
                del LSR[addr[1]]
                del DIRE[addr[1]]
                del XAA[addr[1]]
            except KeyError:
                pass
            finally:
                p_a = "".join(str(s) for s in message)
                print(f"Send: {p_a}")
                writer.write(p_a.encode())
                break
        else:
            message = "Wrong Command"
        p_a = "".join(str(s) for s in message)
        print(f"Send: {p_a}")
        writer.write(p_a.encode())

async def main():
    ''' This is the main function that starts the server program.'''
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
