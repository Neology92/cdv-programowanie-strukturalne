names = {}

for i in range(0, 3):
    elem = input("Enter name: ")
    names[i] = elem

print(names)

for key, value in names.items():
    print(f"imie{key} = {value}")