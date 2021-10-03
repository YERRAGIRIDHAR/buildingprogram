import time
from datetime import datetime as dt

hosts_temp = r"E:\PYTHON projects\PY000038 Building a Website Blocker\hosts" # or we can write simly "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "dub119.mail.live.com", "www.dub119.mail.live.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16): # This statement executes only btw 8am and 4pm
        print("Working hours....")
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content: # If website list in the content then it will pass
                    pass
                else: 
                    file.write(redirect +" "+ website + "\n") # If not it will add in btw 8 and 5pm

    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0) # To place the curser in the starting of the file
            for line in content:
                if not any(website in line for website in website_list): # If any item in website list is not in line(host file) then it will write every line which is not having website list
                    file.write(line)
            file.truncate() # Check with every line and truckated(ended) at 21 the end because line present in the last 3 lines
        print("Fun hours.....")
    time.sleep(5) #Script will sleep for 5 seconds