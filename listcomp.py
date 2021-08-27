temps = [223, 176, 823]
new_temps = [temp/10 for temp in temps]
print(new_temps)
 
temps = [223, 176, 823]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)

print(new_temps)

def foo(lst):
    return [i for i in lst if i > 0]

temps = [223, 176, -7643, 823]

# new_temps = [temp/10 if temp != -7643 else 0 for temp in temps]
# print(new_temps)
