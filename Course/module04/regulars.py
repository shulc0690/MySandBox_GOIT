import re
# search
# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)


# findall
# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)

# text = "Вивчення Python може бути веселим.: example@example1.com"
# pattern = r"(\w+)@(\w+)(\.\w+)"
# match = re.findall(pattern, text)

# print("Знайдено:", match.group(3))

# sub
# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# match = re.findall(pattern, phone)
# print(match)
# print(formatted_phone)


# split
text = "Python - це проста, але потужна мова програмування."
# pattern = r"\s+"
pattern = r"[;,\-:!\s]+"
words = re.split(pattern, text)

print(words) 

text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)

# re.search(pattern, string) - використовується для пошуку першого входження шаблону в рядку. Повертає об'єкт Match, якщо відповідність знайдена.
# re.findall(pattern, string) - знаходить всі входження шаблону в рядку. Повертає список всіх знайдених відповідностей.
# re.sub(pattern, repl, string) - замінює всі входження шаблону в рядку на інший рядок. Використовується для модифікації та форматування тексту.
# re.split(pattern, string) - розбиває рядок за заданим шаблоном. Повертає список рядків, отриманих після розділення.
# Використання регулярних виразів вимагає розуміння їхнього синтаксису та особливостей. Спеціальні символи, такі як *, +, ?, квадратні та круглі дужки, 
# мають конкретні функції у регулярних виразах. Розуміння цих елементів дозволяє виконувати складні операції пошуку та редагування з текстом.
# Коректне застосування регулярних виразів може значно спростити обробку тексту, автоматизацію задач та вирішення складних проблем обробки даних.