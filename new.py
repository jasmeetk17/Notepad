import tkinter as tk

def justify_center():
    text_widget.config(justify='center')

root = tk.Tk()
root.title("Text Justification Example")

# Create a Text widget
text_widget = tk.Text(root, width=40, height=10)
text_widget.pack(pady=20)

# Insert some text
text_widget.insert(tk.END, "This is centered text.\nYou can add more lines to see the justification.")

# Create a button to justify the text in the center
justify_button = tk.Button(root, text="Justify Center", command=justify_center)
justify_button.pack(pady=10)

root.mainloop()
