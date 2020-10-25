# bize verilen bir liste içerisinde bir defa geçen elemanları bulmak için yazılan program
# listenin bir txt dosyasında bulunduğu varsayılarak program yazılmıştır. txt dosyasında son satırdan sonra enter tuşuna basılarak 
#txt dosyası kaydedilmelidir.
# txt dosyası yerine direk bir listede oluşturularak program yazılabilir. önemli olan kısım for döngüsü içerisinde gerçekleşmektedir.
# n=m.count(m[i]) kodu ile liste içerisinde her elemandan kaç tane bulunduğu sayılmakta ve 
# sadece bir defa bulunanlar ekrana yazdırılmaktadır.

def text_to_list():
    products=open('products.txt','r+') 
    products.seek(0)
    m=products.readlines()
    products.close()
    print (m, "\n")
    print ("bir tane bulunan ürünler :","\n")
    for i in range(len(m)):
          n = m.count(m[i])
          if n == 1:
                print(m[i])

text_to_list()
