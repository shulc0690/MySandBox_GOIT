# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Cat(Animal):
    # def __init__(self, nickname: str, weight: int) -> None:
    #     super().__init__(nickname, weight)

    # def say(self):
    #     return f"Meow"
    
# cat = Cat("Simon",10)

# 
# 
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Dog(Animal):
#     def __init__(self, nickname: str, weight: int, breed: str ) -> None:
#         super().__init__(nickname, weight)
#         self.breed = breed

#     def say(self):
#         return f"Woof"
    
# dog = Dog("Barbos", 23, "labrador")

# 
# 
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
                        
#     def info(self):
#         return {"name": self.name, "age": self.age, "address": self.address}
        

# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner: Owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()


# owner = Owner("Yurii", 26, "Ave")
# cat = Dog("Simon", 4, "labrador", owner)
# print(cat.who_is_owner())


# 
# 
# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"
    
# class CatDog(Cat, Dog):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# class DogCat(Dog, Cat):
#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# cd = CatDog("Simon", 10)
# dc = DogCat("Other",5)
# print(cd.say(), dc.say())

# 
# 
# from collections import UserDict

# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for key in self.data:
#             if self.data[key] == value:
#                 keys.append(key)
#         return keys

# 
# 
# from collections import UserList

# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         sum = 0
#         for value in self.data:
#             if int(value) > 0:
#                 sum = sum + int(value) 
#         return sum

# countable = AmountPaymentList([1, '2', 3, '4'])
# print(countable.amount_payment())

# 
# 
# from collections import UserString

# class NumberString(UserString):
#     def number_count(self):
#         count = 0
#         for char in self.data:
#             if char.isdigit():
#                 count += 1
#         return count
    
# countable = NumberString("sdf sdf 1fdf 2f2 3 fdf s6")
# print(countable.number_count())

# 
# 
# class IDException(Exception):
#     pass

# id_list = ["23"]

# def add_id(id_list: list, employee_id: str):
#     if not employee_id.startswith('01'):
#         raise IDException()
#     id_list.append(employee_id)
#     return id_list

# updated_list = add_id(id_list,'013')
# print(updated_list)

# 
# 
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id, 
                "name": name, 
                "phone": phone, 
                "email": email, 
                "favorite": favorite})
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None
    
    def remove_contacts(self, id):
        self.contacts = [contact for contact in self.contacts if contact["id"] != id]
            

c = Contacts()
c.add_contacts("Iva", "+5656", "mail", True)
c.add_contacts("Eva", "+3656", "email", False)
c.add_contacts("Wylie Pope", "+'(692) 802-2949", "est@utquamvel.net", False)
all = c.list_contacts()
print(all)

c.remove_contacts(2)
all = c.list_contacts()
print(all)