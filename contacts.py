#Task 1
import contacts_manager
from datetime import datetime

contact_list = {
    "234-423-1342":{"Name": "Joe Smith","Phone Number": "234-423-1342","Date": "2023-04-13","Email Address": "joesmith@gmail.com"},
    "123-567-1234":{"Name": "Steve Johnson", "Phone Number": "123-567-1234", "Date": "2024-01-12","Email Address": "stevejohn@aol.com"}
    }

def display_menu(contact):
    print("Welcome to the Contact Manager")
    
    print("Menu:\n1. Add contact\n2. Remove contact\n3. Display contacts\n4. Quit")
    try:
        user_input = int(input("Please select an option: "))
        while user_input > 0 and user_input < 4:
            if user_input == 1:
                contact = contacts_manager.add_contact(contact)
                display_menu(contact)
            elif user_input == 2:
                contacts_manager.remove_contact(contact)
                display_menu(contact)
            elif user_input == 3:
                contacts_manager.display_contacts(contact)
                display_menu(contact)
        print("Thank you for using the contact manager!")
    except ValueError:
        print("You must enter a number between 1 and 4")

print(datetime.now().strftime("%B %Y"))
display_menu(contact_list)