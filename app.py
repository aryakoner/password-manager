import os
import pyperclip
from cryptography.fernet import Fernet
from tkinter import *

# Function to generate a key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Function to decrypt a password
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# GUI setup
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    encrypted_password = encrypt_password(password)

    with open("passwords.txt", "a") as file:
        file.write(f"{website} | {encrypted_password.decode()}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

def show_passwords():
    password_list.delete(0, END)

    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            website, encrypted_password = line.split(" | ")
            decrypted_password = decrypt_password(encrypted_password.strip().encode())
            password_list.insert(END, f"Website: {website}, Password: {decrypted_password}")

# GUI window
window = Tk()
window.title("Password Manager")

website_label = Label(window, text="Website:")
website_label.pack()
website_entry = Entry(window)
website_entry.pack()

password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

save_button = Button(window, text="Save Password", command=save_password)
save_button.pack()

show_button = Button(window, text="Show Saved Passwords", command=show_passwords)
show_button.pack()

password_list = Listbox(window)
password_list.pack()

window.mainloop()