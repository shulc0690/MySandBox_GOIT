import random

coin = {1: 'Reshka', 2: 'Orel'}

sequence = []
count_0 = 0
count_p = 0

while count_0 < 4 and count_p < 4:
    choice = random.randint(1,2)
    if choice == 1:
        count_p += 1
        count_0 = 0
    else:
        count_0 += 1
        count_p = 0
    name = coin[choice]
    sequence.append(name)

print(sequence)
print(len(sequence))