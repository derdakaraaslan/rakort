# SSH Bağlantı Testi

Bu proje, belirli bir ağdaki cihazlara SSH bağlantısı kurmayı ve bağlantıların başarılı olup olmadığını test etmeyi amaçlamaktadır. Python'un **`asyncio`** kütüphanesi kullanılarak eşzamanlı (asenkron) bağlantılar yapılır ve her cihaz için SSH bağlantı denemeleri yapılır. Timout süresi 2 olarak belirlenmiştir. Bu süre ağ koşullarına göre ayarlanmalıdır.

## Gereksinimler

Bu projede aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- **asyncssh**: SSH bağlantıları kurmak için kullanılan kütüphane.
- **asyncio**: Python'un asenkron programlama kütüphanesi. Python sürümleriyle birlikte gelmektedir.
- **time**: Python'un zaman ölçümü ve uyku işlevlerini sağlayan standart kütüphanedir. Python ile birlikte gelir.
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
