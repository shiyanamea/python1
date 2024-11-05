# Function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base case: the first two numbers in the Fibonacci series are 0 and 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

# Function to print Fibonacci series up to the nth number
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

# Test the function
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
print_fibonacci_series(num_terms)

