# önce ürünleri alış ve satış fiyatlarımızın olduğu listeyi giriyoruz.
# sonra içiçe iki tane for döngüsü kurarak oluşturduğumuz listenin elemanlarını karşılaştırıp en büyük ve en küçük ile
# aralarındaki farkı bulmaya çalışıyoruz ancak, burada önemli olan aldığımız fiyattan sonra sattığımız fiyatların en büyüğü
# arasındaki farkı hesaplamamız isteniyor. Yani listenin en büyüğü ve en küçüğü arasındaki fark istenmiyor.
# Eğer bu şekilde istense idi o zaman min() ve max() fonksiyonlarını kullanarak problemi çok daha basit şekilde çözebilirdik.
# Bu nedenle iki tane for dongüsü kurarak liste elemanlarını ve liste elemanlarının index değerlerini karşılaştırıyoruz.
# böylece bir ürün alındığı fiyattan sonra en fazla ne kadar fiyata satılmış ve maksimum kazancımız
# ne olmuş onu tespit ediyoruz.


def max_profit():
    x = int(input("kaç sayı girmek istiyorsunuz? "))
    liste = []
    for i in range(x):
        y = int(input("sayı giriniz"))
        liste.append(y)

    max_prof = 0
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[j] - liste[i] > max_prof and j > i:
                max_prof = liste[j] - liste[i]

    print("max profit", max_prof)


max_profit()
