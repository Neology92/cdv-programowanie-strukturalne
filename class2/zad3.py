def get_values(dict):
    dict["brand"] = input("Wprowadz marke: ")
    dict["model"] = input("Wprowadz model: ")
    dict["capacity"] = input("Wprowadz pojemonsc: ")
    dict["max_velocity"] = input("Wprowadz predkoscMax: ")

def show(dict):
    print("Marka: " + str(dict["brand"]))
    print("Model: " + str(dict["model"]))
    print("Pojemnosc: " + str(dict["capacity"]))
    print("Predkosc maksymalna: " + str(dict["max_velocity"]))



if __name__ == "__main__":
    car = {}
    get_values(car)
    show(car)