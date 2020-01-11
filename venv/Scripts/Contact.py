import re
import datetime
class Contact:
    suname = None
    name = None
    phone_number = None
    date_of_birth = None
    phone_numbers = None
    count_of_numbers = 0
    def __init__(self, arr):
        self.surname = arr[0].capitalize()
        self.name = arr[1].capitalize()
        self.count_of_numbers = -1 # pos of last phone number
        self.phone_numbers = []
        self.add_new_phone_number(arr[2])
        if (len(arr) == 4):
            if (arr[3] != ""):
                try:
                    self.date_of_birth = datetime.datetime.strptime(arr[3], '%d.%m.%Y')
                except ValueError:
                    print("Invalid format of date\n")
                    self.date_of_birth = ""
    def add_new_phone_number(self, num):
        self.count_of_numbers += 1
        self.phone_numbers.append(num)
    def show_contact(self):
        print(self.surname + " " + self.name + " ", end='')
        for i in self.phone_numbers:
            print(i, end=" ")
        if self.date_of_birth:
            print(self.date_of_birth.strftime("%d.%m.%Y"), end = "")
        print()
    def age(self):
        today = datetime.datetime.today()
        delta = today - self.date_of_birth
        return int(delta.total_seconds()//(3600*24*365))



def is_valid_name(name):
    for i in name:
        if not ((i >= '0' and i <= '9') or (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z') or (i == " ")):
            return False
    return True


def is_valid_number(number):
    if number[0] == "+":
        number = "8" + number[2:]
    if re.match(r'8[0-9]{10}', number) and len(number) == 11:
        return True
    else:
        return False