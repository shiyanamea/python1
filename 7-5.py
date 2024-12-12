import csv

# Function to take user input for the dictionary
def get_user_input():
    data = []
    while True:
        name = input("Enter name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        age = input("Enter age: ")
        city = input("Enter city: ")

        # Create a dictionary for the current row
        data.append({"name": name, "age": age, "city": city})

    return data

# File path for the CSV file
file_path = "l7pgm5_data.csv"

# Get user input
data = get_user_input()

# Writing the dictionary to the CSV file
try:
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
        writer.writeheader()  # Write the header
        writer.writerows(data)  # Write the rows of data

    print(f"Data has been written to {file_path}")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Reading the CSV file and displaying its content
try:
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        print("\nContent of the CSV file:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
