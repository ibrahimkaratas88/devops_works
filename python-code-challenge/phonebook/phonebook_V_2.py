def print_menu():
    print("Welcome to the phonebook application")
    print("1. Find phone number")
    print("2. Insert a phone number")
    print("3. Delete a person from the phonebook")
    print("4. Show all phonebook")
    print("5. Terminate")
    print("Select operation on Phonebook App (1/2/3/4) :", '\n')
    print()
    
def bulma():
    name = input("Please enter the name :")
    if name in phonebook:
        print('\n',"The number is",'\n', phonebook[name])
    else:
        print(name, "The name was not found",'\n')
        

def ekleme():
    print("Add Name and Number",'\n')
    name = input("Name: ")
    phone = input("Number: ")
    phonebook[name] = phone
    
def silme():
    print("Remove Name and Number",'\n')
    name = input("Name: ")
    if name in phonebook:
        del phonebook[name]
    else:
       print(name, "The name was not found",'\n')

def hepsi():
    print("Telephone Numbers:")
    print ("Name     :", "Numbers      :")
    for x in phonebook.keys():
        print(x,"     ",phonebook[x])




phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

while True:
    print_menu()
    menu = int(input())
    if menu == 1:
        bulma()
    elif menu == 2:
        ekleme()
    elif menu == 3:
        silme()
    elif menu == 4:
        hepsi()
    elif menu == 5:
        print ("Exiting Phonebook")
        break
    else:
        True
        







