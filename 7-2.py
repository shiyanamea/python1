input_file = input("Enter the input file path: ")
output_file = input("Enter the output file path: ")

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for i, line in enumerate(infile, start=1):
            if i % 2 != 0:
                outfile.write(line)

    print(f"Odd lines from {input_file} have been copied to {output_file}")

except FileNotFoundError:
    print(f"The file {input_file} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


1>main acc
2>inputfile
3>outputfile
