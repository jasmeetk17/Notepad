import tkinter as tk

root=tk.Tk()
root.title("Jasmeet's Notepad")
root.geometry("1366x768")

#creating starting menu for file
menu_bar = tk.Menu()

#file menu 
file = tk.Menu(menu_bar,tearoff=False)

#file menu images
save = tk.PhotoImage(file='icon\\save.png',width=24,height=24)
new = tk.PhotoImage(file='icon\\file-add.png',width=24,height=24)
open = tk.PhotoImage(file='icon\\file.png',width=24,height=24)
save_as = tk.PhotoImage(file='icon\\save-2.png',width=24,height=24)
exit = tk.PhotoImage(file='icon\\exit-left.png',width=24,height=24)

#file menu options with cascade
file.add_command(label="New",image=new,command=tk.LEFT,accelerator="ctrl+n")
file.add_command(label="Open",accelerator="ctrl+o",image=open,command=tk.LEFT)
file.add_command(label="Save",accelerator="ctrl+s",image=save,command=tk.LEFT)
file.add_command(label="Save As",accelerator="ctrl+shift+s",image=save_as,command=tk.LEFT)
file.add_command(label="Exit",accelerator="ctrl+e",image=exit,command=tk.LEFT)

menu_bar.add_cascade(label="File",menu=file)


#view menu with cascade

view = tk.Menu(menu_bar,tearoff=False)

#view menu images
zoomin = tk.PhotoImage(file='icon\\zoom-in.png',width=24,height=24)
zoomout = tk.PhotoImage(file='icon\\zoom-out.png',width=24,height=24)

view.add_command(label="Zoom",accelerator="ctrl+z",image=zoomin,command=tk.LEFT)
view.add_command(label="Zoom In",accelerator="ctrl+z+shift",image=zoomout,command=tk.LEFT)
menu_bar.add_cascade(label="View",menu=view)


#edit menu with cascade
edit = tk.Menu(menu_bar,tearoff=False)

#edit images
cut = tk.PhotoImage(file='icon\\cut.png',width=24,height=24)
copy = tk.PhotoImage(file='icon\\copy.png',width=24,height=24)
paste = tk.PhotoImage(file='icon\\paste.png',width=24,height=24)
delete = tk.PhotoImage(file='icon\\delete.png',width=24,height=24)
undo = tk.PhotoImage(file='icon\\undo.png',width=24,height=24)

edit.add_command(label="Cut",accelerator="ctrl+x",image=cut,command=tk.LEFT)
edit.add_command(label="Copy",accelerator="ctrl+c",image=copy,command=tk.LEFT)
edit.add_command(label="Paste",accelerator="ctrl+v",image=paste,command=tk.LEFT)
edit.add_command(label="Delete",accelerator="ctrl+d",image=delete,command=tk.LEFT)
edit.add_command(label="Undo",accelerator="ctrl+u",image=undo,command=tk.LEFT)

menu_bar.add_cascade(label="edit",menu=edit)

#edit menu with cascade
color = tk.Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(label="Color",menu=color)

root.config(menu=menu_bar)
root.mainloop()
