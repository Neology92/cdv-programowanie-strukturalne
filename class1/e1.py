import random

a = int(input("Get min value: "))
b = int(input("Get max value: "))

if a > b:
    print("Error: Min value must be greater than max val...")
    exit()

my_list = []
for i in range(0, 4):
    my_list.append(random.randint(a, b))   
    print(f"Number{i}: {my_list[i]}" )
