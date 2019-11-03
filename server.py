''' This module contains the implementation of the server and its functionalities'''
import asyncio
import signal
import os
import time

LSR = {}
DIRE = {}
FI = {}
ROOT = os.getcwd()
XAA = {}
LS = []
signal.signal(signal.SIGINT, signal.SIG_DFL)

def register(cmd,addr):
    '''Register allows a new client to register to the server.
    
    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    if cmd[-1] == "admin":
        path =(f'{ROOT}\\admin.txt')
        f_a = open(path, "r")
        contents = f_a.read()
        contents = contents.split(" ")
        f_a.close()
        q_a = len(contents)
        for i in range(0, q_a):
            if i%2 == 0:
                if cmd[1] == contents[i]:
                    recv = " Username already exists "
                    return recv
                path =(f'{ROOT}\\admin.txt')
                f_a = open(path, "a+")
                f_a.write(cmd[1])
                f_a.write(" ")
                f_a.write(cmd[2])
                f_a.write(" ")
                f_a.close()
                os.mkdir(cmd[1])
                os.chdir(cmd[1])
                DIRE[addr[1]] = {cmd[1]:str(os.getcwd())}
                recv = " Personal folder created "
                return recv
    elif cmd[-1] == "user":
        path =(f'{ROOT}\\user.txt')
        f_a = open(path, "r")
        contents = f_a.read()
        contents = contents.split(" ")
        f_a.close()
        q_a = len(contents)
        for i in range(0, q_a):
            if i%2 == 0:
                if cmd[1] == contents[i]:
                    recv = "  Username already exists "
                    return recv
                path =(f'{ROOT}\\user.txt')
                f_a = open(path, "a+")
                f_a.write(cmd[1])
                f_a.write(" ")
                f_a.write(cmd[2])
                f_a.write(" ")
                f_a.close()
                os.mkdir(cmd[1])
                os.chdir(cmd[1])
                DIRE[addr[1]] = {cmd[1]:str(os.getcwd())}
                recv = " Personal folder created "
                return recv
    else:
        recv = " Invalid privilege entered "
        return recv

def login(cmd, addr):
    '''Login allows a client to login to the server.
    Once logged in, the client will have the user's personal folder as starting point to work with.
    
    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    if cmd[1] not in LS:
        path =(f'{ROOT}\\admin.txt')
        f_a = open(path, "r")
        contents = f_a.read()
        contents = contents.split(" ")
        f_a.close()
        tem = len(contents)
        for i in range(0, tem):
            if i%2 == 0:
                if cmd[1] == contents[i]:
                    if cmd[2] == contents[i+1]:
                        recv = "Login succesful - Admin"
                        LS.append(cmd[1])
                        LSR[addr[1]] = {cmd[1]:"admin"}
                        DIRE[addr[1]] = {cmd[1]:str(os.getcwd())}
                        return recv
                    recv = "Login Unsuccesful - Wrong Password"
                    return recv
                path =(f'{ROOT}\\user.txt')
                f_a = open("user.txt", "r")
                content = f_a.read()
                content = content.split(" ")
                f_a.close()
                tem = len(content)
                if cmd[1] == content[i]:
                    if cmd[2] == content[i+1]:
                        recv = "Login succesful - User"
                        LS.append(cmd[1])
                        LSR[addr[1]] = {cmd[1]:"user"}
                        DIRE[addr[1]] = {cmd[1]:str(os.getcwd())}
                        return recv
                    recv = "Login Unsuccesful - Wrong Password"
                    return recv
                recv = "Username does not exist"
                return recv
    recv = " User already logged in "
    return recv

def delete(cmd, addr):
    '''Delete allows a client with admin priviliges to delete a user from the server.
    Request cannot be done if user is not admin.
    
    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    if LSR[addr].values() == "admin":
        cmd = cmd.split(" ")
        f_a = open("admin.txt", "r")
        temp = f_a.read()
        f_a.close()
        temp = temp.split(" ")
        o_a = len(temp)
        for i in range(0, o_a):
            if LSR[addr].keys() == temp[i]:
                if cmd[2] == temp[i+1]:
                    g_a = open("user.txt", "r")
                    delf = g_a.read()
                    g_a.close()
                    delf = delf.split(" ")
                    w_a = len(delf)
                    for i in range(0, w_a):
                        if delf[i] == cmd[1]:
                            del delf[i]
                            g_a = open("user.txt", "w")
                            g_a.write("")
                            g_a.close()
                            recv = " User deleted "
                            return recv
                        g_a = open("user.txt", "w")
                        g_a.write("")
                        g_a.close()
                        recv = " User name not found "
                        return recv
                    r_a = len(delf)
                    for i in range(0, r_a):
                        g_a = open("user.txt", "a+")
                        g_a.write(delf[i])
                        g_a.write(" ")
                        g_a.close()
                else:
                    recv = "Entered password wrong"
                    return recv
    else:
        recv = " Command cannot be processed due to privilege issues."
        return recv

def lists(addr):
    '''Lists displays all the files in the present working directory of the client.
    
    Parameters:
    -----------------
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    rec = []
    for i in DIRE[addr[1]].keys():
        temp1 = str(DIRE[addr[1]][i])
    Files_a = os.listdir(temp1)
    rec.append(["NAME", "SIZE IN BYTES", "CREATION TIME"])
    for i in Files_a:
        j = os.stat(i)
        rec.append([i, j.st_size, time.ctime(j.st_mtime)])
        p_a = "\n".join(str(s) for s in rec)
    return p_a

