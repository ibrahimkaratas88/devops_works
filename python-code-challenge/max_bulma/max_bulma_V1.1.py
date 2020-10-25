
print("###  This program finds maximum number which you enter ###")
print("How many number you want to enter")
# say = int(input())
counter = 0
say = 0

while counter > say-1:
    say = input ()
    b = say.isnumeric()
    if b == True:
        liste =[]
        say = int(say)
        for i in range (say):
            print ("lütfen", i+1 , ". sayıyı giriniz")
            a = input ()
            c = a.isdigit()
            if c == True:
                a = int(a)
                liste.append(a)
                counter +=1
            else:
                print(" Lütfen tam sayı giriniz : ")
    elif b == False:
        say = str (say)
        say = say.title()
        if say == "Exit":
            print ("Exiting the program....Good Bye")
            break
    else:
        print ("Not Valid Input!!! Please enter valid input :")
        print("To exit the program, please type 'exit'")
        print("Please enter a number ") 
            

    print ("girdiğiniz sayıların sırası", liste)
    liste = sorted(liste, reverse=True)
    print("girdiğiniz sayıların büyükten küçüğe sıralaması ", liste)
    print('en büyük sayı = ', liste[0])

    max = 0
    for z in liste:
        if z > max:
            max = z
    print("girdiğiniz sayıların büyükten küçüğe sıralması", liste)
    print("en büyük sayı = ", max)
