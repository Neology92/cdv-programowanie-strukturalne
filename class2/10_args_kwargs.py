# def sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result

# def show_dict(**kwargs):
#     for name, val in kwargs.items():
#         print(f"{name} - {val}")

# def get_names(list):
#     i = 1
#     while True :
#         user_input = input("Enter name (Empty to continue, min 3): ")
#         if user_input == "" and i > 3: 
#             break;
#         else:
#             list.append(user_input)
#             i += 1

# def show_names(args):
#     print("Name1: " + str(args[0]))
#     print("Name2: " + str(args[1]))
#     print("Name3: " + str(args[2]))
#     if len(args) > 3:
#         print("Other names: " + str(args[3:]))


def show(first, second, thrid, **options):
    if options.get('action') == 'add':
        res = first + second + thrid
    elif options.get('action') == 'multiply':
        res = first * second * thrid
        
    if options.get('element') == 'first':
        elem = first
    elif options.get('element') == 'second':
        elem = second
    
    print(f"Results is {res}")
    print(f"Element is {elem}")
        


if __name__ == "__main__":
    show(1, 2, 5, action = 'add', element = "second")
    show(1, 2, 5, action = 'multiply', element = "first")
    # result = sum(1, 23, 4, 45, 2, 4, -55)
    # print(result)
    # show_dict(name1 = "a", name2="vs")
    # names = []
    # get_names(names)
    # show_names(names)