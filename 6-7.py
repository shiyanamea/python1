def check_number():
    try:
        # Prompt the user to enter a number
        number = float(input("Enter a number: "))
        
        # Check if the number is positive or zero
        if number >= 0:
            print(f"The number you entered is: {number}")
        else:
            # Raise ValueError if the number is negative
            raise ValueError("The number cannot be negative.")
    
    except ValueError as e:
        # Handle ValueError and display the error message
        print(f"Error: {e}")

# Call the function
check_number()
