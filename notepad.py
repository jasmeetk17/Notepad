from re import X
import tkinter as tk
from tkinter import ttk,font
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

root=tk.Tk()
root.title("Jasmeet's Notepad")
root.geometry("1366x768")

text_area=tk.Text(root,width=1366,height=766)
text_area.config(wrap="word",relief=tk.FLAT)
text_area.place(x=0,y=24)


#creating starting menu for file
menu_bar = tk.Menu()

#file menu 
file = tk.Menu(menu_bar,tearoff=False)

#exit the app
def exit_app():
    root.destroy()

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

#images for toolbar
bold_img=tk.PhotoImage(file='icon\\bold.png',width=24,height=24)
italic_img=tk.PhotoImage(file='icon\\italic.png',width=24,height=24)
underline_img=tk.PhotoImage(file='icon\\underline.png',width=24,height=24)
align_left_img=tk.PhotoImage(file='icon\\align-left.png',width=24,height=24)
align_right_img=tk.PhotoImage(file='icon\\align-right.png',width=24,height=24)
align_center_img=tk.PhotoImage(file='icon\\align-center.png',width=24,height=24)
align_justify_img=tk.PhotoImage(file='icon\\align-justify.png',width=24,height=24)

#status bar 
def open_status_bar():
    statusbar = tk.Label(root, text="No of Words: ", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    statusbar.pack(side=tk.BOTTOM, fill=tk.X)

#view menu images
zoomin = tk.PhotoImage(file='icon\\zoom-in.png',width=24,height=24)
zoomout = tk.PhotoImage(file='icon\\zoom-out.png',width=24,height=24)
toolbar=tk.PhotoImage(file='icon\\tools.png',width=24,height=24)
statusbar=tk.PhotoImage(file='icon\\statusbar.png',width=24,height=24)

view.add_command(label="Zoom",accelerator="ctrl+plus",image=zoomin,compound="left")
view.add_command(label="Zoom In",accelerator="ctrl+minus",image=zoomout,compound="left")
view.add_command(label="Status Bar",accelerator="ctrl+shift+s",image=statusbar,compound="left",command=open_status_bar)
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

color_code={"Red":"#FF0000",
            "Orange":"#FFA500",
            "Yellow":"#FFF200",
            "Green":"#008000",
            "Blue":"#0000FF",
            "Indigo":"#4b0082",
            "Voilet":"#7f00ff" }

#color images
red = tk.PhotoImage(file='icon\\color-mode-red.png',width=24,height=24)
orange = tk.PhotoImage(file='icon\\color-mode-orange.png',width=24,height=24)
yellow = tk.PhotoImage(file='icon\\color-mode-yellow.png',width=24,height=24)
green = tk.PhotoImage(file='icon\\color-mode-green.png',width=24,height=24)
blue = tk.PhotoImage(file='icon\\color-mode-blue.png',width=24,height=24)
indigo = tk.PhotoImage(file='icon\\color-mode-indigo.png',width=24,height=24)
violet = tk.PhotoImage(file='icon\\color-mode-violet.png',width=24,height=24)

def red_color():
    text_area.configure(bg=color_code['Red'])

color.add_command(label="Red",image=red,compound="left",command=red_color)

def orange_color():
    text_area.configure(bg=color_code['Orange'])

color.add_command(label="Orange",image=orange,compound="left",command=orange_color)

def yellow_color():
    text_area.configure(bg=color_code['Yellow'])

color.add_command(label="Yellow",image=yellow,compound="left",command=yellow_color)

def green_color():
    text_area.configure(bg=color_code['Green'])

color.add_command(label="Green",image=green,compound="left",command=green_color)

def blue_color():
    text_area.configure(bg=color_code['Blue'])

color.add_command(label="Blue",image=blue,compound="left",command=blue_color)

def indigo_color():
    text_area.configure(bg=color_code['Indigo'])

color.add_command(label="Indigo",image=indigo,compound="left",command=indigo_color)

def voilet_color():
    text_area.configure(bg=color_code['Voilet'])

color.add_command(label="Violet",image=violet,compound="left",command=voilet_color)


menu_bar.add_cascade(label="Color",menu=color)

#getting font

toolbar=ttk.Label(root)
toolbar.pack(side=tk.TOP,fill=tk.X)

#font box
font_style = tk.font.families()
font_style1 = tk.StringVar()

font_box = ttk.Combobox(toolbar,textvariable=font_style1,width=20,state="readonly")
font_box['values'] = font_style
font_box.current(font_style.index('Arial'))
font_box.grid(row=0,column=0,padx=5)


#size for font
size=list(range(8,75))
font_size= tk.IntVar()

font_size_box= ttk.Combobox(toolbar,textvariable=font_size,width=20,state="readonly")
font_size_box['values'] = size
font_size_box.current(size.index(8))
font_size_box.grid(row=0,column=1,padx=5)


font_var='Arial'
size_var=8

#change the font family
def change_font(root):
    global font_var
    font_var=font_style1.get()
    text_area.configure(font=(font_var,size_var))

def change_size(root):
    global size_var
    size_var=font_size.get()
    text_area.configure(font=(font_var,size_var))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size_box.bind("<<ComboboxSelected>>",change_size)

#font style section
bold=tk.Button(toolbar,image=bold_img,width=15,height=15)
bold.grid(row=0,column=3,padx=5)



def change_bold():
    text_change = tk.font.Font(root,text_area['font'])
    if text_change.actual()['weight'] == 'normal':
        text_area.configure(font=(font_var,size_var,"bold"))
    elif text_change.actual()['weight'] == 'bold':
        text_area.configure(font=(font_var,size_var,"normal"))

bold.configure(command=change_bold)

italic=tk.Button(toolbar,image=italic_img,width=15,height=15)
italic.grid(row=0,column=4,padx=5)

def change_italic():
    text_change = tk.font.Font(root,text_area['font'])
    if text_change.actual()['slant'] == 'roman':
        text_area.configure(font=(font_var,size_var,"italic"))
    elif text_change.actual()['slant'] == 'italic':
        text_area.configure(font=(font_var,size_var,"normal"))

italic.configure(command=change_italic)

underline=tk.Button(toolbar,image=underline_img,width=15,height=15)
underline.grid(row=0,column=5,padx=5)

def change_underline():
    text_change = tk.font.Font(root,text_area['font'])
    if text_change.actual()['weight'] == "normal":
        text_area.configure(font=(font_var,size_var,"underline"))
    elif text_change.actual()['weight'] == "underline":
        text_area.configure(font=(font_var,size_var,"normal"))
underline.configure(command=change_underline)

         
#alignment section
def align_left():
   start = "1.0"
   end = "end"
   text_area.tag_configure("left",justify='left')
   text_area.tag_add("left",start,end)

align_left_btn=tk.Button(toolbar,image=align_left_img,width=15,height=15)
align_left_btn.grid(row=0,column=6,padx=5)
align_left_btn.configure(command=align_left)


def align_right():
   start = "1.0"
   end = "end"
   text_area.tag_configure("right",justify='right')
   text_area.tag_add("right",start,end)

align_right_btn=tk.Button(toolbar,image=align_right_img,width=15,height=15)
align_right_btn.grid(row=0,column=7,padx=5)
align_left_btn.configure(command=align_right)

def align_center():
   start = "1.0"
   end = "end"
   text_area.tag_configure("center", justify='center')
   text_area.tag_add("center",start,end)

align_center_btn=tk.Button(toolbar,image=align_center_img,width=15,height=15)
align_center_btn.grid(row=0,column=8,padx=5)
align_left_btn.configure(command=align_center)


align_justify_btn=tk.Button(toolbar,image=align_justify_img,width=15,height=15)
align_justify_btn.grid(row=0,column=9,padx=5)



#scroll bar
scroll_bar=tk.Scrollbar(root)
text_area.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_area.pack(side=tk.LEFT,expand=True)
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)

text_area.configure(font=('Arial',8))


root.config(menu=menu_bar)
root.mainloop()
