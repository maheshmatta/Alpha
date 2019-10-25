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
