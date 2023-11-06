import time
import math

# Encryption and Decryption functions for Columnar Transposition
def columnar_transposition_encrypt(text, key):
    cipher = ""
    k_indx = 0
    msg_len = float(len(text))
    msg_lst = list(text)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1
    return cipher

def columnar_transposition_decrypt(text, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(text))
    msg_lst = list(text)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:-null_count]
    return msg


def main_columnar_transposition():
    key = input("Enter the Columnar Transposition key: ")
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = columnar_transposition_encrypt(message, key)
    encryption_time = time.time() - start_time

    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = columnar_transposition_decrypt(encrypted_message, key)
        decryption_time = time.time() - start_time

        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_columnar_transposition()