def create_folder(cmd, addr):
    '''create_folder creates a new folder in the present working directory of the client.
    Folder cannot be created if the name of folder already exists.

    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    if os.getcwd() == ROOT:
        recv = " folder cannot be created in ROOT folder"
        return recv
    for i in DIRE[addr[1]].keys():
        temp1 = str(DIRE[addr[1]][i])
    Files_a = os.listdir(temp1)
    for i in range(0, len(Files_a)):
        if Files_a[i] == cmd[1]:
            recv = " folder name already exists "
            return recv
    os.mkdir(cmd[1])
    recv = " folder created "
    return recv

def write_file(cmd):
    '''Write data in to the end of the file in current working directory,starting on a new line.
    If no file exists with the given name, a new file is created in the current working directory.
    
    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    '''
    if cmd[1] not in FI.keys():
        FI[cmd[1]] = 1
        if len(cmd) <= 2:
            try:
                f_a = open(cmd[1], "w")
                f_a.write("")
                f_a.close()
                recv = " FIle cleared "
            except PermissionError:
                recv = " Permission denied to access this FIle "
        else:
            try:
                for i in range(2, len(cmd)):
                    f_a = open(cmd[1], "a+")
                    f_a.write(cmd[i])
                    f_a.write(" ")
                    f_a.write("\n")
                f_a.close()
                recv = " FIle writing complete "
            except PermissionError:
                recv = " Permission denied to access this FIle "
        del FI[cmd[1]]
        return recv
    recv = " FIle being used by other user. "
    return recv

def change_folder(cmd, addr):
    '''Move the current working directory to the specified folder residing in the current folder.
    To walk back the previous folder, a name of two dots (..) is provided. 

    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    for i in DIRE[addr[1]].keys():
        temp1 = str(DIRE[addr[1]][i])
    os.chdir(temp1)
    if os.getcwd() == ROOT:
        if cmd[1] == "..":
            recv = " Cant move back from ROOT folder "
            return recv
        else:
            for i in DIRE[addr[1]].keys():
                if i != cmd[1]:
                    if LSR[addr[1]][i] == "admin":
                        if cmd[1] == "admin" or cmd[1] == "user":
                            os.chdir(cmd[1])
                            for i in DIRE[addr[1]].keys():
                                DIRE[addr[1]] = {i:str(os.getcwd())}
                            recv = " Current working DIREctory changed "
                            return recv
                        recv = " Permission denied to access FIle "
                        return recv
                    if cmd[1] == "user":
                        os.chdir(cmd[1])
                        for i in DIRE[addr[1]].keys():
                            DIRE[addr[1]] = {i:str(os.getcwd())}
                            recv = " Current working DIREctory changed "
                            return recv
                    recv = " Permission denied to access FIle "
                    return recv
                os.chdir(cmd[1])
                for i in DIRE[addr[1]].keys():
                    DIRE[addr[1]] = {i:str(os.getcwd())}
                recv = " Current working DIREctory changed "
                return recv
    if cmd[1] == "..":
        os.chdir("..")
        for i in DIRE[addr[1]].keys():
            DIRE[addr[1]] = {i:str(os.getcwd())}
        recv = " Current working DIREctory moved back to previous. "
        return recv
    try:
        os.chdir(cmd[1])
        for i in DIRE[addr[1]].keys():
            DIRE[addr[1]] = {i:str(os.getcwd())}
    except FileNotFoundError:
        recv = " folder not found "
        return recv
    else:
        recv = " Current working DIREctory changed. "
        return recv

def read_file(cmd, addr):
    '''Read data from the file in current working directory and return first hundred characters.
    Each subsequent call by the same client will return the next hundred characters in the file, 
    up until all characters are read. 
    A service request without a name will close the currently opened file from reading.

    Parameters:
    -----------------
    cmd:
        It is the command given by the client to the server.
    addr:
        It is a bundle of the ip address and the port of the client.
    '''
    for i in DIRE[addr[1]].keys():
        user = str(DIRE[addr[1]][i])
    try:
        for j in XAA[user].keys():
            LS.append(str(j))
    except KeyError:
        XAA[user] = {}
    finally:
        if len(cmd) == 1:
            XAA[user] = {}
            recv = "Reading FIle is closed"
            return recv
        else:
            if cmd[1] in LS:
                z = XAA[user][cmd[1]]
                f_a = open(cmd[1], "r")
                temp = str(f_a.read())
                y = list()
                if z+100 <= len(temp):
                    for i in range(z, z+100):
                        y.append(temp[i])
                    p_a = "".join(str(s) for s in y)
                    XAA[user] = {cmd[1]:z+100}
                    return p_a
                else:
                    l = len(temp)
                    for i in range(z, l):
                        y.append(temp[i])
                    p_a = "".join(str(s) for s in y)
                    XAA[user] = {cmd[1]:0}
                    return p_a
            else:
                list_of_Files = os.listdir(os.getcwd())
                if cmd[1] in list_of_Files:
                    y = list()
                    f_a = open(cmd[1], "r")
                    temp = str(f_a.read())
                    if len(temp) > 100:
                        for i in range(0, 100):
                            y.append(temp[i])
                        p_a = "".join(str(s) for s in y)
                        XAA[user] = {cmd[1]:100}
                        return p_a
                    elif len(temp) == 0:
                        recv = " FIle is empty"
                        return recv
                    else:
                        for i in range(0, len(temp)):
                            y.append(temp[i])
                        p_a = "".join(str(s) for s in y)
                        XAA[user] = {cmd[1]:len(temp)}
                        return p_a
                elif cmd[1] == '':
                    XAA[user] = {}
                    recv = "Reading FIle is closed"
                    return recv
                else:
                    recv = "FIle doesn´t exist"
                    return recv
async def handle_echo(reader, writer):
    '''Establishes the connection between sender and receiver and performs read and write operations.
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
            message = register(message,addr)
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
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8080)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
asyncio.run(main())
