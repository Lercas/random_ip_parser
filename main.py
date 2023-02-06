import socket
import random
import threading

def random_ip():
    return str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))

def ping(host):
    try:
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        return False

def check_host(host):
    is_reachable = ping(host)
    if is_reachable:
        print(host, "is reachable")
    else:
        print(host, "is not reachable")

while True:
    random_host = random_ip()
    print("Рандомный IP:", random_host)
    t = threading.Thread(target=check_host, args=(random_host,))
    t.start()
