# class NameTooShortError(Exception):
#     pass

# class NameStartsFromLowError(Exception):
#     pass

# def enter_name():
#     name = input("Enter name: ")
#     if len(name) < 3:
#         raise NameTooShortError("Name is too short, need more than 2 symbols")
#     if not name[0].isupper():
#         raise NameStartsFromLowError("Name should start from capital letter")
#     return name

# if __name__ == "__main__":
#     try:
#         name = enter_name()
#         print(f"Hello, {name}")
#     except (NameTooShortError, NameStartsFromLowError) as e:
#         print(e)

# 
# exception parametrized
class NameNotValidError(ValueError):
    def __init__(self, name) -> None:
        super().__init__(f'Name not valid for name {name}')


# try:
#     1 / 0
# except ZeroDivisionError as e:
#     raise ExceptionGroup('We have some problems', [NameNotValidError('Name'), e])

name = 'Igor'
raise NameNotValidError(name)

# raise ExceptionGroup('We have some problems', [NameNotValidError(name), ])