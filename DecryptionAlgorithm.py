import string
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk

alphabet = string.ascii_lowercase


def decrypt():
   
    key = key_entry.get().replace("-", "")

    if len(key) != 30:
        result_label.config(text="Invalid key length")
        return

    rnd_key = abs((alphabet.index(key[1]) + 1) - (alphabet.index(key[29]) + 1))
    key_var = alphabet.index(key[rnd_key]) + 1
    decoding_factor = (alphabet.index(key[18]) + 1) + (alphabet.index(key[key_var]) + 1)

   
    input_numbers = numbers_entry.get()

    words = []
    for number in input_numbers.strip().split():
        if number.isdigit():
            char_index = (int(number) // decoding_factor) - 1 

            if char_index >= 0 and char_index < 26:
                char = alphabet[char_index]
                words.append(char)
        elif number == "-":
            words.append(" ")

    if words:
        result_label.config(text="".join(words))
    else:
        result_label.config(text="Invalid input")



window = ThemedTk(theme="breeze")
window.title("Decryption")
window.iconbitmap("icon.ico")

key_label = ttk.Label(window, text="Decryption key:")
key_entry = ttk.Entry(window, width=50)
key_label.grid(row=0, column=0, padx=5, pady=5)
key_entry.grid(row=0, column=1, padx=5, pady=5)

numbers_label = ttk.Label(window, text="Encrypted numbers:")
numbers_entry = ttk.Entry(window, width=50)
numbers_label.grid(row=1, column=0, padx=5, pady=5)
numbers_entry.grid(row=1, column=1, padx=5, pady=5)

decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=0, padx=5, pady=5)

result_label = ttk.Label(window, text="", font=("TkDefaultFont", 12), background="#f0f0f0")
result_label.grid(row=2, column=1, padx=5, pady=5)


window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

window.mainloop()
