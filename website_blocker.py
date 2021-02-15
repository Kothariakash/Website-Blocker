import time
from datetime import datetime as dt

host="hosts"
redirect="127.0.0.1"
blocked_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print("working hours...")
        with open (host,'r+') as file:
            content=file.read()
            for website in blocked_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open (host,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in blocked_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
