import time

def generate_monoalphabetic_key():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shuffled_alphabet = "qwertyuiopasdfghjklzxcvbnm"  # Your key for decryption, 26 characters
    key = {}
    for i in range(len(alphabet)):
        key[alphabet[i]] = shuffled_alphabet[i]
    return key

def monoalphabetic_substitution_encrypt(text, key):
    text = str(text)
    encrypted = []
    for letter in text:
        encrypted.append(key.get(letter, letter))
    return ''.join(encrypted)

def monoalphabetic_substitution_decrypt(text, key):
    text = str(text)
    decrypted = []
    reverse_key = {v: k for k, v in key.items()}
    for letter in text:
        decrypted.append(reverse_key.get(letter, letter))
    return ''.join(decrypted)

def main_monoalphabetic_substitution():
    key = generate_monoalphabetic_key()
    message = input("Enter the message to encrypt: ")

    # Encryption
    start_time = time.time()
    encrypted_message = monoalphabetic_substitution_encrypt(message, key)
    encryption_time = time.time() - start_time
    print(f"Encrypted message: {encrypted_message}")
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the message? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_message = input("Enter the encrypted message: ")

        # Decryption
        start_time = time.time()
        decrypted_message = monoalphabetic_substitution_decrypt(encrypted_message, key)
        decryption_time = time.time() - start_time
        print(f"Decrypted message: {decrypted_message}")
        print(f"Decryption time: {decryption_time:.6f} seconds")

        avg_time = (encryption_time + decryption_time) / 2
    else:
        avg_time = encryption_time

    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_monoalphabetic_substitution()
