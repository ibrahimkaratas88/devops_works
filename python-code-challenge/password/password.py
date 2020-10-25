

def print_menu():
   print("Welcome to the password application")
   print("1. Show password list")
   print("2. Insert password")
   print("3. Find a password")
   print("4. Terminate")
   print("Select operation on Password App (1/2/3/4) :", '\n')
   print()
   sifreler=open('sifreler.txt','a+')
   sifreler.seek(0)
   m=sifreler.read()
   sifreler.seek(len(m))
   n=int(input())
   if n==1:
      print(m)
      print_menu()
   elif n==2:
      n2(sifreler)
   elif n==3:
      n3(sifreler,m)
   elif n==4:
      sifreler.close()
   else:
      print_menu()


def n2(sifreler):
   import secrets
   na=input("name and surname   :\n")
   na=na.lower()
   harf =""
   for i in range(3):
      harf += secrets.choice(na)
   sayı=""
   for j in range (4):
      sayı += str(secrets.randbelow(9))
   password = harf + sayı
   sifreler.write(na+'\t'+password+'\n')
   sifreler.close()
   print ("şifreniz....:", password, "\n")
   print_menu()
    
def n3(sifreler,m):
   na=input('name:\n')     
   s=m.index(na)
   e=m.index('\n',s)
   print(m[s:e])
   print_menu()



print_menu()