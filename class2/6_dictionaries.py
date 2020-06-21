# dict = {
#     'key1': 'value1',
#     'key2': 'value2',
#     'key3': 'value3',
#     'key4': 'value4',
#     'key5': 'value5'
#     }


pracownik = {
    "imie": "Andrzej",
    "nazwisko": "Kowal",
    "miasto": "Poznan",
    "wiek": 44,
    "imionaDzieci": ["Gabi", "Julia"],
    "imionaRodzicow": ["Zych", "Anna"],
}

print(pracownik["imionaDzieci"][0])
print(pracownik["imionaDzieci"][1])

pracownik['height'] = 100
pracownik['weight'] = 80

# print(pracownik)
print(type(pracownik))

key = 'wiek'
if key in pracownik:
    del pracownik[key]

# print(pracownik)
print("---")

for key, value in pracownik.items():
    print(f"{key} = {value}")

print(pracownik.keys())

print(pracownik.get('wiek', 'Brak klucza o nazwie wiek'))
pracownik["wiek"] = 45
print(pracownik.get('wiek', 'Brak klucza o nazwie wiek'))