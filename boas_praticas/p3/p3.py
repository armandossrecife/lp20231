import os

class Person:
  def __init__(self, cpf, name, adress, phones):
    self.cpf = cpf
    self.name = name
    self.adress = adress
    self.phones = phones

class ManageFile:
  def __init__(self, file_name):
    self.file_name = file_name

  def file_exists(self):
    test_file = os.path.exists(self.file_name)
    if test_file:
      return True
    else:
      return False

  def insert_content(self, person):
    register = person.cpf + ';' + person.name + ';' + person.adress + ';' + person.phones
    with open(self.file_name, 'a') as file_temp:
      new_line = register + "\n"
      file_temp.write(new_line)

  def ler_conteudo_do_arquivo(self):
    # tests if the file exists
    if self.file_exists():
      with open(self.file_name, mode='r') as file_temp:
        file_content = file_temp.read()
        print(file_content)
    else:
      print(f'The file {self.file_name} does not exist!')

  def list_file_content(self):
    list_content = []
    if self.file_exists():
      with open(self.file_name, mode='r') as file_temp:
        for line in file_temp:
          list_content.append(line)
    else:
      print(f'The file {self.file_name} does not exist!')
    return list_content

class MyPhoneList:
  def __init__(self):
    self.ManageFile = ManageFile("people.txt")

  def read_person_data(self):
    cpf = input("Type the CPF: ")
    name = input("Type the name: ")
    adress = input("Type the adress: ")
    phones = input("Type the phones (comma separated): ")
    person_temp = Person(cpf, name, adress, phones)
    return person_temp

  def insert_contact(self):
    if (self.read_person_data != None):
      self.ManageFile.insert_content(self.read_person_data())

  def list_contacts(self):
    return self.ManageFile.list_file_content()

  def search_by_cpf(self):
      cpf = int(input("Type the CPF you need to find: "))
      with open('people.txt', mode='r') as file:
        line = file.read()
      line = line.split(" ")
      for i in line:
        cpfN = i.split(";")[0]
        if (int(cpfN) == int(cpf)):
          return i
      return None

def clean():
  f = open("people.txt", "w")
  f.write("")
  f.close()

my_phone_list = MyPhoneList()

menu = "**MENU****\n1. Insert person\n2. List registered people\n3. Search person by CPF\n4. Search person by Phone\n5. Remove person by CPF\n6. EXIT."
menuon = True

while (menuon):
  print(menu)
  op = int(input("Option: "))
  if (op == 1):
    print("***Inserting a new person***")
    my_phone_list.insert_contact()
  elif (op == 2):
    print("***List of registered people***")
    print(my_phone_list.list_contacts())
  elif (op == 3):
    print("***Searching person by CPF***")
    print(my_phone_list.search_by_cpf())
  elif (op == 4):
    print("***Yet to implement***")
  elif (op == 5):
    print("***Yet to implement***")
  elif (op == 6):
    clean()
    print("***Cleaned***")
  elif (op == 7):
    break
  else:
    print("***Invalid option, please type a valid one.***\n")