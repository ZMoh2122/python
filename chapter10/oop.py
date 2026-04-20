# Literal object for a dog
dog1 = {
    "name": "Buddy",
    "age": 5,
    "breed": "Golden Retriever",
    "color": "Golden",
    # Function to make the dog bark
    "bark": lambda: f"{dog1['name']} says Woof!",
    # Function to display dog's details
    "get_details": lambda: f"Name: {dog1['name']}, Age: {dog1['age']}, Breed: {dog1['breed']}, Color: {dog1['color']}",
}

# Access attributes
print(dog1["name"]) # Output: Buddy
print(dog1["age"])  # Output: 5

# Call functions
print(dog1["bark"]()) # Output: Buddy says Woof!
print(
    dog1["get_details"]()
) # Output: Name: Buddy, Age: 5, Breed: Golden Retriever, Color: Golden


print("------------------------------")



# Literal object for a dog
dog2 = {
    "name": "Jack",
    "age": 8,
    "breed": "German Shepherd",
    "color": "Black",
    # Function to make the dog bark
    "bark": lambda: f"{dog2['name']} says Woof!",
    # Function to display dog's details
    "get_details": lambda: f"Name: {dog2['name']}, Age: {dog2['age']}, Breed: {dog2['breed']}, Color: {dog2['color']}",
}

# Access attributes
print(dog2["name"]) # Output: Buddy
print(dog2["age"])  # Output: 5

# Call functions
print(dog2["bark"]()) # Output: Buddy says Woof!
print(
    dog2["get_details"]()
) # Output: Name: Buddy, Age: 5, Breed: Golden Retriever, Color: Golden
