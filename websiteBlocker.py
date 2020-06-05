import time
from datetime import datetime as dt
hosts_file = r"C:\Windows\System32\drivers\etc\hosts" 
redirect_to = "127.0.0.1"
website_to_block = ["www.gmail.com","gmail.com","www.facebook.com","facebook.com"]
while True:
    #to check working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,19) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,21):
        print("you are not allowed to use these sites on working hours")
        with open("../Application4_website_blocker/hosts","r+") as host_tem:
            data = host_tem.read()
            print(data)
            for item in website_to_block:
                if item in data:
                    pass
                else:
                     host_tem.write(redirect_to + " " + item +"\n")
        print("Before_sleep1")
    else:
        with open("../Application4_website_blocker/hosts","r+") as host_tem:
            data = host_tem.readlines()
            host_tem.seek(0)
            for line in data:
                if not any(item in line for item in website_to_block):
                    host_tem.write(line)
                host_tem.truncate() 
        print("your working hour is finished ! hurrayy")
    time.sleep(6)
    print("after sleepv 2")