import os,time
def register(cmd):
    cmd=cmd.split(' ')
    if cmd[-1]=="admin":
        f=open("admin.txt","r")
        contents=f.read()
        contents=contents.split(" ")
        f.close()
        for i in range(0,len(contents)):
            if i%2==0:
                if cmd[1]==contents[i]:
                    print(" Username already exists")
                else:
                    f=open("admin.txt","a+")
                    f.write(cmd[1])
                    f.write(" ")
                    f.write(cmd[2])
                    f.write(" ")
                    f.close()
                    break
    elif cmd[-1]=="user":
        f=open("user.txt","r")
        contents=f.read()
        contents=contents.split(" ")
        f.close()
        for i in range(0,len(contents)):
            if i%2==0:
                if cmd[1]==contents[i]:
                    print(" Username already exists")
                else:
                    f=open("user.txt","a+")
                    f.write(cmd[1])
                    f.write(" ")
                    f.write(cmd[2])
                    f.write(" ")
                    f.close()
                    break
    else:
        print("Invalid privilege entered.")
def login(cmd):
    cmd=cmd.split(' ')
    f=open("admin.txt","r")
    contents=f.read()
    contents=contents.split(" ")
    f.close()
    for i in range(0,len(contents)):
        if i%2==0:
            if cmd[1]==contents[i]:
                if cmd[2]==contents[i+1]:
                    print("Login succesful - Admin")
                    return("admin")
                else:
                    print("Login Unsuccesful - Wrong Password")
                    break
            else:
                f=open("user.txt","r")
                content=f.read()
                content=content.split(" ")
                f.close()
                for i in range(0,len(content)):
                    if i%2==0:
                        if cmd[1]==content[i]:
                            if cmd[2]==content[i+1]:
                                print("Login succesful - User")
                                return("user")
                            else:
                                print("Login Unsuccesful - Wrong Password")
                                break
            print("Username does not exist")
def change_folder(cmd):
    cmd=cmd.split(" ")
    if cmd[1]=="..":
        os.chdir("..")
        print(os.getcwd())
    else:
        os.chdir(cmd[1])
        print(os.getcwd())
#print(os.getcwd())
'''change_folder("change as")
change_folder("change ..")'''
def read_file(cmd,x):
    user=x
    cmd=cmd.split(" ")
    if cmd[1] in user:
        z=user[cmd[1]]
        fo=open(cmd[1],"r")
        temp=str(fo.read())
        y=list()
        if z+100<=len(temp):
            for i in range(z,z+100):
                y.append(temp[i])
            p="".join(str(s) for s in y)
            print(p)
            inde=z+100
            user={cmd[1]:inde}
            return(user)
        else:
            l=len(temp)
            for i in range(z,l):
                y.append(temp[i])
            p="".join(str(s) for s in y)
            print(p)
            inde=0
            user={cmd[1]:inde}
            return(user)
    else:
        list_of_files = os.listdir(os.getcwd())
        if cmd[1] in list_of_files:
            y=list()
            fo=open(cmd[1],"r")
            temp=str(fo.read())
            for i in range(0,100):
                y.append(temp[i])
            p="".join(str(s) for s in y)
            print(p)
            inde=100
            user={cmd[1]:inde}
            return(user)
        elif cmd[1] == '':
            user={}
            recv = 'reading file is closed'
            print(recv)
            return(user)
        else:
            recv = 'file doesn´t exist'
            print(recv)
            return recv
def delete(cmd, addr):
    ''' hi '''
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
'''x={}
x=read_file("readfile aaa.txt",x)
x=read_file("readfile ",x)
x=read_file("readfile ",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile ",x)'''