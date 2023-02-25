#========================================================================
#                                                                       #
#       This program catalogs tasks of its users into a list            #
#       that is stored in a txt file.                                   #
#       Users can see all tasks and their own tasks which they can      #
#       reassign to another user or mark as complete                    #
#       Admin can also add new users, generate reports and see          #
#       statistics.                                                     #
#                                                                       #
#=======================================================================#


#========================[IMPORTING LIBRARIES]===========================


from datetime import datetime

import textwrap


#====================[VERIFYING AND CREATING FILES]======================


# The following two files supposed to be available in the same directory 
# as the program:

# user.txt
# tasks.txt

# The following block declares placeholder variables to store data from
# files user.txt and tasks.txt for further manipulation so the files not
# need to be kept open.
users = None
tasks = None

# The following block checks whether file user.txt exists in the directory
# and if not, gives options to upload an existing file or create a new one.
# Data from the file are stored in variable called users.
while True:
    try:
        with open("user.txt", "r") as file:
            users = file.readlines()
            break
    except FileNotFoundError:
        output = "───────────────────────────────────────────────────────────\n"
        output += "This program requires a file user.txt\n"
        output += "\n"
        output += "The file user.txt not found!\n"
        output += "\n"
        output += "You have the following options:\n"
        output += "\n"
        output += "1   -   Upload existing user.txt file, retrieving your data\n"
        output += "2   -   Create a new user.txt file\n"
        output += "───────────────────────────────────────────────────────────"
        print(output)

        while True:
            selection = input("Please, select option  1 or 2: ")
            if selection == "1":
                break
            elif selection == "2":
                with open("user.txt", "w+") as file:
                    file.write("admin, adm1n")
                    output = "──────────────────────────────────────\n"
                    output += "File user.txt was succesfully created!\n"
                    output += "\n"
                    output += "     You are new admin\n"
                    output += "\n"
                    output += "Your username is:   admin\n"
                    output += "Your password is:   adm1n\n"
                    output += "──────────────────────────────────────\n"
                    print(output)
                    break
            else:
                print("You have entered incorect characters!")
                continue        

# The following block checks whether file tasks.txt exists in the directory
# and if not, gives options to upload an existing file or create a new one.
# Data from existing file are stored in variable called tasks.
while True:
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            break
    except FileNotFoundError:
        output = "────────────────────────────────────────────────────────────\n"
        output += "This program requires a file tasks.txt\n"
        output += "\n"
        output += "The file tasks.txt not found!\n"
        output += "\n"
        output += "You have the following options:\n"
        output += "\n"
        output += "1   -   Upload existing tasks.txt file, retrieving your data\n"
        output += "2   -   Create a new tasks.txt file\n"
        output += "────────────────────────────────────────────────────────────"
        print(output)
        
        while True:
            selection = input("Please, select option  1 or 2: ")
            if selection == "1":
                break
            elif selection == "2":
                with open("tasks.txt", "w+") as file:
                    print("File tasks.txt was succesfully created!\n")
                    break
            else:
                print("You have entered incorect characters!")
                continue        


#============================[LOGIN SECTION]=============================


# The following block declares placeholder variables for username verification.
username = None
password = None
user_test = None

# The following block reads user input of a username and compares it to the
# first position of each list in variable users, saved from file user.txt and 
# searches for a matching record of existing usernames. If found, it stores
# both values (username and password into the placeholder variables above.) 
while True:
    login = input("\nEnter username: ")
    for user in users:
        user_test = user
        user_test = user_test.split(", ")
        if login == user_test[0]:
            username = user_test[0]
            password = user_test[1]

    if username != None:
        break
    else:
        print("Entered username does not exist!\n")
        continue


# The following block reads in user input and compares it to the value of 
# variable called password. If a match, correct password was entered as per
# the records in user.txt.
while True:
    password_input = input("\nEnter your password: ")
    if password_input == password:
        print("You're in!\n")
        break
    else:
        print("You have entered incorect password! Try again.\n")
        continue

# The following block erase placeholder variables for username verification as
# this step is now completed and the data are no longer needed.
# The variables will be used for further work with the files.
password = None
user_test = None


#==================[OWN FUNCTIONS FOR MENU SELECTIONS]===================


#==========[NEW USER]============

