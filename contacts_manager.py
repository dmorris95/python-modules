from datetime import datetime
import re

phone_pattern = r"\d{3}-\d{3}-\d{4}"


def add_contact(contact):
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]"
     

    name_input = input("Please enter the Contacts name: ")
    while name_input == "":
        name_input = input("You must enter the contacts name: ")

    date_input = input("Please enter the date you first met the contact into a valid format: ")
    while True:
        if re.match(date_pattern, date_input):
            date_obj = datetime.strptime(date_input, '%Y-%m-%d').date()
            break
        else:
            date_input = input("Please enter the date in a valid format (yyyy-mm-dd): ")
    
    phone_input = input("Please enter the contacts phone number: ")
    while True:
        if re.match(phone_pattern, phone_input):
            break
        else:
            phone_input = input("Please enter the phone number in a valid format (XXX-XXX-XXXX): ")

    email_input = input("Please enter the contacts email: ")
    while True:
        if re.match(email_pattern, email_input):
            break
        else:
            email_input = input("Please enter the contacts email in a valid format: ")

    contact[phone_input] = {"Name": name_input, "Phone Number": phone_input, "Date": date_obj, "Email Address": email_input}
    print("Contact successfully added!")
    return contact

def remove_contact(contact):
    user_input = input("Please enter the phone number of the contact you would like to remove: ")
    if user_input in contact:
        del contact[user_input]
        print("Contact successfully deleted")
    else:
        print("That contact is not in your contact list, please try agian!")
                
    

def display_contacts(contact):
    if len(contact) == 0:
        print("You have to have contacts first!")
    else:
        for num, c_info in contact.items():
            print(f"Contact Number: {num}\nName: {c_info['Name']}------ Phone Number: {c_info['Phone Number']}\nDate: {c_info['Date']} ------Email Address: {c_info['Email Address']}")
