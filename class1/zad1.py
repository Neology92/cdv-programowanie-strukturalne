print("-----------------")
print("User1")
print("-----------------")

u1_name = input("Enter your name: ")
u1_surname = input("Enter your surname: ")
u1_age = int( input("Enter your age: ") )

print("-----------------")
print("User2")
print("-----------------")
u2_name = input("Enter your name: ")
u2_surname = input("Enter your surname: ")
u2_age = int( input("Enter your age: ") )
print("====================")
print(f"User1: {u1_name} {u1_surname} {u1_age}")
print(f"User2: {u2_name} {u2_surname} {u2_age}")
avg = (u1_age + u2_age) / 2
print(f"Avg age: {avg:.2f}")
