import os

FILE_DIR = 'data'
FILE_NAME = 'test.txt'
FILE_PATH = os.path.join(FILE_DIR,FILE_NAME)

FILE_NAME_JSON = 'test.json'
FILE_PATH_JSON = os.path.join(FILE_DIR,FILE_NAME_JSON)

# option 1
# if not os.path.exists(FILE_DIR):
#     os.mkdir(FILE_DIR)
# if not os.path.exists(FILE_PATH):
#     with open(FILE_PATH, 'w') as fh:
#         fh.write('first line\nsecond line\nthird line')
#         fh.close()

#         fh = open('test.txt', 'r')
#         lines = fh.readlines()
#         print(lines)
# else:
#     print(f'{FILE_PATH} is not exist')

# option2
# if not os.path.exists(FILE_DIR):
#     os.mkdir(FILE_DIR)

# with open(FILE_PATH, mode='a', encoding='utf-8') as fh:
#     chars = fh.tell()
#     fh.seek(chars)
#     fh.write('first line\nsecond line\nthird line')
#     fh = open(FILE_PATH, 'r')
#     lines = fh.readlines()
#     print(lines)

# print(fh)



# option3
# import json
# test_json = {"name": "Mar", "age": 18}

# if not os.path.exists(FILE_DIR):
#     os.mkdir(FILE_DIR)

# with open(FILE_PATH_JSON, mode='r+', encoding='utf-8') as fh:
#     history = json.load(fp=fh)
#     history.append(test_json)
#     fh.seek(0)
#     json.dump(obj=history, fp=fh)


# with open("test.txt", "w") as fh:
#     fh.write("first line\nsecond line\nthird line")

# with open("test.txt", "r") as fh:
#     lines = [el.strip() for el in fh.readlines()]

# print(lines)

# s = "Привіт!"
# utf8 = s.encode()
# print(f"UTF-8: {utf8}")

# utf16 = s.encode("utf-16")
# print(f"UTF-16: {utf16}")

# cp1251 = s.encode("cp1251")
# print(f"CP-1251: {cp1251}")

# s_from_utf16 = utf16.decode("utf-16")
# print(s_from_utf16 == s)

# Перетворення списку чисел у байт-рядок
# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)  # Виведе байтове представлення чисел



# german_word = 'straßeê'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі
# print(german_word.casefold())
# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")



# from pathlib import PurePath

# p = PurePath("/usr/bin/simple.jpg")
# print(p)
# print("Name:", p.name)  
# print("Suffix:", p.suffix) 
# print("Parent:", p.parent)



# from pathlib import Path

# p = Path("test.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) 
# print("Exists:", p.exists()) 


from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("data/test.txt")
absolute_path = relative_path.absolute()
print(absolute_path, relative_path)