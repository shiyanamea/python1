def compare(s1, s2, n):
    # Compare the first n characters of both strings
    return s1[:n] == s2[:n]

# Test the function
s1 = "hello"
s2 = "helicopter"
n = 3
# we gave n=3 so s1=hel s2=hel true
result = compare(s1, s2, n)
print("Are the first", n, "characters the same?", result)

