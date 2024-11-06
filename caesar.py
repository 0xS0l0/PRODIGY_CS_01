import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26  # Ensures shift is within 0-25
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += shifted_char
        else:
            result += char  # Non-alphabet characters remain the same

    return result

def perform_cipher():
    text = entry_text.get()
    shift = entry_shift.get()
    
    try:
        shift = int(shift)
    except ValueError:
        messagebox.showerror("Invalid Shift", "Shift value must be an integer.")
        return

    mode = var_mode.get()
    result = caesar_cipher(text, shift, mode)
    entry_result.delete(0, tk.END)
    entry_result.insert(0, result)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")

# Create and position widgets
tk.Label(window, text="Message:").grid(row=0, column=0, padx=10, pady=10)
entry_text = tk.Entry(window, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Shift:").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(window, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(window, text="Mode:").grid(row=2, column=0, padx=10, pady=10)
var_mode = tk.StringVar(value='encrypt')
tk.Radiobutton(window, text="Encrypt", variable=var_mode, value='encrypt').grid(row=2, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(window, text="Decrypt", variable=var_mode, value='decrypt').grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Result:").grid(row=3, column=0, padx=10, pady=10)
entry_result = tk.Entry(window, width=40)
entry_result.grid(row=3, column=1, padx=10, pady=10)

# Add button to perform encryption or decryption
btn_perform = tk.Button(window, text="Process", command=perform_cipher)
btn_perform.grid(row=4, column=0, columnspan=2, pady=20)

# Run the GUI loop
window.mainloop()
