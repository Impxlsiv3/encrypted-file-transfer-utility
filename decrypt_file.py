from tkinter import filedialog, Tk, simpledialog, messagebox
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def unpad(data):
    return data.rstrip(b' ')

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        ciphertext = f.read()

    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(plaintext)

    decrypted_path = file_path.replace(".enc", ".dec")
    with open(decrypted_path, 'wb') as f:
        f.write(plaintext)

    messagebox.showinfo("Success", "File decrypted successfully!")

def main():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select file to decrypt")
    if not file_path:
        return
    password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
    if not password:
        return
    decrypt_file(file_path, password)

if __name__ == "__main__":
    main()
