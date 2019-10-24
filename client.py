print("************** WELCOME TO ALPHA **************")
cmd=[]
while(1):

    ch=int(input("Enter 1 to Register or 2 to Login or 3 to Quit:"))
    if ch==1:
        while(1):
            cnd=input(" To Register to Server Enter the command\n\t- register <username> <password> <privileges> :  ")
            cmd.append(cnd)
            cnd=cnd.split(' ')
            if cnd[0]!="register":
                print(" Wrong command ")
            else:
                #if(call register function in server)==True
                break
        continue
    if ch==2:
        while(1):
            cnd=input(" To Login to Server Enter the command\n\t- login <username> <password> : ")
            cmd.append(cnd)
            cnd=cnd.split(' ')
            if cnd[0]!="login":
                print(" Wrong command ")
            else:
                #call login function in server
                break
        break
    if ch==3:
        while(1):
            cnd=input(" To Quit Enter the command\n\t - quit: ")
            cmd.append(cnd)
            cnd=cnd.split(' ')
            if cnd[0]!="quit":
                print(" Wrong command ")
            else:
                quit()
    else:
        print("Enter valid choice")
def commands():
    print('''********** LIST OF COMMANDS OF SERVER ****************** 
-> command - change_folder <name>
    This command move the current working directory in the current folder.
-> command - list
    This command prints the list of all files and folders in the current working directory.
-> command - read_file <name>
    This command returns the first 100 characters of the file provided.
-> command - write_file <name> <input>
    This command writes the data at the end of the file.\n\tHere <name> is the name of the file to be edited and <input> is the data need to be added in the file.
-> command - create_folder <name>
    This command creates a new folder with specified <name> in the current working directory
-> command - register <username> <password> <privileges>
    This command registers a new user with <privileges> to the server using the <username> and <password> provided.
-> command - login <username> <password>
    This command helps to login to the server.
-> command - delete <username> <password>
    This command deletes the user from the server.\n
********** LIST OF COMMANDS OF CLIENT ******************
-> command - commands
    This command displays all the available commands
-> command - commands issued
    This command displays all the commands sent by user including input.
-> command - commands clear
    This command clears all the commands sent bu the user.
-> command - quit
    This command logout the user.
    ''')
commands()
while(1):
    cnd=input("Enter command:")
    cmd.append(cnd)
    cnd=cnd.split(' ')
    if (len(cnd)==1):
        if cnd[0]=="commands":
            commands()
            continue
        elif cnd[0]=="quit":
            quit()
        else:
            #send the command to server
            break
    else:    
        if cnd[0]=="commands":
            if cnd[1]=="issued":
                print(" LIST OF COMMANDS ")
                for i in range(len(cmd)):
                    print("COMMAND",i+1,":",cmd[i])
                continue
            elif cnd[1]=="clear":
                cmd.clear()
                print("COMMANDS CLEARED")
                continue
        else:
            #send the command to server
            break
