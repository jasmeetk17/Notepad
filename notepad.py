from re import X
import tkinter as tk
from tkinter import BOTTOM, SUNKEN, ttk,font
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

root=tk.Tk()
root.title("Jasmeet's Notepad")
root.geometry("1366x768")

#exit the app
def exit_app():
    root.destroy()

#images for toolbar
bold_img=tk.PhotoImage(file='icon\\bold.png',width=24,height=24)
italic_img=tk.PhotoImage(file='icon\\italic.png',width=24,height=24)
underline_img=tk.PhotoImage(file='icon\\underline.png',width=24,height=24)
align_left_img=tk.PhotoImage(file='icon\\align-left.png',width=24,height=24)
align_right_img=tk.PhotoImage(file='icon\\align-right.png',width=24,height=24)
align_center_img=tk.PhotoImage(file='icon\\align-center.png',width=24,height=24)
align_justify_img=tk.PhotoImage(file='icon\\align-justify.png',width=24,height=24)

#getting font
fon = tk.font.families()
fam = tk.StringVar()

def open_status_bar():
    statusbar = tk.Label(root, text="No of Words: ", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)

def open_tool_bar():
    def close_tool_bar():
        tool_bar.destroy()

    #create frame
    tool_bar=tk.Frame(root,width=320,height=90,padx=10, pady=10,highlightbackground='blue',highlightthickness=1)


    #create combobox
    fbox = ttk.Combobox(tool_bar,width=30,textvariable=fam,state='readonly')
    fbox['value'] = fon
    fbox.place(x=1,y=5)
    fbox.set('System')

    #font size
    size_combo = ttk.Combobox(tool_bar,width=10,state='readonly')
    size_combo['values'] = ("8","9", "10","11","12", "14", "16", "18", "20","22","24","26","28","30","32","34","36","48","74")
    size_combo.place(x=120,y=28)
    size_combo.set('8')

    close_btn=tk.Button(tool_bar,text='Close',width=10,height=0,bd=0,font=('Bold',10),foreground='white',
                        background='red',command=close_tool_bar)
    close_btn.place(x=120,y=50)

    #font style section
    
    bold=tk.Button(tool_bar,image=bold_img)
    bold.place(x=1,y=30)

    
    italic=tk.Button(tool_bar,image=italic_img)
    italic.place(x=41,y=30)

    
    underline=tk.Button(tool_bar,image=underline_img)
    underline.place(x=81,y=30)

    #alignment section
    
    align_left=tk.Button(tool_bar,image=align_left_img)
    align_left.place(x=220,y=1)

    align_right=tk.Button(tool_bar,image=align_right_img)
    align_right.place(x=260,y=1)

    
    align_center=tk.Button(tool_bar,image=align_center_img)
    align_center.place(x=220,y=35)

    
    align_justify=tk.Button(tool_bar,image=align_justify_img)
    align_justify.place(x=260,y=35)

    

    tool_bar.place(x=60,y=2)


    



#creating starting menu for file
menu_bar = tk.Menu()


#file menu 
file = tk.Menu(menu_bar,tearoff=False)

#file menu images
save = tk.PhotoImage(file='icon\\save.png',width=24,height=24)
new = tk.PhotoImage(file='icon\\file-add.png',width=24,height=24)
open = tk.PhotoImage(file='icon\\file.png',width=24,height=24)
save_as = tk.PhotoImage(file='icon\\save-as.png',width=24,height=24)
exit = tk.PhotoImage(file='icon\\exit.png',width=24,height=24)

#file menu options with cascade
file.add_command(label="New",image=new,command=tk.LEFT,accelerator="ctrl+n",compound="left")
file.add_command(label="Open",accelerator="ctrl+o",image=open,command=tk.LEFT,compound="left")
file.add_command(label="Save",accelerator="ctrl+s",image=save,command=tk.LEFT,compound="left")
file.add_command(label="Save As",accelerator="ctrl+shift+s",image=save_as,command=tk.LEFT,compound="left")
file.add_command(label="Exit",accelerator="ctrl+e",image=exit,compound="left",command=exit_app)

menu_bar.add_cascade(label="File",menu=file)


#view menu with cascade

view = tk.Menu(menu_bar,tearoff=False)

#view menu images
zoomin = tk.PhotoImage(file='icon\\zoom-in.png',width=24,height=24)
zoomout = tk.PhotoImage(file='icon\\zoom-out.png',width=24,height=24)
toolbar=tk.PhotoImage(file='icon\\tools.png',width=24,height=24)
statusbar=tk.PhotoImage(file='icon\\statusbar.png',width=24,height=24)

view.add_command(label="Zoom",accelerator="ctrl+plus",image=zoomin,compound="left")
view.add_command(label="Zoom In",accelerator="ctrl+minus",image=zoomout,compound="left")
view.add_command(label="Status Bar",accelerator="ctrl+shift+s",image=statusbar,compound="left",command=open_status_bar)
view.add_command(label="Tool Bar",accelerator="ctrl+shift+t",image=toolbar,compound="left",command=open_tool_bar)
menu_bar.add_cascade(label="View",menu=view)


#edit menu with cascade
edit = tk.Menu(menu_bar,tearoff=False)

#edit images
cut = tk.PhotoImage(file='icon\\cut.png',width=24,height=24)
copy = tk.PhotoImage(file='icon\\copy.png',width=24,height=24)
paste = tk.PhotoImage(file='icon\\paste.png',width=24,height=24)
delete = tk.PhotoImage(file='icon\\delete.png',width=24,height=24)
undo = tk.PhotoImage(file='icon\\undo.png',width=24,height=24)

edit.add_command(label="Cut",accelerator="ctrl+x",image=cut,compound="left")
edit.add_command(label="Copy",accelerator="ctrl+c",image=copy,compound="left")
edit.add_command(label="Paste",accelerator="ctrl+v",image=paste,compound="left")
edit.add_command(label="Delete",accelerator="ctrl+d",image=delete,compound="left")
edit.add_command(label="Undo",accelerator="ctrl+u",image=undo,compound="left")

menu_bar.add_cascade(label="Edit",menu=edit)

#edit menu with cascade
color = tk.Menu(menu_bar,tearoff=False)

#color images
red = tk.PhotoImage(file='icon\\color-mode-red.png',width=24,height=24)
orange = tk.PhotoImage(file='icon\\color-mode-orange.png',width=24,height=24)
yellow = tk.PhotoImage(file='icon\\color-mode-yellow.png',width=24,height=24)
green = tk.PhotoImage(file='icon\\color-mode-green.png',width=24,height=24)
blue = tk.PhotoImage(file='icon\\color-mode-blue.png',width=24,height=24)
indigo = tk.PhotoImage(file='icon\\color-mode-indigo.png',width=24,height=24)
violet = tk.PhotoImage(file='icon\\color-mode-violet.png',width=24,height=24)

color.add_command(label="Red",image=red,compound="left")
color.add_command(label="Orange",image=orange,compound="left")
color.add_command(label="Yellow",image=yellow,compound="left")
color.add_command(label="Green",image=green,compound="left")
color.add_command(label="Blue",image=blue,compound="left")
color.add_command(label="Indigo",image=indigo,compound="left")
color.add_command(label="Violet",image=violet,compound="left")

menu_bar.add_cascade(label="Color",menu=color)






root.config(menu=menu_bar)



root.mainloop()
