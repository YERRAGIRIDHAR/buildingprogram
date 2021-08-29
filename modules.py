import time
import os

while True:
    if os.path.exists("veg.txt"):
        with open("veg.txt") as x:
            print(x.read())
    else:
        print("No file ya yes.")
    time.sleep(5)
