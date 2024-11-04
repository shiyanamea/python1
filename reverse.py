# Input from user
number = int(input("Enter a number to reverse: "))
reverse = 0  # Variable to store the reversed number

# While loop to reverse the number
while number > 0:
    digit = number % 10  # Get the last digit
    reverse = reverse * 10 + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number

# Output the reversed number
print(f"The reversed number is: {reverse}")
