def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")
