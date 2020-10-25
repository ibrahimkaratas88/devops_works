def int_to_Roman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
print("###  This program converts decimal numbers to Roman Numerals ###")
print("To exit the program, please type 'exit'")
print("Please enter a number between 1 and 3999, inclusively :")
a = 0
while a == 0:
    x = input ()
    b = x.isnumeric()
    if b == True:
        x = int(x)
        if (x >= 1) and (x <4000):
            print(int_to_Roman(x))
        else:
            print ("Not Valid Input!!! Please enter valid input (1-3999) :")
            print("To exit the program, please type 'exit'")
            print("Please enter a number between 1 and 3999, inclusively :")
    elif b == False :
        x = str(x)
        x = x.title()
        if x == "Exit":
            print("Exiting the program... Good Bye")
            a = 1
            break
        else:
            print ("Not Valid Input!!! Please enter valid input (1-3999) :")
            print("To exit the program, please type 'exit'")
            print("Please enter a number between 1 and 3999, inclusively :")