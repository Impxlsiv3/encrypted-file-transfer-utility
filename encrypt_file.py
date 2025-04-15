from tkinter import filedialog, Tk, simpledialog, messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(file_path, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(file_path, 'rb') as f:
        plaintext = pad(f.read())
    
    ciphertext = cipher.encrypt(plaintext)

    with open(file_path + ".enc", 'wb') as f:
        f.write(salt + iv + ciphertext)

    messagebox.showinfo("Success", "File encrypted successfully!")

def main():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select file to encrypt")
    if not file_path:
        return
    password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
    if not password:
        return
    encrypt_file(file_path, password)

if __name__ == "__main__":
    main()
