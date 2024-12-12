import csv

file_path = input("Enter the CSV file path: ")

try:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


csv file ndaknm ayil detai;s kodknm
