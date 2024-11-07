import re
import paramiko
import time

def parse_logs(log_data):
    results = []
    current_section = []

    for line in log_data.splitlines():
        # TIME kelimesine göre bölümleme yapıyorum
        if line.startswith("TIME"):
            if current_section: # Eğer bir section varsa ve TIME kelimesi bulunduysa, artık bu section bitmiştir.
                result = check_section(current_section)
                if result:
                    results.append(result)
                current_section = []

        current_section.append(line)

    # Son sectionu kontrol etmek için
    if current_section:
        result = check_section(current_section)
        if result:
            results.append(result)
    
    return results

def check_section(section):
    section_text = "\n".join(section)
    # Regex ile DHCPREQUEST arıyorum
    if re.search(r"OPTION:\s*53\s*\(\s*1\)\s*DHCP\s*message\s*type\s*3\s*\(DHCPREQUEST\)", section_text):
        print("DHCPREQUEST bulundu")
        # Gerekli bilgileri regex ile arıyorum
        client_identifier = re.search(r"Client-identifier\s*(.+)", section_text)
        request_ip = re.search(r"Request IP address\s*(.+)", section_text)
        vendor_class = re.search(r"Vendor class identifier\s*(.+)", section_text)
        host_name = re.search(r"Host name\s*(.+)", section_text)

        result = {
            "Client-identifier": client_identifier.group(1).strip() if client_identifier else None,
            "Request IP address": request_ip.group(1).strip() if request_ip else None,
            "Vendor class identifier": vendor_class.group(1).strip() if vendor_class else None,
            "Host name": host_name.group(1).strip() if host_name else None
        }
        return result
    return None

def write_to_file(data, filename="parsed_data.txt"):
    with open(filename, "a") as file:
        for entry in data:
            file.write(str(entry) + "\n")

def listen_via_ssh(command="cat /var/log/dhcp.log"):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect('host_adresi', username='kullanıcı_adı', password='şifre', port=22)
    
    _, stdout, _ = client.exec_command(command)
    
    start_time = time.time()
    log_data = ""
    
    while time.time() - start_time < 300:
        if stdout.channel.recv_ready():
            line = stdout.readline()
            log_data += line
            if line.startswith("TIME"):
                parsed_data = parse_logs(log_data)
                if parsed_data:
                    write_to_file(parsed_data)
                log_data = ""

    client.close()

with open("data.txt", "r") as file: # Kodu test edebilmek için data.txt dosyası oluşturup içine log verilerini kopyaladım
    log_data = file.read()
parsed_data = parse_logs(log_data)
if parsed_data:
    write_to_file(parsed_data)
log_data = ""

# listen_via_ssh()