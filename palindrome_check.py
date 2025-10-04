def is_palindrome(s):
    # Normalize the string (optional: lowercasing for case-insensitive check)
    s = s.lower()
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")
