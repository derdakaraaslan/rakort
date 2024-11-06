# FastAPI Uygulaması

Bu proje, kullanıcılar ve ürünler üzerinde CRUD (Create, Read, Update, Delete) işlemlerini gerçekleştiren bir FastAPI uygulamasıdır. Proje, SQLAlchemy kullanarak veritabanı ile iletişim kurar ve çeşitli kullanıcı ve ürün işlemleri sağlar. Ayrıca, büyük miktarda kullanıcı verisi eklemek, silmek veya güncellemek için toplu (bulk) işlemler de desteklenmektedir.

Projede bulk komutları sadece user için yazılmıştır. Product için işlemler aynı olacağından dolayı zaman kazanılması açısından yapılmamıştır.

## Özellikler

- **Kullanıcı Yönetimi API**:
  - `GET /users/`: Kullanıcıları listeleme
  - `GET /users/{user_id}`: Belirli bir kullanıcıyı görüntüleme
  - `POST /users/`: Yeni kullanıcı ekleme
  - `PUT /users/{user_id}`: Kullanıcı güncelleme
  - `DELETE /users/{user_id}`: Kullanıcı silme
  - `POST /random_bulk_insert_users/`: Rastgele 100.000 kullanıcı ekleme
  - `POST /bulk_insert_users/`: Verilen verilerle toplu kullanıcı ekleme
  - `DELETE /random_bulk_delete_users/`: Rastgele 100.000 kullanıcı silme
  - `DELETE /bulk_delete_users/`: Verilen kullanıcı kimlikleriyle toplu kullanıcı silme
  - `PUT /random_bulk_update_users/`: Rastgele kullanıcılar için toplu güncelleme
  - `PUT /bulk_update_users/`: Verilen kullanıcı kimlikleriyle toplu kullanıcı güncelleme

- **Ürün Yönetimi API**:
  - `GET /products/`: Ürünleri listeleme
  - `GET /products/{product_id}`: Belirli bir ürünü görüntüleme
  - `POST /products/`: Yeni ürün ekleme
  - `PUT /products/{product_id}`: Ürün güncelleme
  - `DELETE /products/{product_id}`: Ürün silme

- **Veritabanı Yönetimi**: 
  - SQLAlchemy kullanarak SQlite (veya başka bir ilişkisel veritabanı) ile etkileşim.
  - Veritabanı tabloları uygulama başlatıldığında otomatik olarak oluşturulur.

- **Toplu Veri İşlemleri**:
  - 100.000'lerce kullanıcıyı veritabanına toplu olarak ekleyebilme, silebilme ve güncelleyebilme.


## Gereksinimler

Bu projede aşağıdaki Python kütüphanelerine ihtiyaç vardır:

- **fastapi**: Web uygulamaları için modern, hızlı (yüksek performanslı) bir Python framework'ü.
- **uvicorn**: FastAPI uygulamaları için ASGI server.
- **sqlalchemy**: Python için ORM (Object Relational Mapping) kütüphanesi. Veritabanı ile etkileşim sağlar.
- **pydantic**: Veri doğrulama ve ayıklama için kullanılan kütüphane. FastAPI ile birlikte gelir.


## Projeyi Çalıştırma

Öncelikle aşağıdaki komut ile gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt 
```


Ardından projeyi çalıştırın:

```bash
uvicorn app.main:app --reload
```
