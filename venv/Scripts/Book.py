from Scripts.Contact import Contact, is_valid_name, is_valid_number
import re
import datetime
class Phonebook:
    Phonebook = []
    def add_contacts_from_file(self, lines):
        for line in lines.split("\n"):
            if line:
                contact = Contact(line.split('~')) # pars & init new contact
                old_contact = self.find(contact.name, contact.surname)
                if old_contact:
                    old_contact.add_new_phone_number(contact.phone_numbers[0])
                else:
                    self.Phonebook.append(contact)
        print("Phonebook is ready")

    def write_contacts_to_file(self, file):
        for contact in self.Phonebook:
            for i in range(contact.count_of_numbers+1):
                file.write(contact.surname)
                file.write("~")
                file.write(contact.name)
                file.write("~")
                file.write(contact.phone_numbers[i])
                file.write("~")
                if contact.date_of_birth:
                    file.write(contact.date_of_birth.strftime("%d.%m.%Y"))
                file.write("\n")


    def show_phonebook(self):
        for contact in self.Phonebook:
            contact.show_contact()

    def add_new_number(self):
        name = input("input name of contact\n")
        surname = input("input surname of contact \n")
        contact = self.find(name, surname)
        if contact:
            new_number = input("Input new phone number of "+ contact.name + " " + contact.surname + "\n")
            if is_valid_number(new_number):
                f = True
                for num in contact.phone_numbers:
                    if num == new_number:
                        f = False
                if f:
                    contact.add_new_phone_number(new_number)
                    print("new number of "+contact.surname+" "+contact.name+" is added\n")
                else:
                    print("this number is already in phonebook\n")
            else:
                print("Not valid format")
        else:
            print("No such contact")

    def add_new_contact(self, name, surname, number, date = ""):
        if is_valid_name(name) and is_valid_name(surname) and is_valid_number(number): #if it is valid, we will add it
            new_contact = Contact([surname, name, number, date])
            old_contact = self.find(new_contact.name, new_contact.surname)
            if old_contact:
                f = False
                for number in old_contact.phone_numbers:
                    if new_contact.phone_numbers[0] == number:
                        print("This contact is already in phonebook")
                        f = True
                if not f :
                    old_contact.add_new_phone_number(new_contact.phone_numbers[0])
                    print("New phone number of",new_contact.surname,new_contact.name, "is added")
            else:
                self.Phonebook.append(new_contact)
                print(new_contact.name, new_contact.surname, "is added to phonebook")
        else:
            print("Invalid format\nPlease try add a contact again")

    def find(self, name, surname):
        for contact in self.Phonebook:
            if (contact.name == name) and (contact.surname == surname):
                return contact
        else:
            return None

    def find_contact(self):
        nameSearch = input("input a name or part of name or press Enter\n")
        surnameSearch = input("input a surname or part of surname or press Enter\n")
        numberSearch = input("input a number or part of number or press Enter\n ")
        f = False
        for contact in self.Phonebook:
            if re.search(nameSearch, contact.name) and re.search(surnameSearch, contact.surname):
                for num in contact.phone_numbers:
                    g = False
                    if re.search(numberSearch, num):
                        f = True
                        g = True
                if g:
                    contact.show_contact()
        if not f:
            print("No such contact\n")

    def delete_contact(self):
        name = input("input name of contact which you want to delete\n")
        surname = input("input surname of contact which you want to delete\n")
        contact = self.find(name, surname)
        if contact:
            answer = int(input("Are you sure that you want to delete "+ contact.name + " " +
                            contact.surname + " from your phonebook?\n1 - Yes 2 - No\n"))
            if answer == 1:
                self.Phonebook.remove(contact)
        else:
            print("No such contact\n")

    def change_contact(self):
        name = input("input name of contact which you want to change\n")
        surname = input("input surname of contact which you want to change\n")
        contact = self.find(name, surname)
        if contact:

            answer = int(input("What do you want to change in contact " + contact.name + " " +
                               contact.surname + " \n1 - name, 2 - surname, 3 - phone number, 4 - date of birth\n"))
            f = False
            if answer == 1:
                new_name = input("Input a new name\n")
                if is_valid_name(new_name):
                    if self.find(new_name, contact.surname):
                        print("Sorry, but contact with these name and surname is already exist")
                    else:
                        f = True
                        contact.name = new_name
                else:
                    print("Invalid format")
            elif answer == 2:
                new_surname = input("Input a new surname\n")
                if is_valid_name(new_surname):

                    if self.find(conatct.name, new_surname):
                        print("Sorry, but contact with these name and surname is already exist")
                    else:
                        f = True
                        contact.surname = new_surname
                else:
                    print("Invalid format")
            elif answer == 3:
                new_number = input("Input a new phone number\n")
                if is_valid_number(new_number):
                    g = true
                    for i in contact.phone_numbers:
                        if i == new_number:
                            g = false
                    if g:
                        f = True
                        contact.phone_numbers[0] = new_number
                    else:
                        print("This number is alredy belongs to this contact")
                else:
                    print("Invalid format")
            elif answer ==4:
                date = input("Input a new date of birth\n")
                try:
                    new_date_of_birth = datetime.datetime.strptime(date, '%d.%m.%Y')
                except ValueError:
                    new_date_of_birth = ""
                    print("Invalid format")
                if new_date_of_birth:
                    f = True
                    contact.date_of_birth = new_date_of_birth
            if f:
                print("Contact of "+contact.name + " " + contact.surname+" has changed\n")
        else:
            print("No such contact")

    def get_age(self):
        name = input("input name of contact\n")
        surname = input("input surname of contact\n")
        contact = self.find(name, surname)
        if contact:
            if contact.date_of_birth:
                print(contact.age())
            else:
                print("Date of Birth is not exist")
        else:
            print("No such contact")
    def upcoming_bithdays(self):
        today = datetime.date.today()
        soon = datetime.date.today() + datetime.timedelta(days = 30)
        for contact in self.Phonebook:
            if contact.date_of_birth:
                day = contact.date_of_birth.day
                month = contact.date_of_birth.month
                if datetime.date(today.year, month, day) < today:
                    year = today.year + 1
                else:
                    year = today.year
                nxt_birth = datetime.date(year, month, day)
                if nxt_birth < soon:
                    print(contact.surname, contact.name)
    def contacts_older_than(self, age):
        for contact in self.Phonebook:
            if contact.date_of_birth:
                if (contact.age() >= age):
                    print(contact.surname, contact.name, contact.age())

    def contacts_younger_than(self, age):
        for contact in self.Phonebook:
            if contact.date_of_birth:
                if (contact.age() < age):
                    print(contact.surname, contact.name, contact.age())


