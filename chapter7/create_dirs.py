import os

# Step 1: Define the directory and file name
directory = "example_folder/subfolder"
file_name = "example_file.txt"

# Step 2: Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory) # Create the directory and any intermediate directories
    print(f"Directory '{directory}' created.")

# Step 3: Create and write to the file
file_path = os.path.join(directory, file_name) # Combine directory and file name into a full path
with open(file_path, "w") as file:
    file.write("This file is created in a specific directory.\n")
    file.write("Hello, World!")

print(f"File '{file_path}' created successfully.")
