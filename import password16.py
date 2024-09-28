import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    
    # Base character set
    character_set = string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    # Display generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_password():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Secure Password Generator")

# Password length label and entry
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkboxes for criteria
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(pady=5)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(pady=5)

# Password output field
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=5)

# Generate and Copy buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

# Start the Tkinter loop
root.mainloop()
