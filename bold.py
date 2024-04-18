import tkinter as tk

def make_bold():
    aText.tag_add("bt", "sel.first", "sel.last")

lord = tk.Tk()

aText = tk.Text(lord, font=("Georgia", "12"))
aText.grid()

aButton = tk.Button(lord, text="bold", command=make_bold)
aButton.grid()

aText.tag_config("bt", font=("Georgia", "12", "bold"))

lord.mainloop()