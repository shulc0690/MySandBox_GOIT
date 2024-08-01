# age = int(input("Age >>> "))

# message = f"You are {age}"

# if age >= 18:
#     print(message)
# else:
#     print("You not 18")
# def factorial(n: int = 1):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

import random

def get_random_car_plate():
    car_plate = ''

    set_of_letters = ['A','B','C','E']
    
    first = random.choices(set_of_letters, k=2)
    second = random.randint(1000,9999)
    third = random.choices(set_of_letters, k=2)
    
    car_plate += "".join(first) + ' '
    car_plate += str(second) + ' '
    car_plate += "".join(third)
    return car_plate


print(get_random_car_plate())