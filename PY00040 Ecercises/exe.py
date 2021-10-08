x = ['pen', 'table', 'book']

x.append('lamp')
print(x)

def y(x, lamp):
    if lamp not in y:
        return x


elements = [
    [1, 4, 6, 7],
    [4, 5, 6],
    [6, 7, 8],
    [],
    ["nodata", "nodata"],
    [1, 3]
            ]
for list in elements:
    if list and isinstance(list[0], int):
        print(list[0])


data = [1, 2, 3, None]
fillme = []

for item in data:
    if item:
        fillme.append(item)
        print(fillme)


def foo(a, b):
    return a + b


import itertools

def foo(mylist):
    list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
    return list(itertools.chain.from_iterable(list_of_lists))
print(list)

numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6, 77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 
            8, 8, 9, 8, 8, 0, 9, 0, 9, 8, 9, 8, 8, 8, 9, 9, 9, 9, 0, 1, 3, 5, 6, 7, 8, 7, 7, 7, 
                5, 7, 7, 5, 4, 5, 6, 5, 56, 4, 3, 4, 8, 6, 6, 7, 8, 8, 9]

a = numbers[::2]
print(sum(a) / len(a))


def f(list):
    middle_index = int(len(list)/2)
    return list[middle_index]
print(list)


import random
def f():
    return [random.randint(1,10) for i in range(1000)]


dict = {"a":1, "b":3, "c":6}
def d(dict):
    return sum(dict.values())
print(sum(dict.values()))


