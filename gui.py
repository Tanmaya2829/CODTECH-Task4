import tkinter as tk
from tkinter import filedialog, messagebox
import os
from encryptor import encrypt_file, decrypt_file

def browse_file():
    file_path.set(filedialog.askopenfilename())

def perform_encryption():
    key = key_entry.get().encode().ljust(32)[:32]
    filepath = file_path.get()
    if not os.path.exists(filepath):
        messagebox.showerror("Error", "File does not exist!")
        return
    encrypt_file(key, filepath)
    messagebox.showinfo("Success", "File encrypted successfully!")

def perform_decryption():
    key = key_entry.get().encode().ljust(32)[:32]
    filepath = file_path.get()
    if not os.path.exists(filepath):
        messagebox.showerror("Error", "File does not exist!")
        return
    decrypt_file(key, filepath)
    messagebox.showinfo("Success", "File decrypted successfully!")

app = tk.Tk()
app.title("AES-256 Encryption Tool")

tk.Label(app, text="Enter 32-byte Key:").pack(pady=5)
key_entry = tk.Entry(app, width=50, show="*")
key_entry.pack(pady=5)

file_path = tk.StringVar()
tk.Entry(app, textvariable=file_path, width=50).pack(pady=5)
tk.Button(app, text="Browse", command=browse_file).pack(pady=5)
tk.Button(app, text="Encrypt", command=perform_encryption).pack(pady=5)
tk.Button(app, text="Decrypt", command=perform_decryption).pack(pady=5)

app.mainloop()