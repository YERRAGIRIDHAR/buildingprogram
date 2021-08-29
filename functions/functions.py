def area(a, b):
    return a*b

print(area(2, 5))

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)
print(foo("raju", "naresh", "giri"))


def foo(args):
    if isinstance(args, str):
        x = args.upper
        return x.sorted()
    
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=2,b=3,c=5))


def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
