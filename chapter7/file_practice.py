# # Step 1: Open a file in 'w' mode
# with open("example.txt", "w") as file:
#  file.write("Zakariya")
#  file.write("Mubaarak")

# # Step 3: Close the file
# file.close()




# with open("text.txt", "r") as file:
#     content = file.read()
#     print(content)


# # Step 1: Create an empty file
# with open("empty_file.txt", "w") as file:
#     pass  # No content is written

# # File "empty_file.txt" is created and remains empty.


# Step 1: Prepare a list of lines
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

# # Step 2: Write all lines to a file
# with open("multi_lines.txt", "w") as file:
#     file.writelines(lines)

# # File "multi_lines.txt" is created with multiple lines.



import os

# Step 1: Define the file name
file_name = "check_exists.txt"

# Step 2: Check if the file exists
if not os.path.exists(file_name):
    # Step 3: Create the file
    with open(file_name, "w") as file:
        file.write("This file was created because it didn't exist.\n")
else:
    print(f"{file_name} already exists!")

# File "check_exists.txt" is created only if it doesn't exist.



