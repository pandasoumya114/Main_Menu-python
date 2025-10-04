def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabets
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep spaces, numbers, symbols unchanged
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just reverse shifting


# Example usage
message = input("Enter a message: ")
shift_key = int(input("Enter shift key (number): "))

encrypted = encrypt(message, shift_key)
decrypted = decrypt(encrypted, shift_key)

print("\nOriginal Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
