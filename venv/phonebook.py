import re
from Scripts.Contact import Contact
from Scripts.Book import Phonebook
new_book  = Phonebook()
with open("file.txt", 'r') as f:

    lines = f.read()
    new_book.add_contacts_from_file(lines)
    n = input("0-show phonebook\n1-add contact\n2-add new number\n3-delete contact\n4-change contact\n5-find contact\n"
              "6-age of contact\n7- bithdays in next 30 days\n8- show contacts who older than\n9- show contacts who younger than\n"
                  "10-exit\n")

    while n != "10":
        if n =="0":
            new_book.show_phonebook()
        elif n == "1":
            print("Example: Ivanov Ivan 89991234576 01-01-1990\nInput your contact: \n")
            new_name = input("Input a name of contact\n")
            new_surname = input("Input a surname of contact\n")
            new_number = input("Input a phone number of contact\n")
            new_dob = input("Input date of birth of contact\n")
            new_book.add_new_contact(new_name, new_surname, new_number, new_dob)
        elif n == "2":
            new_book.add_new_number()
        elif n == "3":
            new_book.delete_contact()
        elif n == "4":
            new_book.change_contact()
        elif n == "5":
            new_book.find_contact()
        elif n == "6":
            new_book.get_age()
        elif n == "7":
            new_book.upcoming_bithdays()
        elif n == "8":
            age = input("input a number of age\n")
            try:
                new_book.contacts_older_than(int(age))
            except ValueError:
                print("Invalid format")
        elif n == "9":
            age = input("input a number of age\n")
            try:
                new_book.contacts_younger_than(int(age))
            except ValueError:
                print("Invalid format")
        else:
            print("No such command")
        n = input("0-show phonebook\n1-add contact\n2-add new number\n3-delete contact\n4-change contact\n5-find contact\n"
              "6-age of contact\n7- bithdays in next 30 days\n8- show contacts who older than\n9- show contacts who younger than\n"
                  "10-exit\n")


with open("file.txt", 'w') as f:
    new_book.write_contacts_to_file(f)



