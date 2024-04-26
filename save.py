import tkinter as tk
from tkinter import filedialog

def save_file():
    # Get the content of the text area
    content = text_area.get("1.0", tk.END)
    
    # Open a file dialog to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    # Write the content to the file
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)

# Create the main window
root = tk.Tk()
root.title("Save Text File")

# Create a text area
text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=20)

# Create a button to save the file
save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(pady=20)

root.mainloop()
