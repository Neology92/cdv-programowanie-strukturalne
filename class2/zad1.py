country = ['first', 'second', 'thrid', 'fourth', 'fifth']

for i in range(0,2):
    print('List: ', str(country))
    new_elem = input('Enter new element: ')
    country.append(new_elem)

print("==========")
print("   MENU")
print("==========")
print("1) Wyswietl pierwsze 3 elementy")
print("2) Wyswietl element listy, ktory dodalem")
print("3) Wyswietl zawartosc listy")
print("4) Wyczysc zawartosc listy")
print("5) Znajdz element w liscie, ktory poda uzytkownik")
print("---------")
choice = int(input("Choice: "))

if(choice == 1):
    print(country[:2])
elif(choice == 2 ):
    print(country[-2:])
elif(choice == 3 ):
    print(country)
elif(choice == 4 ):
    country.clear()
elif(choice == 5 ):
    to_find = input("Enter elem to find: ")
    i = 0
    for elem in country:
        if(elem == to_find):
            print("Found on index " + str(i))
        i += 1
else:
    print("Wrong choioce")

print(country)