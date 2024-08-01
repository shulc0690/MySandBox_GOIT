# class Point:
#     def __init__(self, x: float, y: float, z: float = 0):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __repr__(self):
#         return f"Point(x={self.x}, y={self.y})"

# original_point = Point(2, 3)
# print(repr(original_point))  

# # Використання рядка, повернутого __repr__, для створення нового об'єкта
# new_point = eval(repr(original_point))
# print(new_point, dir(new_point))


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print(human)