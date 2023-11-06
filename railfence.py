import random
import time  # Add this line to import the 'time' module

# Encryption and Decryption functions for Rail Fence Transposition
def rail_fence_encrypt(text, key):
    # create the matrix to cipher
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def rail_fence_decrypt(text, key):
    # create the matrix to decipher
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]
    dir_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if (rail[i][j] == '*') and (index < len(text)):
                rail[i][j] = text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)


def main_rail_fence_transposition():
    key = int(input("Enter the Rail Fence key: "))
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = rail_fence_encrypt(message, key)
    encryption_time = time.time() - start_time

    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = rail_fence_decrypt(encrypted_message, key)
        decryption_time = time.time() - start_time

        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_rail_fence_transposition()
