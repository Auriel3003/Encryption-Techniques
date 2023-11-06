import time

def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])  # Missing closing parenthesis here
    return "".join(key)

def vigenere_cipher_encrypt(text, key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def vigenere_cipher_decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

def main_vigenere_cipher():
    text = input("Enter the text to encrypt: ")
    keyword = input("Enter the Vigenere Cipher keyword: ")
    key = generate_key(text, keyword)

    # Encryption
    start_time = time.time()
    encrypted_text = vigenere_cipher_encrypt(text, key)
    encryption_time = time.time() - start_time

    print("Ciphertext:", encrypted_text)
    print(f"Encryption time: {encryption_time:.6f} seconds")

    decrypt_choice = input("Do you want to decrypt the text? (y/n): ")
    if decrypt_choice.lower() == 'y':
        encrypted_text = input("Enter the encrypted text: ")

        # Decryption
        start_time = time.time()
        decrypted_text = vigenere_cipher_decrypt(encrypted_text, key)
        decryption_time = time.time() - start_time

        print("Original/Decrypted Text:", decrypted_text)
        print(f"Decryption time: {decryption_time:.6f} seconds")

    avg_time = (encryption_time + decryption_time) / 2 if decrypt_choice.lower() == 'y' else encryption_time
    print(f"Average time for encryption and decryption: {avg_time:.6f} seconds")

if __name__ == "__main__":
    main_vigenere_cipher()
