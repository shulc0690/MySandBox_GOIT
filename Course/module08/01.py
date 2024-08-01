# lst = [1, 4, 9, 11, 400]
# c = map(lambda x: x**2, lst)
# print(c)
# a = filter(lambda x: x < 100, c)

# print(list(a))



# nums1 = [1, 2, 3, 1]
# nums2 = [4, 5, 6, 7]
# sum_nums = list(map(lambda x, y: x + y, nums1, nums2))

# print(list(sum_nums))


first_names = ["Ivan", "Nick", "John"]
last_names = ["Walker", "Doe", "Crawn"]
grades = [77, 83, 90]


print(list(zip(first_names, last_names, grades)))

last_names.pop()
print(list(zip(first_names, last_names, grades)))