# Take the filename as user input
filename = input("Enter the file name: ")

# Open the file and read lines into a list
with open(filename, 'r') as file:
    lines = file.readlines()
print(lines)