# The following function registers a new user.
def reg_user(x):
    x = None
    # The following block reads in user input of a new user username and 
    # validates whether it already exists and it is a single word of at 
    # least 4 characters.
    while True:
        username_reg = input("Create a new username:\n")
        username_reglen = username_reg.split()
        task_user = username_reg
        task_username = None

        with open("user.txt", "r") as file:
            users = file.readlines()

        for user in users:
            user_test = user
            user_test = user_test.split(", ")
            if task_user == user_test[0]:
                task_username = user_test[0]

        if len(username_reglen) > 1:
            print("\nUsername can only be a single word, no spaces!\n")
            continue
        elif len(username_reg) < 4:
            print("\nUsername must be at least 4 characters long!\n")
        elif task_username != None:
            print("\nEntered username already exists!\n")
            continue
        else:
            break
    print("")

    # The following block reads in user input of a new user password and 
    # validates it is a single word of at least 5 characters and with 
    # at least one number, then double checks the entry and stores the 
    # value in placeholder variable called password.
    print("""Password must be a single word of at least 5 characters
and must contain at least one number\n""")
    while True:
        password_reg = input("Choose new password:\n")
        password_reglen = password_reg.split()
        if len(password_reglen) > 1:
            print("Password can only be a single word, no spaces!\n")
            continue
        elif any(chr.isdigit() for chr in password_reg) is False:
            print("Password must contain at least one number!\n")
            continue
        elif len(password_reg) < 5:
            print("Password must be at least 5 characters long!\n")
        else:
            password_ver = input("\nRe-enter your password:\n")
            if password_reg != password_ver:
                print("Your entry does not match! Try again.\n")
                continue
            else:
                password = password_ver
                break

    # The following block generates a list entry containing the new user
    # username and password before it is added to the file user.txt
    # it verifies whether there is any entry in the file already and 
    # modifies the appropriate output.
    with open("user.txt", "r") as file:
        user_test = file.readlines()
        user_len = len(user_test)
        if user_len == 0:
            adding_user = username_reg + ", " + password
        else:
            adding_user = ", \n" + username_reg + ", " + password

    # The following block append the new user credentials in the file
    # user.txt
    with open("user.txt", "a+") as file:
        file.write(adding_user)
        print("\nNew user succesfully created\n")


#========[ADD TASK]==========
    
# The folowing function adds task.
def add_task(x):
    x = None
    # The following block declares placeholder variables for clarity, which
    # will be used in this block to store input data for manipulation.
    task_username = None
    task_title = None
    task_description = None
    task_duedate = None
    task_currentdate = None

    # The following block reads in user input of a username of the user for
    # whom a task supposed to be assigned, and verifies whether the username
    # exists by comparing records in a file called user.txt. If yes, it stores
    # the username in a variable called task_username.

    while True:
        task_user = input("\nEnter a username of the person whom the task is assigned to:\n")
        with open("user.txt", "r") as file:
            users = file.readlines()
        
        for user in users:
            user_test = user
            user_test = user_test.split(", ")
            if task_user == user_test[0]:
                task_username = user_test[0]

        if task_username != None:
            break
        else:
            print("Entered username does not exist!\n")
            continue
    
    # The following block resets the placeholder variables used in the
    # blocks above as the data are no longer needed.
    users = None
    user_test = None
    task_user = None

    # The following block reads in user input of the rest of the tasks for
    # adding a task, and save data to relevant placeholder variable above.
    while True:
        task_title = input("\nEnter the title of the task:\n")
        if len(task_title) > 35:
            print("\nThe task title max length is 35 characters!")
            continue
        else:
            break
    
    task_description = input("\nEnter the description of the task:\n")

    # The following block reads in a current date, store it in a variable 
    # called now and converts its format into a variable called test_currentdate 
    # for further input validation.
    now = datetime.now()
    task_currentdate = now.strftime("%d %b %Y")
    task_currentdate = datetime.strptime(task_currentdate, "%d %b %Y")

    # The following block reads in user input of the due date for the task,
    # validates its format and that it is a future date, then formats correctly
    # the upper case of the month and stores it in a variable called task_duedate.
    while True:
        date_test = input("\nEnter a task due date in the format (DD Mmm YYYY):\n").lower()

        try:
            if datetime.strptime(date_test, "%d %b %Y"):
                pass
        except ValueError:
            print("""You have entered invalid format! Should be DD Mmm YYYY
e.g: 01 Jan 2000""")
            continue
        
        if len(date_test) == 11:
            date_test = date_test.replace(date_test[3], date_test[3].upper())
        if len(date_test) == 10:
            date_test = date_test.replace(date_test[2], date_test[2].upper())
        
        date_test1 = datetime.strptime(date_test, "%d %b %Y")
        if date_test1 <= task_currentdate:
            print("The task due date must be a future date!")
            continue
        else:
            break
    
    task_duedate = date_test
    task_currentdate = now.strftime("%d %b %Y")

    # The following block verifies whether there is a record in the file
    # already and modifies the output accordingly, then appends the data 
    # from placeholder variables (the new task data) to the file called tasks.txt.
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        tasks_len = len(tasks)
    with open("tasks.txt", "a+") as file:
        if tasks_len == 0:
            file.write(f"{task_username}, {task_title}, {task_description}, {task_currentdate}, {task_duedate}, No")
        else:
            file.write(f", \n{task_username}, {task_title}, {task_description}, {task_currentdate}, {task_duedate}, No")
    
    print("\nTask recorded!\n")
    
    # The following block displays the entered data for clarity.
    output = "─────────────────────────────────────────────────────\n"
    output += f"Task:           {task_title}\n"
    output += f"Assigned to:    {task_username}\n"
    output += f"Date assigned:  {task_currentdate}\n"
    output += f"Due Date:       {task_duedate}\n"
    output += f"Task Complete?  No\n"
    output += f"Task Description:\n{textwrap.fill(task_description, 53)}\n"
    output += "─────────────────────────────────────────────────────\n"
    print(output)
    print("")


