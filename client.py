'''This module contains the main file of Client and defines all the functionalities of the client'''
import asyncio
print("**************  WELCOME TO ALPHA CLEINT SERVER FILE MANAGMENT SYSTEM  **************")
CMD = []
async def tcp_echo_client():
    '''This function defines the connection of the client with the server and functionalities.'''
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    message = ''
    while True:
        ch_a = input("Enter 1 to Register or 2 to Login or 3 to Quit:")
        if ch_a == "1":
            cnd = (input("Enter command\n\t- register <username> <password> <privileges> :"))
            CMD.append(cnd)
            cnd = cnd.split(' ')
            if cnd[0] != "register":
                print(" Wrong command ")
            else:
                p_a = " ".join(str(s) for s in cnd)
                message = p_a
                writer.write(message.encode())
                data = await reader.read(100)
                print(f'Received: {data.decode()}')
            continue
        elif ch_a == "2":
            cnd = input("Enter command\n\t- login <username> <password> :")
            CMD.append(cnd)
            cnd = cnd.split(' ')
            if cnd[0] != "login":
                print(" Wrong command ")
            else:
                p_a = " ".join(str(s) for s in cnd)
                message = p_a
                writer.write(message.encode())
                data = await reader.read(100)
                data = data.decode()
                print(f'Received: {data}')
                if "Login succesful - User" in data or "Login succesful - Admin" in data:
                    break
                else:
                    continue
        elif ch_a == "3":
            cnd = input("Enter command\n\t - quit:")
            CMD.append(cnd)
            cnd = cnd.split(' ')
            if cnd[0] != "quit":
                print(" Wrong command ")
                continue
            else:
                message = cnd[0]
                writer.write(message.encode())
                data = await reader.read(100)
                print(f'Received: {data.decode()}')
                quit()
        else:
            data = " Please enter valid choice"
            print(f'Received: {data}')
            continue
    def commands():
        '''This function defines information about all available commands and usage they have.'''
        print('''****************** LIST OF COMMANDS OF SERVER ******************
    -> command - change_folder <name>
        This command move the current working directory in the current folder.
    -> command - list
        This command prints the list of all files and folders in the current working directory.
    -> command - read_file <name>
        This command returns the first 100 characters of the file provided.
    -> command - write_file <name> <input>
        This command writes the data at the end of the file.\n\tHere <name> is the name of the file to be edited and <input> is the data need to be added in the file.
    -> command - create_folder <name>
        This command creates a new folder with specified <name> in the current working directory.
    -> command - register <username> <password> <privileges>
        This command registers a new user with <privileges> to the server using the <username> and <password> provided.
    -> command - login <username> <password>
        This command helps to login to the server.
    -> command - delete <username> <password>
        This command deletes the user from the server.\n
    ********** LIST OF COMMANDS OF CLIENT ******************
    -> command - commands
        This command displays all the available commands.
    -> command - commands issued
        This command displays all the commands sent by user including input.
    -> command - commands clear
        This command clears all the commands sent bu the user.
    -> command - quit
        This command logout the user.
        ''')
    commands()
    while 1:
        cnd = input("Enter command:")
        CMD.append(cnd)
        cnd = cnd.split(' ')
        if len(cnd) == 1:
            if cnd[0] == "commands":
                commands()
                continue
            elif cnd[0] == "quit":
                message = cnd[0]
                writer.write(message.encode())
                data = await reader.read(100)
                print(f'Received: {data.decode()}')
                quit()
            elif cnd[0] == "register" or cnd[0] == "login":
                print("User already logged in")
            else:
                p_a = " ".join(str(s) for s in cnd)
                message = p_a
                writer.write(message.encode())
                data = await reader.read(2048)
                print(f'Received: {data.decode()}')
                continue
        else:
            if cnd[0] == "commands":
                if cnd[1] == "issued":
                    print(" LIST OF COMMANDS ")
                    tem = len(CMD)
                    for i in range(tem):
                        print("COMMAND", i+1, ":", CMD[i])
                    continue
                elif cnd[1] == "clear":
                    CMD.clear()
                    print("COMMANDS CLEARED")
                    continue
            elif cnd[0] == "register" or cnd[0] == "login":
                print("User already logged in")
            elif cnd[0] == "quit":
                message = cnd[0]
                writer.write(message.encode())
                data = await reader.read(100)
                print(f'Received: {data.decode()}')
                quit()
            else:
                p_a = " ".join(str(s) for s in cnd)
                message = p_a
                writer.write(message.encode())
                data = await reader.read(2048)
                print(f'Received: {data.decode()}')
                continue
asyncio.run(tcp_echo_client())
