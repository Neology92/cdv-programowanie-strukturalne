import random

a = int(input("Get low value: "))
b = int(input("Get high value: "))

if a > b:
    buff = b
    b = a
    a = buff

my_list = []
for i in range(0, 4):
    my_list.append(random.randint(a, b))   
    print("Number" + str(i) + ": " + str(my_list[i]))
