import asyncio
import ipaddress
from aioping import ping

async def check_connection(ip):
    # Bu işlem sonsuz döngü içerisinde yapılacaktır.
    # Bu sayede ip adresine sürekli ping gönderilecektir.
    # Verilen ip adresine ping gönderilirken herhangi bir hata oluşursa işlem devam edecektir.
    # Ping sonucu başarılı olursa ip adresi konsola yazdırılacaktır.
    while True:
        try:
            # Belirtilen ip adresine ping gönderiyoruz.
            response = await ping(str(ip), timeout=5)            
        except TimeoutError as e:
            # Ping sonucu başarısız olursa ip adresi konsola yazdırıyoruz.
            print(f"{ip} is unreachable.")
        except Exception as _:
            # Burada ekstra hata kontrolleri yapılabilir.
            pass

async def main():
    # 172.29.0.1/23 ağında 510'u kullanılabilir olan 512 adet ip adresi bulunmaktadır.
    # Bu ip adreslerinin her birine aynı andaping gönderebilmek için asyncio kütüphanesini kullanıyoruz.
    # Bu sayede aynı anda birden fazla ip adresine ping gönderebiliyoruz.
    network = ipaddress.ip_network('172.29.0.1/23', False)
    tasks = [check_connection(device) for device in network.hosts()]
    await asyncio.gather(*tasks)

asyncio.run(main())