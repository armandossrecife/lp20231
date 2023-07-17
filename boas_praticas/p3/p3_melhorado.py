import os

class Person:
    def __init__(self, cpf, name, address, phones):
        self.cpf = cpf
        self.name = name
        self.address = address
        self.phones = phones

class ManageFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_exists(self):
        return os.path.exists(self.file_name)

    def insert_content(self, person):
        register = f"{person.cpf};{person.name};{person.address};{person.phones}"
        with open(self.file_name, 'a') as file_temp:
            file_temp.write(register + "\n")

    def read_file_content(self):
        if self.file_exists():
            with open(self.file_name, mode='r') as file_temp:
                file_content = file_temp.read()
                print(file_content)
        else:
            print(f"The file {self.file_name} does not exist!")

    def list_file_content(self):
        list_content = []
        if self.file_exists():
            with open(self.file_name, mode='r') as file_temp:
                for line in file_temp:
                    list_content.append(line.strip())
        else:
            print(f"The file {self.file_name} does not exist!")
        return list_content

class MyPhoneList:
    def __init__(self):
        self.manage_file = ManageFile("people.txt")

    def read_person_data(self):
        cpf = input("Type the CPF: ")
        name = input("Type the name: ")
        address = input("Type the address: ")
        phones = input("Type the phones (comma separated): ")
        person_temp = Person(cpf, name, address, phones)
        return person_temp

    def insert_contact(self):
        person = self.read_person_data()
        if person is not None:
            self.manage_file.insert_content(person)

    def list_contacts(self):
        return self.manage_file.list_file_content()

    def search_by_cpf(self):
        cpf = input("Type the CPF you need to find: ")
        for line in self.manage_file.list_file_content():
            if line.startswith(cpf):
                return line
        return None


def clean_file():
    with open("people.txt", "w") as file:
        file.write("")

def menu():
    print("**MENU****")
    print("1. Insert person")
    print("2. List registered people")
    print("3. Search person by CPF")
    print("4. Search person by Phone")
    print("5. Remove person by CPF")
    print("6. EXIT.")

my_phone_list = MyPhoneList()
menu_on = True
while menu_on:
    menu()
    op = input("Option: ")
    if op == '1':
        print("***Inserting a new person***")
        my_phone_list.insert_contact()
    elif op == '2':
        print("***List of registered people***")
        print(my_phone_list.list_contacts())
    elif op == '3':
        print("***Searching person by CPF***")
        print(my_phone_list.search_by_cpf())
    elif op == '4':
        print("***Yet to implement***")
    elif op == '5':
        print("***Yet to implement***")
    elif op == '6':
        break
    else:
        print("***Invalid option, please type a valid one.***\n")