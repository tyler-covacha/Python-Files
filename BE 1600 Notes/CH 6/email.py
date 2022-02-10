def menu():
    '''prints menu'''
    
    print("Menu")
    print("----------------------------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit the program")
    print()



def look_up_email(name):
    ''' finds if the name is in the file '''

    name_email = load_emails()

    # if the name is in the file, print the name and its email
    if name in name_email:
        print("Name:", name)
        print("Email:",name_email[name])

    # if the name is not in the file
    else: 
        print("The specified name was not found")

    
    
def add_new_name_email(name, email):
    ''' adds a new name and email '''
    
    name_email = load_emails()

    # if the name is already in the file
    if name in name_email:
        return print("That name already exists")

    # saves the new name and email
    name_email[name] = email
    save_emails(name_email)
    print("Name and address have been added")

    
    
def change_email(name):
    ''' changes the email of the user_input name '''
    
    name_email = load_emails()

    # asks user to change email address
    if name in name_email:
        name_email[name] = input("Enter the new address: ")

    # if the name is not found in the file
    else:
        return print("The specified name was not found")

    # saves the name and its new email
    save_emails(name_email)
    print("Information updated")

        
        
def delete_name_email(name):
    ''' deletes a name and email in the file '''
    
    name_email = load_emails()

    # deletes the name and its email from the file
    if name in name_email:
        del name_email[name]
        save_emails(name_email)
        return print("Information deleted")

    # if the name doesn't exist in the file
    else:
        return print("The specified name was not found")


    
def load_emails():
    ''' writes each name and its email into a dictionary '''

    name_email = {}
    f = open("emails.txt",'r')
    for line in f:
        line = line.split()
        name_email[line[0]] = line[1]
    f.close()
    return name_email


        
def save_emails(name_email):
    ''' takes each name and its email and writes it into the file '''
    
    f = open("emails.txt",'w')
    for key,value in name_email.items():
        f.write("{0} {1} \n".format(key,value))
    f.close()



def main():
    ''' the main function for name and email addresses '''
    
    menu()

    # asks user for choice
    user_input = input("Enter your choice: ")

    # if it's not a valid choice, asks user for choice
    while user_input not in "12345":
        user_input = input("Enter a valid choice: ")

    # if the choice is either 1, 2, 3, or 4
    while user_input in "1234":

        # looks up the name and email
        if user_input == '1':
            name = input("Enter a name: ")
            look_up_email(name)

        # enters a new name and email address
        elif user_input == '2':
            name = input("Enter name: ")
            email = input("Enter email address: ")
            add_new_name_email(name, email)

        # changes email address
        elif user_input == '3':
            name = input("Enter name: ")
            change_email(name)

        # deletes name and email address
        elif user_input == '4':
            name = input("Enter name: ")
            delete_name_email(name)
        print()

        # asks user for choice
        menu()
        user_input = input("Enter your choice: ")

        # if it's not a valid choice, asks user for choice
        while user_input not in "12345":
           user_input = input("Enter a valid choice: ")

    # exits the function
    if user_input == '5':
        print("Information saved")

    

main()