#=======[VIEW ALL TASKS]========

# The following function shows all tasks.
def view_all(x):
    x = None
    # The folowing block reads in data from a file called tasks.txt and
    # stores them in a variable called task_list.
    with open("tasks.txt", "r") as file:
        tasks_list = file.readlines()

    # The following block splits the list of all entries in tasks_list into
    # separate lines lists, and prints each line/task in a numerated table format.
    print("\nThe list of all tasks:\n")
    for pos, line in enumerate(tasks_list):
        split_list = line.split(", ")
        output = f"─────────────────────────[{pos + 1}]─────────────────────────\n"
        output += f"Task:           {split_list[1]}\n"
        output += f"Assigned to:    {split_list[0]}\n"
        output += f"Date assigned:  {split_list[3]}\n"
        output += f"Due Date:       {split_list[4]}\n"
        output += f"Task Complete?  {split_list[5]}\n"
        output += f"\n"
        output += f"Task Description:\n{textwrap.fill(split_list[2], 53)}\n"
        output += "─────────────────────────────────────────────────────\n"
        output += ""
        print(output)
    print("\nTask completed!\n")


#=======[VIEW MINE TASKS]========

# The following function shows mine tasks.
def view_mine(x):
    x = None
    # The following block reads in data from a file called tasks.txt and
    # stores them in a variable called task_list.
    with open("tasks.txt", "r") as file:
        tasks_list = file.readlines()

    # The following block splits the list of all entries in tasks_list into
    # separate lines lists, compares the first position of each entry against 
    # current username and prints each line/task for that user in a numerated 
    # table format. It keeps track of task numbers assigned to the user.
    print(f"\nThe list of tasks of user {username}:\n")
    pos_mine = 1
    pos_all = 1
    mine_tasks = []
    for line in tasks_list:
        split_list = line.split(", ")
        if split_list[0] != username:
            pos_all += 1
        if split_list[0] == username:
            output = f"────────────────[Your task number {pos_mine}]─────────────────\n"
            output += "\n"
            output += f"Task number:    {pos_all}   [Catalogue number of all tasks]\n"
            output += f"Task:           {split_list[1]}\n"
            output += f"Assigned to:    {split_list[0]}\n"
            output += f"Date assigned:  {split_list[3]}\n"
            output += f"Due Date:       {split_list[4]}\n"
            output += f"Task Complete?  {split_list[5]}\n"
            output += f"\n"
            output += f"Task Description:\n{textwrap.fill(split_list[2], 53)}\n"
            output += "─────────────────────────────────────────────────────\n"
            output += ""
            print(output)
            pos_mine += 1
            pos_all += 1
            mine_tasks += [pos_all - 1]

    # The following block displays options to manipulate tasks or return to the
    # main menu.
    output = f"──────────[YOU HAVE THE FOLLOWING OPTIONS]───────────\n"
    output += "\n"
    output += f"    Enter the task number to edit tasks\n"
    output += f"    Enter '-1' to return to the main menu\n"
    output += "─────────────────────────────────────────────────────"
    print(output)

    # The following block reads user input of the selection above, validates its
    # format, verify whether the selection is valid/selected tasks exists, and 
    # the task is assigned to the user and returns error messages for invalid inputs.
    while True:
        selection = input("")
        if selection == "-1":
            break
        if selection.isdigit() is False:
            print("\nYou have entered invalid characters!")
            continue
        else:
            selection = int(selection)
            if selection >= pos_all or selection == 0:
                print("\nYou have selected out of range task! Try again.")
                continue
            if selection not in mine_tasks:
                print("\nYou can only edit your onw tasks!")
                continue
            if selection < pos_all:
                break
            else:
                print("\nYou have entered invalid characters!")
                continue

    # The following block executes the menu selection of valid inputs, returns
    # to the main menu or calls access_task function to manipulate tasks.
    if selection == "-1":
        return x
    
    else:
        # The following block displays options for complete/edit the task selected
        # in the VIEW MY TASKS - END OPTIONS and use value stored in variable called 
        # selection as parameter.
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        # The following block breaks the data in variable called tasks into lines.
        lines = []
        for line in tasks:
            line = line.split(",\n")
            lines += line

        # The following block extracts from the list the line corresponding with 
        # the user choice of task for editing stored in variable called selection
        # and displays it for clarity before further manipulation of the file.
        selected_line = [lines[selection - 1]]

        sel_line_list = []
        for line in selected_line:
            line = line.split(",")
            sel_line_list += line

        output = "─────────────[TASK YOU GOING TO EDIT]────────────────\n"
        output += "\n"
        output += f"Task number:     {selection}\n"
        output += f"Task:           {sel_line_list[1]}\n"
        output += f"Assigned to:     {sel_line_list[0]}\n"
        output += f"Date assigned:  {sel_line_list[3]}\n"
        output += f"Due Date:       {sel_line_list[4]}\n"
        output += f"Task Complete?  {sel_line_list[5]}\n"
        output += f"\n"
        output += f"Task Description:\n{textwrap.fill(sel_line_list[2], 53)}\n"
        output += "─────────────────────────────────────────────────────\n"
        output += ""
        print(output)
        

        #=====[TASK COMPLETE CONFIRMATION NESTED FUNCTION]====

        # The following function verifies whether a task can be marked as 
        # complete and gives a confirmation option.
        def comp_confirm(x):
            x = None
            print("You have selected 'c' to mark the task as complete!")
            if sel_line_list[5] != " No":
                print("The task is already marked as complete!")
                return x
            if sel_line_list[5] == " No":
                print("The task can be marked as complete. Do you want to proceed? Y/N:")
                while True:
                    next_choice = input("\n").lower()
                    if next_choice == "n":
                        return x
                    if next_choice == "y":
                        mark_complete(1)
                        print("\nYour selected task succesfully marked as complete!\n")
                        break
                    else:
                        print("\nYou have selected invalid characters! Try again.")
                        continue


        #========[TASK MARK COMPLETE NESTED FUNCTION]=========

        # The following function executes the user task mark as complete request by
        # copying relevant data from global variables, change the value in pos[5]
        # in the task/line, convert the list into string and inserts it into a correct
        # position in the list of tasks, then converts it into a string and rewrite 
        # the document.
        def mark_complete(x):
            x = None

            global adjust_line
            global all_lines

            adjust_line = sel_line_list
            all_lines = lines
            adjust_line[5] = " Yes"
            adjust_line = ",".join(adjust_line)
            all_lines[selection - 1] = adjust_line
            all_lines_str = ""

            for line in all_lines:
                all_lines_str += line

            with open("tasks.txt", "w") as file:
                file.write(all_lines_str)
            
            return x


        #=============[EDIT TASK NESTED FUNCTION]=============
        
        # The following function executes the user edit task request.
        def edit_task(x):
            x = None
            # The following block verifies whether a task selected by user can be
            # edited by checking whether it is marked as complete or not.
            if sel_line_list[5] == " No" or sel_line_list[5] == "No":
                pass
            else:
                print("\nThe task is marked as complete and cannot be edited!")
                return x
        

            #========[NESTED FUNCTION TO CHANGE TASK USER]========

            # The following function changes user assigned to a task.
            def change_user(x):
                x = None

                # The following block declares placeholder variables for clarity, which
                # will be used in this block to store input data for manipulation.
                global current_user_test
                current_user_test = sel_line_list
                task_username = None

                # The following block reads in user input of a username of the user for
                # whom a task supposed to be reassigned, and verifies whether the username
                # exists by comparing records in a file called user.txt. If yes, it also 
                # compares whether it is the username of the current user, then stores
                # the username in a variable called task_username.
                while True:
                    task_user = input("\nEnter a username of the person to whom you wish to reassign the task:\n")
                    with open("user.txt", "r") as file:
                        users = file.readlines()
                    
                    for user in users:
                        user_test = user
                        user_test = user_test.split(", ")
                        if task_user == user_test[0]:
                            task_username = user_test[0]


                    if task_username == current_user_test[0]:
                        print("The task is already assigned to this user")
                        break
                    elif task_username != None:
                        break
                    else:
                        print("Entered username does not exist!\n")
                        continue

                if task_username == current_user_test[0]:
                    return x
                
                # The following block reassigns the task to a new user and rewrites the 
                # record in 'tasks.txt' file.
                else:
                    if task_username != current_user_test[0]:
                        global adjust_line
                        global all_lines
                        adjust_line = sel_line_list
                        all_lines = lines
                        adjust_line[0] = task_username
                        adjust_line = ",".join(adjust_line)
                        all_lines[selection - 1] = adjust_line
                        all_lines_str = ""

                        for line in all_lines:
                            all_lines_str += line

                        with open("tasks.txt", "w") as file:
                            file.write(all_lines_str)

                print(f"\nTask successfully reassigned to user {task_username}")      
                return x

                
            #======[NESTED FUNCTION TO CHANGE TASK DUE DATE]======

            # The following function changes task due date.
            def change_duedate(x):
                x = None
                # The following block declares placeholder variables for clarity, which
                # will be used in this block to store input data for manipulation.
                global new_task_duedate
                new_task_duedate = None
                task_currentdate = None

                # The following block reads in a current date, store it in a variable 
                # called now and converts its format into a variable called test_currentdate 
                # for further input validation.
                now = datetime.now()
                task_currentdate = now.strftime("%d %b %Y")
                task_currentdate = datetime.strptime(task_currentdate, "%d %b %Y")

                # The following block reads in user input of the due date for the task,
                # validates its format and that it is a future date, then formats correctly
                # the upper case of the month and stores it in a variable called new_task_duedate.
                while True:
                    date_test = input("\nEnter a new task due date in the format (DD Mmm YYYY):\n").lower()

                    try:
                        if datetime.strptime(date_test, "%d %b %Y"):
                            pass
                    except ValueError:
                        print("""You have entered invalid format! Should be DD Mmm YYYY
            e.g: 01 Jan 2000""")
                        continue
                    
                    if len(date_test) == 11:
                        date_test = date_test.replace(date_test[3], date_test[3].upper())
                    if len(date_test) == 10:
                        date_test = date_test.replace(date_test[2], date_test[2].upper())
                    
                    date_test1 = datetime.strptime(date_test, "%d %b %Y")
                    if date_test1 <= task_currentdate:
                        print("The task due date must be a future date!")
                        continue
                    else:
                        break
                
                new_task_duedate = date_test
                task_currentdate = now.strftime("%d %b %Y")

                # The following block changes the due date in the task and inserts it in the 
                # list of all tasks, then rewrites the file 'tasks.txt'.
                global adjust_line
                global all_lines
                adjust_line = sel_line_list
                all_lines = lines
                adjust_line[4] = " " + new_task_duedate
                adjust_line = ",".join(adjust_line)
                all_lines[selection - 1] = adjust_line
                all_lines_str = ""

                for line in all_lines:
                    all_lines_str += line

                with open("tasks.txt", "w") as file:
                    file.write(all_lines_str)

                print(f"\nTask due date successfully changed to {new_task_duedate}")      
                return x


            #====[NESTED FUNCTION TO CHANGE TASK USER AND DUE DATE]====

            # The following function combines change_user() and change_duedate() functions.
            def change_user_and_duedate(x):
                x = None
                change_user(1)
                change_duedate(1)
                return x


            #==================[EDITING TASK SUB-MENU]===================

            # The following block displays options for editing tasks.
            output = f"──────────[YOU HAVE THE FOLLOWING OPTIONS]───────────\n"
            output += "\n"
            output += f"    Enter 'a' to assign the task to another user\n"
            output += f"    Enter 'd' to edit the task due date\n"
            output += f"    Enter 'b' to edit both, the user and due date\n"
            output += f"    Enter '-1' to return to the main menu\n"
            output += "─────────────────────────────────────────────────────"
            print(output)

            # The following block takes user input of the task manipulation choice and 
            # calls relevant nested function to execute the particular choice.
            while True:
                choice = input("").lower()
                if choice == "-1":
                    return x
                if choice == "a":
                    change_user(1)
                    break
                if choice == "d":
                    change_duedate(1)
                    break
                if choice == "b":
                    change_user_and_duedate(1)
                    break
                else:
                    print("\nYou have entered invalid characters! Try again.")
                    continue

            # The following block displays the task as it was adjusted for clarity.
            output = "\n──────────────[TASK CHANGES RECORDED]────────────────\n"
            output += "\n"
            output += f"Task number:     {selection}\n"
            output += f"Task:           {sel_line_list[1]}\n"
            output += f"Assigned to:     {sel_line_list[0]}\n"
            output += f"Date assigned:  {sel_line_list[3]}\n"
            output += f"Due Date:       {sel_line_list[4]}\n"
            output += f"Task Complete?  {sel_line_list[5]}\n"
            output += f"\n"
            output += f"Task Description:\n{textwrap.fill(sel_line_list[2], 53)}\n"
            output += "─────────────────────────────────────────────────────\n"
            output += ""
            print(output)
            
            return x


        #===================[EDITING TASK]====================

        # The following block displays options to mark complete or edit the task.
        output = f"──────────[YOU HAVE THE FOLLOWING OPTIONS]───────────\n"
        output += "\n"
        output += f"    Enter 'c' to mark the task as complete\n"
        output += f"    Enter 'e' to edit the task\n"
        output += f"    Enter '-1' to return to the main menu\n"
        output += "─────────────────────────────────────────────────────"
        print(output)

        # The following block takes user input of the task manipulation choice and 
        # calls relevant nested function to execute the particular choice.
        while True:
            choice = input("").lower()
            if choice == "-1":
                return x
            if choice == "c":
                comp_confirm(1)
                break
            if choice == "e":
                edit_task(1)
                break
            else:
                print("\nYou have selected invalid characters! Try again.")
                continue
                

