first_choice = ('1: Login \n 2 Register ')
if first_choice == 1:
    
elif first_choice == 2:

else:
    print('wrong choice entered')


print('1: Commands \n 2: Quit')
sel = input('enter your choice: ')
if sel == '1':
    print('''COMMANDS:- 
    -> command - change_folder <name>
    This command move the current working directory in the current folder.
    -> command - list
    This command prints the list of all files and folders in the current working directory.
    -> command - read_file <name>
    This command returns the first 100 characters of the file provided.
    -> command - write_file <name> <input>
    This command writes the data at the end of the file.Here <name> is the name of the file to be edited and <input> is the data need to be added in the file.
    -> command - create_folder <name>
    This command creates a new folder with specified <name> in the current working directory
    -> command - register <username> <password> <privileges>
    This command registers a new user with <privileges> to the server using the <username> and <password> provided.
    -> command - login <username> <password>
    This command helps to login to the server.
    -> command - delete <username> <password>
    This command deletes the user from the server.
    ''')
    command_input = []
    command_input.append(input('Enter the command: '))


elif sel == '2':
    print('logging out')
else:
    print('wrong choice entered')

