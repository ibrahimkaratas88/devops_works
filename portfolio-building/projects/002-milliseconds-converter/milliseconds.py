def convertMillis(millis):
    seconds=(millis//1000)%60
    minutes=(millis//(1000*60))%60
    hours=(millis//(1000*60*60))%24
    d = [hours,minutes,seconds]
    return (d)

print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print("To exit the program, please type 'exit'")
print("Please enter the milliseconds (should be greater than zero) :")
a = 0
while a == 0:
    x = input ()
    b = x.isnumeric()
    if b == True:
        x = int(x)
        print(convertMillis(x))
    elif b == False :
        x = str(x)
        x = x.title()
        if x == "Exit":
            print("Exiting the program... Good Bye")
            a = 1
            break
        else:
            print ("Not Valid Input!!!")
            print("To exit the program, please type 'exit'")
            print("Please enter the milliseconds (should be greater than zero) :")