from collections import Counter


# text = "missisipi"

# chars = Counter(text)
# print(chars)
# # print(type(chars))
# # print(dir(chars))
# print(chars.most_common(1))



def is_anagram(world1, world2):
    print(Counter(world1))
    print(Counter(world2))
    return Counter(world1) == Counter(world2)

print(is_anagram("abs", "bsa"))