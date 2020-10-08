#Real quick note. YOU MUST RUN THIS AS ROOT
import requests,socket,struct, time, os
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
while True:
    packet = s.recvfrom(65565);packet = packet[0]
    ip_header = packet[0:20];iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
    version_ihl = iph[0];ihl = version_ihl & 0xF;
    iph_length = ihl * 4;tcp_header = packet[iph_length:iph_length+20]
    tcph = struct.unpack('!HHLLBBHHH' , tcp_header);doff_reserved = tcph[4];tcph_length = doff_reserved >> 4
    h_size = iph_length + tcph_length * 4;data = packet[h_size:];looking_for = "HT"
    if(looking_for in str(data)):
        os.system("sudo systemctl restart tor");time.sleep(10)
        print(requests.get("http://httpbin.org/ip",proxies={"http":"socks4://127.0.0.1:9050","https":"socks4://127.0.0.1:9050/"}).text)
