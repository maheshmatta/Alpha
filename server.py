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