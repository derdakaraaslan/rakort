import concurrent.futures
import psutil
import os
import time
from database import get_db
from database import engine, Base
from process_info_model import ProcessInfo
from sqlalchemy.orm import Session
import asyncio
Base.metadata.create_all(bind=engine)


def update_process_status(db: Session, pid: int, status: str, cpu_usage: float, memory_usage: float):
    # ProcessInfo tablosundaki verileri günceller.
    process_info = db.query(ProcessInfo).filter(ProcessInfo.pid == pid).first()
    if process_info:
        process_info.status = status
        process_info.cpu_usage = cpu_usage
        process_info.memory_usage = memory_usage
        db.commit()
        db.refresh(process_info)


# Her bir işlemde çalışacak fonksiyon
# İşlemciyi zorlamak için asal sayıları hesaplar
def worker_function(data):
    db: Session = next(get_db())  # Veritabanı oturumunu başlat

    pid = os.getpid()
    start_time = time.time()

    process_info = ProcessInfo(pid=pid, status='Running', start_time=start_time)
    db.add(process_info)
    db.commit()
    db.refresh(process_info)

    limit = 10_000_000
    primes = []
    process = psutil.Process(pid)

    async def async_update_status():
        # Asenkron olarak mevcut process'in durumunu günceller
        # Bu işlem biz durdurana kadar devam eder
        while True:
            cpu_usage = process.cpu_percent()
            memory_usage = process.memory_info().rss / (1024 * 1024)
            print("****************************************************************")
            print(f"Process PID: {pid}, CPU: {cpu_usage}%, Memory: {memory_usage} MB")
            print("****************************************************************")
            update_process_status(db, pid, 'Running', cpu_usage, memory_usage)
            await asyncio.sleep(1)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    status_update_task = loop.create_task(async_update_status())
    

    loop.run_in_executor(None, loop.run_forever)

    try:
        for num in range(2, limit):
            if is_prime(num):
                primes.append(num)
    finally:
        # İşlem tamamlandığında asenkron işlemi durdur
        status_update_task.cancel()
        loop.stop()
        # Asenkron işlemi kapat
        while loop.is_running():
            pass
        # Asenkron işlemin kapandığından emin olduktan sonra event loop'u kapat
        loop.close() 

    print(f"{len(primes)} adet asal sayı bulundu.")

    end_time = time.time()
    process_info = db.query(ProcessInfo).filter(ProcessInfo.pid == pid).first()
    process_info.status = 'Completed'
    process_info.end_time = end_time
    process_info.cpu_usage = process.cpu_percent(interval=0.1)
    process_info.memory_usage = process.memory_info().rss / (1024 * 1024)  # MB cinsinden bellek kullanımı
    db.commit()
    db.refresh(process_info)


# Asal sayı kontrolü
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    print(f"CPU Count: {os.cpu_count()}")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # worker_function fonskiyonunu 1000 defa çalıştırır
        # Bu sayede 1000 defa 10_000_000 sayı arasında asal sayıları bulur
        data = range(1000)
        futures = [executor.submit(worker_function, d) for d in data]
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as exc:
                print(f'İşlem bir hata ile sonlandı: {exc}')


if __name__ == "__main__":
    main()
