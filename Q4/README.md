# İşlem İzleme ve Kaynak Kullanımı Güncelleme

Bu proje, belirli işlemlerin durumlarını ve sistem kaynaklarını (CPU ve bellek kullanımı) izlemek amacıyla geliştirilmiştir. Her işlem için asenkron olarak durum güncellemeleri yapılır ve bu güncellemeler veritabanına kaydedilir. Proje, bir işlem başlatıldığında durumu "Running" olarak belirler ve işlem tamamlandığında durumu "Completed" olarak günceller.
Python'un asyncio, psutil, ve SQLAlchemy gibi kütüphaneleri kullanılarak kaynak kullanımı etkin bir şekilde izlenir ve ProcessPoolExecutor ile paralel işlem desteği sağlanır.
Projede, worker_function adındaki fonksiyon paralel olarak 1000 adet çalıştırılır ve her bir işlem içerisinde asyncio kullanılarak asenkron olarak işlem kaynak kullanımları ve işlem durumu veritabanında güncellenir.
İşlemciyi zorlamak adına worker_function asal sayıları hesaplamaktadır. Bu fonksiyon gereksinimlere göre değiştirilebilir.


## Gereksinimler

Bu projede aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- **psutil**: İşlem ve sistem kaynaklarını izlemek için kullanılan kütüphane.
- **SQLAlchemy**: Veritabanı işlemleri için kullanılan ORM kütüphanesi.
- **asyncio**: Python'un asenkron programlama kütüphanesi.
- **concurrent.futures**:  Paralel işlem desteği için Python'un standart kütüphanesi.


## Projeyi Çalıştırma

Öncelikle aşağıdaki komut ile gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt 
```


Ardından projeyi çalıştırın:

```bash
python main.py
```

## Proje Özellikleri

- **Paralel İşlem Desteği**: ProcessPoolExecutor kullanılarak her işlem için paralel çalıştırma sağlanır.
- **Kaynak Kullanımı İzleme**: psutil kütüphanesi ile işlem başına CPU ve bellek kullanımı ölçülür.
- **Asenkron Güncelleme**: İşlem ve sistem kaynaklarını izlemek için kullanılan kütüphane.
- **Veritabanı Güncellemesi**: SQLAlchemy ORM kullanılarak işlem bilgileri güncel bir veritabanında saklanır.