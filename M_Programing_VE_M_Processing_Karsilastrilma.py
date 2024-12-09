from multiprocessing import Process
import threading
import time

# Faktöriyel hesaplama fonksiyonu (recursive)
def faktoriyel_hesapla(n):
    if n <= 1:
        return 1
    return n * faktoriyel_hesapla(n - 1)

# Faktöriyel hesaplama işlemi ve işlem/iş parçaciği kimliği yazdirma
def faktoriyel_hesaplama(sayi):
    sonuc = faktoriyel_hesapla(sayi)
    print(f"Hesaplaniyor (Thread iD: {threading.get_ident()}): {sayi}! -> {sonuc}")
    time.sleep(1)

# Kare hesaplama işlemi ve işlem/iş parçaciği kimliği yazdirma
def kare_hesaplama(sayi):
    print(f"Hesaplaniyor (Process ID: {threading.get_ident()}): {sayi} -> {sayi * sayi}")
    time.sleep(1)

# Çoklu programlama (threading) kullanilarak faktöriyel hesaplama
def coklu_programlama():
    sayilar = [1, 2, 3, 4, 5, 6]
    print("Coklu Programlama Başladi (Thread)...\n")
    
    thread_list = []
    for sayi in sayilar:
        t = threading.Thread(target=faktoriyel_hesaplama, args=(sayi,))
        thread_list.append(t)
        t.start()

    for t in thread_list:
        t.join()  # Tüm iş parçaciklarinin tamamlanmasini bekle
    
    print("\nCoklu Programlama Tamamlandi")

# Çoklu işlemci (multiprocessing) kullanilarak kare hesaplama
def coklu_islemci():
    sayilar = [1, 2, 3, 4, 5, 6]
    print("Coklu islemci Basladi (Process)...\n")
    
    process_list = []
    for sayi in sayilar:
        islem = Process(target=kare_hesaplama, args=(sayi,))
        process_list.append(islem)
        islem.start()

    for islem in process_list:
        islem.join()  # Tüm işlemlerin tamamlanmasini bekle
    
    print("\nCoklu islemci Tamamlandi")

# Ana program
if __name__ == "__main__":
    coklu_programlama()
    coklu_islemci()
