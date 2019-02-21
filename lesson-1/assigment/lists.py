numbers = []
for i in range(10000):
    numbers.append(i)

print(numbers)

# [0,1,2,3,4,5,6,7,8]
numbers_2 = [i for i in range(9)]
print(numbers_2)
# [-10, -9, -8, -7, -6, -5]
numbers_3 = [i for i in range(-10, -4)]
print(numbers_3)
# [0, 3, 6, 8, 12]
print([i for i in range(0, 13, 3)])
# [10, 8, 6, 4, 2]
print([i for i in range(10, 1, -2)])
# [0, -1, -2, -3, -4, -5]
print([i for i in range(0, -6, -1)])

