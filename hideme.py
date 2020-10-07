import  time,os,requests
while 1:
    time.sleep(4)
    os.system("sudo systemctl restart tor")
    time.sleep(4)
    session = requests.session()
    session.proxies = {"http":"socks4://127.0.0.1:9050","https":"socks4://127.0.0.1:9050/"}
    print(session.get("http://httpbin.org/ip").text)
