import tkinter as tk

def update_status(message):
    status_var.set(message)

root = tk.Tk()
root.title("Status Bar Example")

status_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
status_frame.pack(side=tk.BOTTOM, fill=tk.X)

status_var = tk.StringVar()
status_label = tk.Label(status_frame, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(fill=tk.X)

# Example: Update status
update_status("Ready")

root.mainloop()
