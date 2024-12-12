import csv

file_path = input("Enter the CSV file path: ")
columns_to_read = input("Enter the column numbers to read (comma-separated, starting from 1): ").split(',')

# Convert input column numbers to zero-based index
columns_to_read = [int(col.strip()) - 1 for col in columns_to_read]

try:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Read the header row
        
        print(f"Header: {header}")
        print(f"Selected columns: {', '.join([header[col] for col in columns_to_read])}")
        
        for row in csvreader:
            selected_columns = [row[col] for col in columns_to_read]
            print(selected_columns)
            
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


csv file ndaka ennt venda colum mathrm show chyne
