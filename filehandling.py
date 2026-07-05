import os
from textwrap import indent

# file_path = "stuff/test.txt"
# if os.path.exists(file_path):
#     print(f"The file {file_path} exists")


# wriiting files
txt_data = "i like pizza"
file_path = "laala.txt"

# try:
#     with open(file = file_path, mode = "w") as file:
#         file.write(txt_data)
#         print(f"Data written to {file_path}")

# except Exception as e:
#     print(f"An error occurred while writing to the file: {e}")

try:
    with open(file = file_path, mode = "a") as file:
        file.write("\n" + txt_data)
        print(f"Data written to {file_path}")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")




txt_data = ["prahar","sravan","sai"]
file_path = "lists.txt"
try:
    with open(file = file_path, mode = "w") as file:
        for employee in txt_data:
            file.write(employee + "\n")
        print(f"Data written to {file_path}")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


# json files
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:/Users/HP/Desktop/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4) 
    print(f"JSON file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")



# csv files
import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

file_path = "C:/Users/HP/Desktop/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(employees)

    print(f"CSV file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")



# reading files
# txt
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")

# json
import json

file_path = "C:/Users/HP/Desktop/input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")

# csv
import csv

file_path = "C:/Users/HP/Desktop/input.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)

        for line in content:
            print(line)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")