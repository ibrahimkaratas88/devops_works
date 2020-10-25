
def checkform(text):
    pairs = {')':'(', ']':'[','}':'{'}
    que = []
    for i in text:
        if i in pairs.values():
            que.append(i)
        elif i in pairs.keys():
            if que[-1] == pairs[i]:
                que.pop(-1)
            else:
                return False #parantez açılmadan kapanmış
        else:
            return False #geçersiz karakter     
    return False if que else True #que de eleman varsa False

print("please enter paranthesis forms")

text = input()
sonuc = checkform(text)
print (sonuc)