def mult(a,b):
    s = a * b
    return s
print(mult(3,8))

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean
mylist = {"morning" :23, "noon" : 35, "evening" : 30 }
print(mean(mylist))

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 3, 6]))