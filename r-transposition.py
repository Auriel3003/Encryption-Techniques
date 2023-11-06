import time
import math

# Encryption and Decryption functions for Row Transposition
def row_transposition_encrypt(text, key):
    key_order = sorted(range(1, len(key) + 1), key=lambda k: key[k - 1])
    num_rows = math.ceil(len(text) / len(key))
    matrix = ['' for _ in range(num_rows)]

    for i, char in enumerate(text):
        matrix[i % num_rows] += char

    encrypted_message = ''.join([matrix[k - 1] for k in key_order])
    return encrypted_message

def row_transposition_decrypt(text, key):
    key_order = sorted(range(1, len(key) + 1), key=lambda k: key[k - 1])
    num_rows = math.ceil(len(text) / len(key))
    rows = ['' for _ in range(num_rows)]

    row_lengths = [len(text) // num_rows] * num_rows
    remaining_chars = len(text) % num_rows

    for i in range(remaining_chars):
        row_lengths[i] += 1

    i = 0
    for k in key_order:
        row = rows[k - 1]
        row_length = row_lengths[k - 1]
        rows[k - 1] = row + text[i:i+row_length]
        i += row_length

    decrypted_message = ''.join([row for row in rows])
    return decrypted_message

def main_row_transposition():
    key = input("Enter the Row Transposition key (e.g., 3124 for key '3142'): ")
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = row_transposition_encrypt(message, key)
    encryption_time = time.time() - start_time

    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = row_transposition_decrypt(encrypted_message, key)
        decryption_time = time.time() - start_time

        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_row_transposition()

