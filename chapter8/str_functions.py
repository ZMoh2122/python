# len() Returns the length of the string
# count = len("hello") 
# print(count)


# greetings = "Hello"
# count = len(greetings)
# print(count)
# print("Hello".upper())


# # Checks if all characters are alphabetic
# "abc".isalpha() # True
# is_alphebetic = "abc".isalpha()
# print("abc".isalpha())


# # Checks if all characters are digits
# digit = "123".isdigit()
# print(digit)
# # print("1r3".isdigit()) # False


# # Checks if all characters are whitespace
# space = " ".isspace()
# print(space)
# # print(" ".isspace())


# # Checks if all characters are lowercase
# lower = "Abc".upper()
# # print("abc".islower())
# print(lower)


# upper = """ABC
# America
# Messi
# """.upper()
# print(upper)


# og_str = "hello"
# first_letter_caps = og_str.capitalize()
# print(first_letter_caps)
# print(og_str)
# # print("hello".capitalize())


# #capitalizes the first letter of each word
# text = "hello world ,this is another world"
# new_text = text.title()
# print(text)
# print(new_text)


# # Removes leading/trailing whitespace
# name = " Zakariya "
# clean_name = name.strip() # 'Zakariya'
# print (name)
# print(clean_name)


# # removes leading whitespaces
# last_name = "  Mohamed"
# clean_last_name = last_name.lstrip()
# print(last_name)
# print(clean_last_name)


# last_name = "Mohamed "
# clean_last_name = last_name.lstrip()
# print(last_name)
# print(clean_last_name)


# Replaces occurrences of a substring
# og_text = "hello world" # 'hello Python'
# new_text = og_text.replace("world", "Python")
# print(og_text)
# print(new_text)


# Returns the lowest index of substring
# text = "hello world it is me zakman lol i am cool"
# result = text.find("zakman")
# # print(text)
# print(result)


# # Returns the highest index of substring
# text = "hello hello why me"
# result = text.find("hello")
# print(result) 


# # Like find() but raises ValueError if not found
# text = "hello i say no"
# result = text.index("n") 
# print(result)


# Checks if string starts with a substring
text = "bello"
# if(text.startswith("he")):
#     print("yes it starts with")
# else: 
#     print("no it does not start with")


# text = "hello world.this is Zakariya"

# if(text.endswith("ya")):
#     print("yes it ends with ")
# else:
#     print("no it doesn't end with")



# Using str.format() with placeholders and longer words
animal = "quick brown fox"
action = "leaps"
the_other_animal = "dog"

formatted_string = "{} {} gracefully over the lazy {}".format(animal, action, the_other_animal)
print(formatted_string) 
# Output: "quick brown fox leaps gracefully over the lazy dog"
















