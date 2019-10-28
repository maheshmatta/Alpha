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
'''x={}
x=read_file("readfile aaa.txt",x)
x=read_file("readfile ",x)
x=read_file("readfile ",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile aaa.txt",x)
x=read_file("readfile ",x)'''