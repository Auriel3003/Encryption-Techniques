import time

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main_caesar_cipher():
    shift = int(input("Enter the Caesar Cipher shift value: "))
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = caesar_cipher_encrypt(message, shift)
    encryption_time = time.time() - start_time

    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        decryption_time = time.time() - start_time

        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_caesar_cipher()