#======[GENERATE REPORTS]======= 

# The following function generates reports.
def generate_reports(x):
    x = None
    
    #==========[TASKS OVERVIEW REPORT]============
                                                    
    # The following block reads in a file called tasks.txt and stores its data
    # in a variable called tasks_overview.
    with open("tasks.txt", "r") as file:
        tasks_overview = file.readlines()

    # The following line declares a variable with current time for comparison 
    # of due dates below.
    now_time = datetime.now()

    # The following block declares placeholder variables for the counts from 
    # itirations theough the list stored in tasks_overview variable and records
    # relevant data to each placeholder variable.
    rep_pos_all_tasks = 0
    rep_completed_tasks = 0
    rep_uncompleted_tasks = 0
    rep_overdue_tasks = 0
    uncompleted_per = 0
    overdue_per = 0

    # The following block splits the list of all entries in tasks_overview into
    # separate lines list and iterates through the list to extract relevant data
    # for the report to be generated.
    for line in tasks_overview:
        split_tasks = line.split(", ")
        rep_pos_all_tasks += 1
        split_tasks[5] = split_tasks[5].strip("\n")
        split_tasks[5] = split_tasks[5].strip(" ")
        if split_tasks[5] == "Yes":
            rep_completed_tasks += 1
        if split_tasks[5] == "No":
            rep_uncompleted_tasks += 1
            due_date_comp = split_tasks[4]
            due_date_comp = datetime.strptime(due_date_comp, "%d %b %Y")
            if due_date_comp < now_time:
                rep_overdue_tasks += 1

    # The block below is division by zero error fail safe.
    if rep_pos_all_tasks >= 1:    
        uncompleted_per = round((rep_uncompleted_tasks / rep_pos_all_tasks * 100), 0)
        overdue_per = round((rep_overdue_tasks / rep_pos_all_tasks * 100), 0)
    if rep_pos_all_tasks == 0:
        uncompleted_per = 0
        overdue_per = 0

    # The following block displays the results in a user friendly manner.
    day_time = now_time.strftime("%d %b %Y %H:%M:%S")

    output = f"\n──────────────────[TASKS OVERVIEW]───────────────────\n"
    output += "\n"
    output += f"Total number of tasks:              {rep_pos_all_tasks}\n"
    output += f"Tasks completed:                    {rep_completed_tasks}\n"
    output += f"Tasks yet to be completed:          {rep_uncompleted_tasks}\n"
    output += f"Tasks past due:                     {rep_overdue_tasks}\n"
    output += f"\n"
    output += f"Tasks uncompleted in %:             {uncompleted_per}\n"
    output += f"Tasks overdue in %:                 {overdue_per}\n"
    output += f"\n"
    output += f"Report generated:       {day_time}\n"
    output += "─────────────────────────────────────────────────────\n"
    output += ""

    # The following block generates task_overview.txt file and writes in it value 
    # stored in variable called output in the format as outlined above.
    with open("task_overview.txt", "w+", encoding="utf-8") as file:
        file.write(output)


    #==========[USER OVERVIEW REPORT]============

    # The following block reads in user.txt file, extracts each user and stores it 
    # in a new list stored in a variable called users_list.
    users_list = []

    with open("user.txt", "r") as file:
        users_list_file = file.readlines()

    for line in users_list_file:
        line = line.strip()
        line = line.split(", ")
        users_list += [line[0]]

    # The following block iterates over the list of users in users_list and creates
    # a coresponding key in newly generated dictionary called users_dic with 5 * 
    # empty placeholder values per each key, one for each statistics request.
    # An example of the dictionary for clarity is below:
    # users_dic = {user : Number of tasks, % of tasks, completed, uncompleted, overdue}
    users_dic = {}

    for user in users_list:
        users_dic[user] = [0] * 5

    # The following block reads in file tasks.txt and generates a list for each task
    # for further manipulation and stores it in variable called tasks_for_stats_lines.
    with open("tasks.txt", "r") as file:
        tasks_for_stats = file.readlines()

    tasks_for_stats_lines = []
    for line in tasks_for_stats:
        line = line.strip()
        line = line.split("\n")
        tasks_for_stats_lines += [line]

    # The following block break each task into a position per record in the task/
    # breaks each string into records separated with comma.
    number_of_tasks = 0
    tasks_list = []
    for line in tasks_for_stats_lines:
        line = line[0].split(",")
        tasks_list += [line]
        number_of_tasks += 1

    # The following block iterates through the list in tasks_list, and for each 
    # user(that corresponds to one key in dictionary users_dic) compares values
    # in the task records towards criteria in if statements and add values to 
    # the dictionary accordingly.
    now_time = datetime.now()

    for line in tasks_list:
        if line[0] in users_dic:
            users_dic[line[0]][0] += 1
            line[0] = line[0].strip()
            line[4] = line[4].strip()
            line[4] = datetime.strptime(line[4], "%d %b %Y")
            line[5] = line[5].strip(" ")
            line[5] = line[5].strip("\n")

            if line[5] == "Yes":
                users_dic[line[0]][2] += 1
            if line[5] == "No":
                users_dic[line[0]][3] += 1
            if line[5] == "No" and line[4] < now_time:
                users_dic[line[0]][4] += 1

    # The following block iterates through the dictionary in variable called users_dic 
    # and for each key/user compares relevant value position against value in variable
    # called number_of_tasks and the dictionary value[0] to generate percentages for 
    # statistics and adjusts values in each relevant position of the dictionary.
    # The for loop considers division by zero error posibility and rounds results to 
    # 0 decimal places.
    for key, value in users_dic.items():
        if number_of_tasks != 0:
            users_dic[key][1] = round((value[0] / number_of_tasks * 100), 0)
        if users_dic[key][0] != 0:
            users_dic[key][2] = round((value[2] / value[0] * 100), 0)
            users_dic[key][3] = round((value[3] / value[0] * 100), 0)
            users_dic[key][4] = round((value[4] / value[0] * 100), 0)
        if number_of_tasks == 0:
            users_dic[key][1] = 0
        if users_dic[key][0] == 0:
            users_dic[key][2] = 0
            users_dic[key][3] = 0
            users_dic[key][4] = 0

    # The following block generates a header for the report in an output format.
    output_head = "\n──────────────────[USER OVERVIEW]────────────────────\n"
    output_head += "\n"
    output_head += f"Total number of users:              {len(users_list)}\n"
    output_head += f"Total number of tasks:              {number_of_tasks}\n"
    output_head += "\n"
    output_head += "─────────────────[USER STATISTICS]───────────────────\n"
    output_head += ""

    # The following block consolidates the data stored in dictionary in users_dic
    # into an output format.
    output_dic_all = ""
    for key, value in users_dic.items():
        output_dic = ""
        output_dic += f"User:                                   {key}\n"
        output_dic += f"Total tasks assigned:                   {value[0]}\n"
        output_dic += f"Tasks assigned from all tasks in %:     {value[1]}\n"
        output_dic += f"Tasks completion rate in %:             {value[2]}\n"
        output_dic += f"Tasks uncompleted in %:                 {value[3]}\n"
        output_dic += f"Tasks overdue in %:                     {value[4]}\n"
        output_dic += "─────────────────────────────────────────────────────\n"
        output_dic_all += output_dic

    now_time = now_time.strftime("%d %b %Y %H:%M:%S")
    output_time = f"Report generated:           {now_time}\n"

    # The following block generates user_overview.txt file and writes in it values 
    # stored in output variables in the format as above.
    with open("user_overview.txt", "w+", encoding="utf-8") as file:
        file.write(output_head + output_dic_all + output_time)
   
    return x


