number = int(input("Enter a number to find its factors: "))
factors = []  # List to store factors
i = 1  # Start from 1

# While loop to find factors
while i <= number:
    if number % i == 0:  # Check if i is a factor
        factors.append(i)  # Add i to factors list
    i += 1  # Increment i

# Output the factors
print(f"Factors of {number} are: {factors}")
