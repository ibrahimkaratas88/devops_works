
def print_menu():
    print("Welcome to the phonebook application")
    print("1. Show phone number")
    print("2. Insert phone number")
    print("3. Find a phone number")
    print("4. Edit a person from phonebook")
    print("5. Delete a person from phonebook")
    print("6. Terminate")
    print("Select operation on Phonebook App (1/2/3/4/5) :", '\n')
    print()
    contacts=open('contacts.txt','a+')
    contacts.seek(0)
    m=contacts.read()
    contacts.seek(len(m))
    n=input("bir seçenek girin")
    n = int(n)
    if n==1:
        print(m)
        print_menu()
    elif n==2:
        n2(contacts)
    elif n==3:
        n3(contacts,m)
    elif n==4:
        n4(contacts,m)
    elif n==5:
        n5(contacts,m)
    elif n==6:
        contacts.close()
    else:
        print_menu()
#---------------------add-----------------------------------------------------
def n2(contacts):
    na=input("name    :\n")
    nu=input("number  :\n")
    contacts.write(na+'\t'+nu+'\n')
    contacts.close()
    print_menu()
#---------------------srch----------------------------------------------------
def n3(contacts,m):
    n=int(input('1-number\n2-name\n'))
    if n==1:
        nu=input('number:\n')
        e=m.index(nu)
        s=m.index('\n',e)
        print(m[s+1:e+len(nu)])
        print_menu()
    elif n==2:        
        na=input('name:\n')     
        s=m.index(na)
        e=m.index('\n',s)
        print(m[s:e])
        print_menu()
    else:
        print_menu()
#-------------------EDIT------------------------------------------------
def n4(contacts,m):
    n=int(input('1-number\n2-name\n'))
    if n==1:
        nu=input('number:\n')
        e=m.index(nu)
        s=m.rindex('\n',0,e)
        contacts.seek(s+1)
        n2(contacts)
    elif n==2:
        na=input('name:\n')
        s=m.index(na)
        contacts.seek(s)
        n2(contacts)
        print_menu()
    else:
        print_menu()
#---------------------DEL-----------------------------------------------------
def n5(contacts,m):
    n=int(input('1-number\n2-name\n'))
    if n==1:
        nu=input('number:\n')
        e=m.index(nu)
        s=m.rindex('\n',0,e)
        contacts.seek(s+1)
        contacts.write((s-e)*'')
    elif n==2:
        na=input('name:\n')
        s=m.index(na)
        contacts.seek(s)
        contacts.write((s-e)*'')
        print_menu()

print_menu()

