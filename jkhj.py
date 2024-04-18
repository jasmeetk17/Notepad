import tkinter as tk

def change_font(event=None):
    # Check if text is selected
    if text_widget.tag_ranges("sel"):
        # Get the selected text
        selected_text = text_widget.selection_get()
        
        # Get the indices of the selected text
        start_index = text_widget.index("sel.first")
        end_index = text_widget.index("sel.last")
        
        # Configure the font for the selected text
        text_widget.tag_configure("selected_font", font=("Times New Roman", 12))
        
        # Apply the "selected_font" tag to the selected text
        text_widget.tag_add("selected_font", start_index, end_index)

# Create the main window
root = tk.Tk()
root.title("Change Font of Selected Text")

# Create a Text widget
text_widget = tk.Text(root, font=("Arial", 12))
text_widget.pack(padx=10, pady=10, expand=True, fill="both")

# Insert some sample text
text_widget.insert("1.0", "Select this text to change its font.")

# Bind the <<Selection>> virtual event to the change_font function
text_widget.bind("<<Selection>>", change_font)

root.mainloop()
