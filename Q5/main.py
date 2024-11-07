import paramiko
import ipaddress
import asyncio

# ssh client sınıfımız
class SSHClient:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password

    def _create_ssh_client(self, host, port=22):
        # Belirtilen host'a ssh bağlantısı oluşturur
        print(f"Creating SSH connection to {host}")
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=self.username, password=self.password, timeout=3)
            return client
        except Exception as e:
            print(f"SSH bağlantısı kurulamadı {host}: {e}")
            return None

    def send_command_sync(self, host, command):
        # Belirtilen host'a gönderilen komutu çalıştırır
        client = self._create_ssh_client(host)
        if client:
            stdin, stdout, stderr = client.exec_command(command)
            print(f"Running command on {host}: {command}")
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            client.close()
            if error:
                print(f"Error on {host}: {error}")
            return output
        return None

    async def send_command(self, host, command):
        # Belirtilen host'a gönderilen komutu çalıştırır
        # Asenkron olarak çalışır
        # Bu sayede aynı anda birden fazla host'a komut gönderilebilir
        return await asyncio.to_thread(self.send_command_sync, host, command)

    async def send_commands_to_network(self, network_range, command, port=22):
        # Belirtilen ağdaki tüm hostlara belirtilen komutu gönderir
        network = [str(ip) for ip in ipaddress.ip_network(network_range, False).hosts()]
        tasks = []
        for host in network:
            tasks.append(self.send_command(host, command))
        return await asyncio.gather(*tasks)

async def main():
    ssh_client = SSHClient(username="username", password="password")
    network_range = "172.29.0.1/16"
    command = "pwd"
    await ssh_client.send_commands_to_network(network_range, command)

asyncio.run(main())
