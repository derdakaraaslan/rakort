import asyncio
import asyncssh
import ipaddress
import time

async def try_ssh_connection(ip, port=22, username="user", password="password"):
    try:
        # Belirtilen ip adresine ssh bağlantısını deniyoruz.
        # Burada timeout süresi 2 saniye olarak belirlenmiştir. Bu süre ağ durumuna göre belirlenmelidir. 
        # Bu sürenin artılırması projenin çalşıma süresini uzatacaktır.
        await asyncio.wait_for(asyncssh.connect(
            host=str(ip),
            port=port,
            username=username,
            password=password
        ), timeout=2)
        # Bağlantı başarılı olursa ip adresini konsola yazdırıyoruz.
        print(f"{ip} connected.")
    except (asyncssh.Error, OSError) as _:
        # Bağlantı başarısız olursa herhangi bir işlem yapılmamakta.
        pass

async def main():
    # 172.29.0.1/16 ağında 65534 kullanılabilir ip adresi bulunmaktadır.
    # Bu ip adreslerinin her birine aynı anda bağlantı denemek için asyncio kütüphanesini kullanıyoruz.
    # Bu sayede aynı anda birden fazla ip adresine bağlantı deneyebiliyoruz. 
    # Karşı cihazdan yanıt beklerken diğer cihazlara bağlantı denenebilmektedir.
    # Bu sayede işlem süresi kısalacaktır.
    network = ipaddress.ip_network('172.29.0.1/16', False)
    tasks = []
    tasks = [try_ssh_connection(device) for device in network.hosts()]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Geçen süre: {end - start} saniye")
