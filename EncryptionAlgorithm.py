import string
import random
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


alphabet = string.ascii_lowercase


key = ''.join(random.choices(string.ascii_lowercase, k=30))
key_parts = [key[i:i+6] for i in range(0, len(key), 6)]
key_formatted = '-'.join(key_parts)

rnd_key = abs((alphabet.index(key[1]) + 1) - (alphabet.index(key[29]) + 1))
key_var = alphabet.index(key[rnd_key]) + 1
encoding_factor = (alphabet.index(key[18]) + 1) + (alphabet.index(key[key_var]) + 1)

def encrypt_text():
    input_text = input_field.get().lower()

 
    numbers = []
    for char in input_text:
        if char in alphabet:
            number = (alphabet.index(char) + 1) * encoding_factor
            numbers.append(str(number))
        elif char == " ":
            numbers.append("-") 

    output_numbers = " ".join(numbers)
    output_formatted = output_numbers.replace("-", "- ")

    
    output_field.delete("1.0", tk.END)
    output_field.insert("1.0", output_formatted)

   
    key_output.delete("1.0", tk.END)
    key_output.insert("1.0", key_formatted)


root = ThemedTk(theme="breeze")
root.title("Encryption")
root.iconbitmap("icon.ico")


key_label = ttk.Label(root, text="Encryption Key:")
key_label.grid(row=0, column=0)
key_output = tk.Text(root, width=40, height=1)
key_output.grid(row=0, column=1, columnspan=2)
key_output.insert("1.0", key_formatted)


input_label = ttk.Label(root, text="Enter Text:")
input_label.grid(row=1, column=0)
input_field = ttk.Entry(root, width=40)
input_field.grid(row=1, column=1, columnspan=2)


encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=1, column=3)


output_label = ttk.Label(root, text="Encrypted Numbers:")
output_label.grid(row=2, column=0)
output_field = tk.Text(root, width=40, height=5)
output_field.grid(row=2, column=1, columnspan=2)


for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.mainloop()

