def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is Not an Armstrong Number")