#=========[STATISTICS]==========

# The following function shows statistics.
def statistics(x):
    x = None
    # NOTE to task assessor:
    # the task brief specifies that the statistics request should read relevant
    # text files and just if they don't exist, to generate them first.
    # This, however, creates an issue that if the reports were generated before
    # any changes to tasks.txt or user.txt, reading from the reports will bring
    # outdated data.
    # For that reason, the statistics always generates the reports for consistency
    # and accuracy.

    # The following line generates tasks overview and user overview reports.
    generate_reports(1)

    # The following block reads in the reports and stores the data in respective
    # variables.
    with open("task_overview.txt", "r", encoding="utf-8") as file:
        task_overview_statistics = file.readlines()
    with open("user_overview.txt", "r", encoding="utf-8") as file:
        user_overview_statistics = file.readlines()

    # The following block iterates through respective variables and generates
    # user friendly output format stored in variables called stats1 and stats2.
    stats1 = ""
    for line in task_overview_statistics:
        stats1 += line

    stats2 = ""
    for line in user_overview_statistics:
        stats2 += line

    # The following block displays the statistics in a user friendly manner.
    output = "\n────────────────────[STATISTICS]─────────────────────\n"
    output += "\n"
    output += f"{stats1}\n"
    output += f"{stats2}\n"
    output += f"                    END OF REPORT\n"
    output += "─────────────────────────────────────────────────────"
    print(output)
    print("")

    return x


