# original_list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# doubled = []
# for x in original_list:
#     doubled.append(x*2)


# original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# doubled = [x*2 for x in original_list if x < 5]
# print(doubled)


# odd_numbers = []
# for x in range(10):
#     if x % 2 != 0:
#         odd_numbers.append(x)
# print(odd_numbers)


# even_numbers = []
# for x in range(10):
#     if x % 2 != 0:
#         even_numbers.append(x)
#         print(even_numbers)


# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)


# cartesian_product = []
# for x in range(3):
#     for y in range(2):
#         cartesian_product.append((x, y))

# print(cartesian_product)


# Define number of rows and columns
rows = 3

# # Outer loop for rows
# for i in range(1, 11):
#    for j in range(1, 11):
#     print(i, j)


# # Outer loop for rows
# for i in range(3):
#     # Inner loop for columns
#     for j in range(3):
#         print(f"({i}, {j})", end=" ")
#     print()  # Move to the next line after each row


# odd_even = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# print(odd_even)

# ["even", "odd", "even", "odd", "even"]


# names = ["alice", "bob", "charlie"]
# # capitalized_names = [name.capitalize() for name in names]
# capitalized_names = []
# for name in names:
#     capitalized_names.append(name.upper())
# print(capitalized_names) 


def append_zak(param):
    return param.upper()
result = append_zak("Minnesota")
print(result)


names = ["alice", "bob", "charlie"]
capitalized_names = [append_zak(name) for name in names]
print(capitalized_names)
# Output: ['Alice', 'Bob', 'Charlie']









