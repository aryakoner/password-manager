# app.py
import os
from cryptography.fernet import Fernet

# Generate a key for encryption/decryption (You should store this securely)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Example function to encrypt a password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Example function to decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Main
if __name__ == "__main__":
    generate_key()  # Run this once to generate the key
    password = "my_secret_password"
    encrypted = encrypt_password(password)
    print(f"Encrypted: {encrypted}")

    decrypted = decrypt_password(encrypted)
    print(f"Decrypted: {decrypted}")