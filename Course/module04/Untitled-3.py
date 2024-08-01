# def find_ma_vowels(text):
#     vowels = 'aeiou'
#     res =''
#     for char in text:
#         if char.lower() in vowels:
#             res += char
#         else:
#             res += '.'
#     chains = res.split(".")
#     return max(chains, key=len)


# text = "asd ad asdassda rwer we  te OleEeoooeeh"        

# res = find_ma_vowels(text)
# print(res)

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(ord('1'))