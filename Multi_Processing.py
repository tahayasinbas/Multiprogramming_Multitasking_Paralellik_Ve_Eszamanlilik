import multiprocessing
import os

# Faktöriyel hesaplama fonksiyonu (recursive)
def faktoriyel_hesapla(n):
    # Bir sayının faktöriyelini hesaplar
    if n <= 1:
        return 1
    return n * faktoriyel_hesapla(n - 1)

# İşlemleri gösteren ve faktöriyel hesaplayan fonksiyon
def Islemi_Goster(sayilar):
    # Faktöriyel hesapla ve işlem kimliğiyle birlikte yazdır
    sayi = faktoriyel_hesapla(sayilar)
    print(f"Islem Kimligi (PID): {os.getpid()} - Sayi: {sayilar}, Faktoriyeli: {sayi}")

# Ana program bloğu
if __name__ == "__main__":
    # Faktöriyeli hesaplanacak sayılar listesi
    sayilar = [1, 2, 3, 4, 5]
    islemler = []

    # Her bir sayı için ayrı bir işlem oluştur ve başlat
    for sayi in sayilar:
        # Yeni işlem oluşturuluyor, Islemi_Goster fonksiyonu çağrılacak
        p = multiprocessing.Process(target=Islemi_Goster, args=(sayi,))
        islemler.append(p)  # İşlem listesini güncelle
        p.start()  # İşlemi başlat
    
    # Bütün işlemlerin tamamlanmasını bekle
    for p in islemler:
        p.join()  # İşlemin bitmesini bekle