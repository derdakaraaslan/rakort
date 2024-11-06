# Ağ Bağlantı Kontrolü

Bu proje, belirli bir ağdaki cihazlara ping atarak bağlantı durumlarını kontrol etmeyi amaçlamaktadır. Python'un asyncio kütüphanesi ile eşzamanlı bağlantılar yapılır ve her cihaz için sürekli olarak ağ bağlantısı testi gerçekleştirilir. Belirtilen ağda bulunan ip adreslerine ping atılarak erişilemeyen ip adresleri konsola yazdırılır. Bu örnekte 172.29.0.1/23 ağı taranmaktadır. Bu ağda 512 ip adresi bulunmaktadır ancak kullanılabilir ip adresi sayısı 510'dur. Projede Ping testi, her cihaz için 5 saniye içinde cevap alınamaması durumunda başarısız kabul edilir. Proje siz kapatana kadar çalışmaya devam edecektir.

## Gereksinimler

Bu projede aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- **asyncio**: Python'un asenkron programlama kütüphanesi. Python sürümleriyle birlikte gelmektedir.
- **aioping**: IP adreslerine ping atmak için kullanılan asenkron kütüphane.
- **ipaddress**: Python'un IP adresleriyle çalışmak için kullanılan standart kütüphanesidir. Python 3.3 ve sonrasında dahili olarak gelir, bu yüzden ayrıca yüklenmesine gerek yoktur.


## Projeyi Çalıştırma

Öncelikle aşağıdaki komut ile gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt 
```


Ardından projeyi çalıştırın:

```bash
python main.py
```
