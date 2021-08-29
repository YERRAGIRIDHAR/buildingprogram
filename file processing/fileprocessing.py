#read.txt
x = open("friuts.txt")
y = x.read()


with open("friuts.txt") as x:
    y = x.read()
print(y)


x = open("friuts.txt")
print(x.read())


#write.txt
with open("veg.txt", "w") as x:
    x.write("brinjal")

with open("Veg.txt") as x:
    y = x.read()


#append.txt
with open("friuts.txt","a") as x:
    x.write( y)

with open("veg.txt") as x:
    y = x.read()
print(y.strip())

#append when both read & write (txt)
with open("veg.txt", "a+") as x:
    x.seek(0)
    y = x.read()
    x.seek(0)
    x.write("\n")
    x.write(y)
    x.write("\n")
    x.write(y)