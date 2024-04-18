import tkinter as tk
from tkinter import ttk

def change_font():
    # Get selected font family and size from Comboboxes
    selected_font = font_var.get()
    selected_size = size_var.get()
    
    # Update Text widget font
    text_widget.config(font=(selected_font, selected_size))

root = tk.Tk()
root.title("Text Widget Font Settings")

# Font options
fonts = ["Arial", "Times New Roman", "Courier New"]
sizes = [10, 12, 14, 16, 18, 20]

# Selected font and size variables
font_var = tk.StringVar(root)
size_var = tk.StringVar(root)

# Default values
font_var.set("Arial")
size_var.set("12")

# Create Comboboxes for font family and size
font_combobox = ttk.Combobox(root, textvariable=font_var, values=fonts, state="readonly")
font_combobox.pack(padx=10, pady=5)

size_combobox = ttk.Combobox(root, textvariable=size_var, values=sizes, state="readonly")
size_combobox.pack(padx=10, pady=5)

# Create a Text widget
text_widget = tk.Text(root, font=(font_var.get(), int(size_var.get())))
text_widget.pack(padx=10, pady=10)

# Button to apply font changes
apply_button = tk.Button(root, text="Apply", command=change_font)
apply_button.pack(padx=10, pady=5)

root.mainloop()
