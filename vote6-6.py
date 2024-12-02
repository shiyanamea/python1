def can_cast_vote():
    # Get user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Check if age is greater than or equal to 18
    if age >= 18:
        print(f"{name}, you are eligible to vote.")
    else:
        print(f"{name}, you are not eligible to vote yet.")

# Call the function
can_cast_vote()
