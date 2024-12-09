import threading
import time

def faktoriyel(n):
#Bir sayının faktöriyelini hesapla
    if n <= 1:
        return 1
    return n * faktoriyel(n - 1)

# Program 1: Sayıları yazdır
def program_1():
    for i in range(1, 14):
        F_Sonuc = faktoriyel(i)
        print(f"Program 1 Çalıştı: Parca {i}  ,Sonuç: {F_Sonuc}")
        time.sleep(0.5)  # İşlem için bekleme

# Program 2: Harfleri yazdır
def program_2():
    i=0
    for ch in 'Merhaba_Dunya':
        i+=1
        print(f"Program 2 Çalıştı: Parca {i} ,Kelime: {ch}")
        time.sleep(0.5)  

# Her bir program için iş parçacığı oluştur
thread1 = threading.Thread(target=program_1)
thread2 = threading.Thread(target=program_2)

# İş parçacıklarını başlat
thread1.start()
thread2.start()

# Her iki iş parçacığının tamamlanmasını bekle
thread1.join()
thread2.join()

print("Çoklu Programlama örneği tamamlandı!")
