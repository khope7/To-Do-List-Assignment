#User Interface (UI):
#Create a command-line interface (CLI) for the To-Do List Application.
#Display a welcoming message and a menu with the following options:
#        Welcome to the To-Do List App!
#
#        Menu:
#        1. Add a task
#        2. View tasks
#        3. Mark a task as complete
#        4. Delete a task
#        5. Quit
#To-Do List Features:
#Implement the following features for the To-Do List:
#Adding a task with a title (by default “Incomplete”).
#Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
#Marking a task as complete.
#Deleting a task.
#Quitting the application.
#User Interaction:
#Allow users to interact with the application by selecting menu options using input().
#Implement input validation to handle unexpected user input gracefully.
#Error Handling:
#Implement error handling using try, except, else, and finally blocks to handle potential issues.
#Code Organization:
#Organize your code into functions to promote modularity and readability.
#Use meaningful function names with appropriate comments and docstrings for clarity.
#Testing and Debugging:
#Thoroughly test your application to identify and fix any bugs.
#Consider edge cases, such as empty task lists or incorrect user input.
#Documentation:
#Include a README file that explains how to run the application and provides a brief overview of its features.
#Optional Features (Bonus):
#If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
#GitHub Repository:
#Create a GitHub repository for your project.
#Commit your code to the repository regularly.
#Include a link to your GitHub repository in your project documentation.


#NOTE: Not sure how to turn this all into a function without breaking the references to earlier Instantiated variables and code, I saw that build request late into my coding, would like to know how if possible
#Aware of how to create a function
#def aware_of_this():
#    stuff = "stuff"
#    print(stuff)
#    return stuff
#
#aware_of_this()

#Thanks for any help


#Writing Code for ToDoListApplication

#Instantiating task_number variable for task number
task_number = 0

#Instantiating ask_again variable for user re-entry
ask_again = bool

#Instantiating full_list before user entry
full_list = ""

#Instantiating added list for list to str conversion outside of loop
added_list = ""

#Instantiating new_tasks variable for additional tasks entered beyond first entry
new_tasks = ""

#Instantiating list outside of loop for concantentation
tasks_list = []

#Instantiating twice variable for new line of print for additional task added
twice = 0

#Creating CLI for the To-Do-List Application
print('''Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit\n''')

#Creating while loop to continue to repeat entire To-Do-List Application until all user enters 'done' from menu
while True:         
#Asking user for choice between 1-5 using try except ValueError to catch for floats and aplha inputs
    while True:
#Created try except to catch for non-entries
        try:
#Created if statement to run operator unique from additional re-entries to avoid full_list str replacement
            if ask_again == bool:
                tried_operator = int(input("Please enter your choice. \nHINT: your choice must be a number between 1 and 5\n"))
#Created nest if else statement to catch for user input outside range of 1-5
                if tried_operator < 1 or tried_operator > 5:
                    print("Apologies, entry must be a number within range.\n\n")
                else:
                    remote_operator = tried_operator
                    break
#Asking for menu choice again only if user has entered first choice
            elif ask_again == True:
                print(f'''\n       Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit\n\n''')
                tried_operator = int(input("Please choose next menu choice or enter '5' to quit: "))
                if tried_operator < 1 or tried_operator > 5:
                    print("Apologies, entry must be a number within range.\n\n")
                else:
                    remote_operator = tried_operator
                    break
        except ValueError:
            print ("Apologies, entry must be a full number between 1 and 5.\n\n")

#Created additional line for spacing for user friendly interface
    print ("")
#Created while loop if statement unique to first entry for if user chooses option 1: 'Add a task' that continues adding tasks until user completes adding tasks
    if remote_operator == 1 and ask_again == bool:
        while True:
#Asks user for Tasks until 'done' is entered
                default_tasks = input("Please enter your tasks or task, type 'done' once complete: ")
#Created user entry list that appends all entries into list and converts to full_list string after done 
                if default_tasks.lower() != 'done':
#Created task number count to account for all tasks entered in loop
                    task_number += 1
#Created variable of user entry to append to tasks_list
                    tasks = (f"{task_number}. {default_tasks.title()} - Incomplete")
                    tasks_list.append(tasks)
                else:
#Converted list to string for add and replace methods
                    added_list = ""

                    for iteration in tasks_list:
                        added_list += iteration + "\n"

#Initiating run check giving the user the option to leave the program at anytime catching y and n
                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        full_list = added_list + full_list
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
#Created else while loop to keep the user in a loop unless specific answers are entered catching all possible entries
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()

