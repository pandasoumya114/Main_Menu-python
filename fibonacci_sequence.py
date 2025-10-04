def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example usage
num = int(input("Enter how many Fibonacci numbers to generate: "))
print("Fibonacci sequence:", fibonacci(num))
