monday_temperatures = (1, 4, 5)
s = list(monday_temperatures)
s.append(9)
print(s)

#For Loop

citylist = ["nalgonda", "hyderabad","suryapetta","miryalaguda"]

for city in citylist:
    print(city)

citylist = ["nalgonda", "hyderabad","suryapetta","miryalaguda"]

for city in citylist:
    print(city)
    if city == "suryapetta":
        break
    

citylist = ["nalgonda", "hyderabad","suryapetta","miryalaguda"]

for city in citylist:
    if city == "hyderabad":
        continue
    print(city)

citylist = ["nalgonda", "hyderabad","suryapetta","miryalaguda"]

for city in citylist:
    print(city)
else:
    print('city is completed')

for num in range(70):
    print(num)


for num in range(50,70):
    print(num)

for num in range(30,70,5):
    print(num)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for keys, values in phone_numbers.items():
    print("{} has as phone number {}".format(keys, values))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print(f"{key} : {value}")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))


#WHILE LOOP

x = 7
while x < 16:
    x += 1
    print(x)

username = ''
while username != "pypy":
    username =input("enter the name:")