#Created while loop for elif of additional tasks created beyond first entry using ask again bool
    elif remote_operator == 1 and ask_again == True:
        while True:
            ask = input("Please enter your tasks or task, type 'done' once complete: ")
            if ask != 'done':
                new_tasks = ask
                task_number += 1
                if twice != 1:
                    new_tasks = f"{task_number}" + ". " + new_tasks.title() + " - Incomplete"
                else:
                    new_tasks = "\n" + f"{task_number}" + ". " + new_tasks.title() + " - Incomplete"
            else:
                operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                    ask_again = True
                    remote_operator = 0
                    twice = 1
                    full_list = full_list + new_tasks
                    break
                elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                    full_list = full_list + new_tasks
                    print(f"\n\n {full_list} \n Thank you for using the To-Do-List Application")
                    exit()
                else:
                    while True:
                        operation_check = input("Apologies, please type 'y' or 'n':")
                        if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                            break
                        elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                            print("\n\nThank you for using the To-Do-List Application")
                            exit()



#Created while loop for next elif to view the full_list as updated from all other options
    elif remote_operator == 2:
        while True:
            print(f"Here is your full list entered: \n{full_list}")
            operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                ask_again = True
                remote_operator = 0
                break
            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                print("\nThank you. Here is your full list of tasks:\n")
                print(full_list)
                print("\n\nThank you for using the To-Do-List Application")
                exit()
            else:
                while True:
                    operation_check = input("Apologies, please type 'y' or 'n':")
                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()

#Created while loop for next elif to ask user to complete any Incomplete defaulted tasks, reprints adusted full_list and asks user for reentry
    elif remote_operator == 3:
        while True:
                replacement_task = input("Which listed item would you like to list as completed?:  please type ('done') to exit")
                replacement_task = replacement_task.title()
                if replacement_task in full_list:
                    new_text = full_list.replace(f"{replacement_task} - Incomplete", f"{replacement_task} - Complete")

                    full_list = new_text

                    print(full_list)
                    print(f"{replacement_task} has been adjusted")

                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\nThank you. Here is your full list of tasks:\n")
                        print(full_list)
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()
#Created 'done' elif to account for reject of first entry
                elif replacement_task == 'done':
                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\nThank you. Here is your full list of tasks:\n")
                        print(full_list)
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()

#Created else statement to catch for any and all entries not within the full_list variable
                else:
                    print("Apologies, entry must be an item you have entered.")

#Created while loop for next elif to remove any items in list and printing
    elif remote_operator == 4:
        while True:
                removed_item = input("Here is your list: \n" f"{full_list}\n\nWhat item from the list would you like removed?: please type ('done') to exit")
#Created variables to catch for both Complete and Incomplete items
                removed_item1 = removed_item.title() + " - Incomplete"
                removed_item2 = removed_item.title() + " - Complete"
#Created if statments to catch, replace, update full_list, and print for both Complete and Incomplete items in full_list
                if removed_item1 in full_list:
                    scratched_item = full_list.replace(f"{removed_item1}", "")

                    full_list = scratched_item

                    print(full_list)
                    print(f"{removed_item.title()} has been adjusted")

                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\nThank you. Here is your full list of tasks:\n")
                        print(full_list)
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()

                elif removed_item2 in full_list:
                    scratched_item = full_list.replace(f"{removed_item2}", "")

                    full_list = scratched_item

                    print(full_list)
                    print(f"{removed_item.title()} has been adjusted")

                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\nThank you. Here is your full list of tasks:\n")
                        print(full_list)
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()

                elif replacement_task == 'done':
                    operation_check = input("\nWould you like to continue? Please type (y/n) for yes or no: ")

                    if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                        ask_again = True
                        remote_operator = 0
                        break
                    elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                        print("\nThank you. Here is your full list of tasks:\n")
                        print(full_list)
                        print("\n\nThank you for using the To-Do-List Application")
                        exit()
                    else:
                        while True:
                            operation_check = input("Apologies, please type 'y' or 'n':")
                            if operation_check.lower() == "yes" or operation_check.lower() == "ok" or operation_check.lower() == "y":
                                break
                            elif operation_check.lower() == "no" or operation_check.lower() == "n" or operation_check.lower() == "no thanks":
                                print("\n\nThank you for using the To-Do-List Application")
                                exit()

                else:
                    print("Apologies, entry must be an item you have entered.")

#Created last elif for option 5 to print fully adjusted list, thank the user and exit the application
    elif remote_operator == 5:
        print (f"Here is your fully adjusted list:\n{full_list}")
        print("\n\nThank you for using the To-Do-List Application")
        exit()