import random
import string

# Generate key and character set
chars = string.punctuation + string.digits + string.ascii_letters + " "
key = random.sample(chars, len(chars))  # This replaces the need to shuffle a copy

# Encryption function
def encrypt_decrypt(text, from_set, to_set):
    return ''.join(to_set[from_set.index(char)] for char in text)

# Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt_decrypt(plain_text, chars, key)
print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to decrypt: ")
plain_text = encrypt_decrypt(cipher_text, key, chars)
print(f"encrypted message: {cipher_text}")
print(f"decrypted message: {plain_text}")
