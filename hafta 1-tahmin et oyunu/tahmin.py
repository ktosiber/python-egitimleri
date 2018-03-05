import random

tahmin_edilecek=random.randint(1,100)
puan = 100
durum = {
    'kucuk': 'Daha buyuk bir sayi giriniz!',
    'buyuk': 'Daha kucuk bir sayi giriniz!',
    'kaybet': 'Puan bitti kaybettiniz!'
}
while True:
    kul_tamini = input('Bir sayi giriniz: ')
    kul_tamini = int(kul_tamini)
    if puan > 0:
        if (tahmin_edilecek == kul_tamini):
            print ('Tahmin dogru!')
            print ('Puanınız {}, Tahmin edilen sayi : {}'.format(puan, tahmin_edilecek))
            print ('Puanınız '+ str(puan) + 'Tahmin edlien sayi : ' + str(tahmin_edilecek))
            break
        elif (kul_tamini < tahmin_edilecek):
            print (durum['kucuk'])
            puan = puan - 10
        elif (kul_tamini > tahmin_edilecek):
            print (durum['buyuk'])
            puan = puan - 10
    elif puan == 0:
        print (durum['kaybet'])
        break