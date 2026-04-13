# import csv

# # Reading a CSV file
# with open('uk.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row) # Each row is a list 



import csv

# Writing to a CSV file
data = [['Name', 'Age', 'City'], ['Zakir', 19, 'London'], ['John', 30, 'New York']]
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

