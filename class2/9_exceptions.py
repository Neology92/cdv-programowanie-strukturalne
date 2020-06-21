# def div(x, y):
#     try:        
#         return round(x / y, 2)
#     except ZeroDivisionError:
#         print("Err: Couldn't divide by 0!")

# print(div(3,7))


while(True):
    try:
        val = int(input("Enter int number: "))
        break
    except ValueError:
        print("Not an int, ty again!")