#=========[MAIN MENU AND SELECTIONS]===========


# The following block reads in user input of a choice of action from the
# menu below and converts it to lower case.
# admin has an extra options of Registering a user, Generate reports 
# and Display statistics. Each user choice/selection has its own section 
# of code further below.
while True:
    if username == "admin":
        menu = input('''──────────────────────────────────────────
Select one of the following options below:

r   -   Registering a user
a   -   Adding a task
va  -   View all tasks
vm  -   View my tasks
gr  -   Generate reports
ds  -   Display statistics
e   -   Exit
──────────────────────────────────────────
''').lower()
    else:
       menu = input('''──────────────────────────────────────────
Select one of the following options below:

a   -   Adding a task
va  -   View all tasks
vm  -   View my tasks
e   -   Exit
──────────────────────────────────────────
''').lower() 

    #=====[OPTION "r - Registering a user"]======

    # This option is only available to admin and calls reg_user function.
    if menu == "r":
        if username == "admin":
            print("\nYou have selected 'Registering a user'\n")
            reg_user(1)
            # The following line returns back to the main menu.
            continue

        # The following block returns error if "r" choice is selected by
        # non-admin.
        else:
            print("\nYou have made a wrong choice, Please Try again\n")
        

    #=======[OPTION "a - Adding a task"]========

    # This option calls add_task function.
    elif menu == "a":
        print("\nYou have selected 'Adding a task'\n")
        add_task(1)
        # The following line returns back to the main menu.
        continue

    #=======[OPTION "va - View all tasks"]======

    # The following block calls view_tasks() function.
    elif menu == "va":
        view_all(1)
        # The following line returns back to the main menu.
        continue

    #=======[OPTION "vm - View my tasks"]=======

    # The following block calls view_mine() function.
    elif menu == "vm":
        view_mine(1)
        # The following line returns back to the main menu.
        continue


    #=====[OPTION "gr - Generate reports"]======

    # This option is only available to admin and calls generate_reports() function.
    elif menu == "gr":
        if username == "admin":
            generate_reports(1)
            print("\nReport 'TASKS OVERVIEW' succesfully generated.")
            print("Report 'USER OVERVIEW' succesfully generated.")
            print("The reports can be accessed in statistics.\n")
            # The following line returns back to the main menu.
            continue

        # The following block returns error if non-admin selects option "gr".
        else:
            print("\nYou have made a wrong choice, Please Try again\n")


    #====[OPTION "ds - Display statistics"]=====

    # This option is only available to admin and calls statistics() function.
    elif menu == "ds":
        if username == "admin":
            statistics(1)
            # The following line returns back to the main menu.
            continue

        # The following block returns error if non-admin selects option "ds".
        else:
            print("\nYou have made a wrong choice, Please Try again\n")

    #==========[OPTION "e - Exit"]==============

    # Exits the program.
    elif menu == "e":
        print("\nGoodbye!!!\n")
        exit()

    # The following block returns to the main menu if invalid option is selected 
    # by the user.
    else:
        print("\nYou have made a wrong choice, Please Try again\n")


#========================[ END OF PROGRAM ]==============================
# Version 2.0
# Last modified: 03/02/2023
