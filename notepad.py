from re import X
import tkinter as tk
from tkinter import ttk,font
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from tkinter import filedialog
import os

root=tk.Tk()
root.title("Jasmeet's Notepad")
root.geometry("1366x768")

text_area=tk.Text(root,width=300,height=900)
text_area.config(wrap="word",relief=tk.FLAT)
text_area.place(x=0,y=15)

opened_file_name=None

#creating starting menu for file
menu_bar = tk.Menu()

#file menu 
file = tk.Menu(menu_bar,tearoff=False)

#open new tab   
new = tk.PhotoImage(file='icon\\file-add.png',width=24,height=24)

n=''  
def new_window(event=None):
    global n
    n=' '
    text_area.delete(1.0,tk.END)

file.add_command(label="New",image=new,command=new_window,accelerator="Ctrl+N",compound="left")

#save the file with same name
save = tk.PhotoImage(file='icon\\save.png',width=24,height=24)

def save_file(event=None):
    global opened_file_name

    content = text_area.get(1.0, tk.END)
    if opened_file_name is not None:
        # Save to the previously opened file
        try:
            with open(opened_file_name, 'w') as f:
                f.write(content)
            print("File saved successfully.")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        # If no file was opened, fall back to Save As functionality
        save_as_file(event)


file.add_command(label="Save",accelerator="Ctrl+S",image=save,command=save_file,compound="left")

open_icon= tk.PhotoImage(file='icon\\file.png',width=24,height=24)

#open the file
def open_file(event=None):
    global n,opened_file_name
    n = filedialog.askopenfile(mode="r", defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if n is not None:
        file_name = n.name
        opened_file_name=n.name
        print(f"Attempting to open file: {file_name}")
        print(f"Current working directory: {os.getcwd()}")
        try:
            with open(file_name, 'r') as f:
                content = f.read()
                print(content)
                # Assuming 'text_area' is your tkinter Text widget
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        finally:
            n.close()
    else:
        print("No file selected.")

file.add_command(label="Open",accelerator="ctrl+o",image=open_icon,command=open_file,compound="left")


save_as = tk.PhotoImage(file='icon\\save-as.png',width=24,height=24)

#save the new file
def save_as_file(event=None):
    global opened_file_name

    content = text_area.get(1.0, tk.END)
    default_file_name = os.path.basename(opened_file_name) if opened_file_name else "Untitled.txt"

    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", initialfile=default_file_name,filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file is not None:
        file.write(content)
        opened_file_name = file.name # Update the opened_file_name variable
        print("File saved successfully.")
        file.close()
    else:
        print("No file selected for saving.")


file.add_command(label="Save As",accelerator="ctrl+shift+s",image=save_as,command=save_as_file,compound="left")

exit = tk.PhotoImage(file='icon\\exit.png',width=24,height=24)

#exit the app
def exit_app(event=None):
    root.destroy()
file.add_command(label="Exit",accelerator="ctrl+e",image=exit,compound="left",command=exit_app)

root.bind("<Control-n>", new_window)  # Ctrl+X for cut
root.bind("<Control-o>", open_file)  # Ctrl+C for copy
root.bind("<Control-s>",save_as_file)
root.bind("<Control-Shift-s>",save_as_file)  # Ctrl+V for paste
root.bind("<Control-e>", exit_app)  # Delete key for delete

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

#edit menu with cascade
edit = tk.Menu(menu_bar,tearoff=False)

#edit images
cut = tk.PhotoImage(file='icon\\cut.png',width=24,height=24)
copy = tk.PhotoImage(file='icon\\copy.png',width=24,height=24)
paste = tk.PhotoImage(file='icon\\paste.png',width=24,height=24)
delete = tk.PhotoImage(file='icon\\delete.png',width=24,height=24)
undo = tk.PhotoImage(file='icon\\undo.png',width=24,height=24)

def cut_text(event=None):
  if text_area.tag_ranges("sel"):
    text = text_area.get("sel.first", "sel.last")  # Get the selected text
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(text)  # Copy the selected text to the clipboard
    text_area.delete("sel.first", "sel.last")  # Delete the selected text from the widget
  else:
      pass

edit.add_command(label="Cut",accelerator="ctrl+x",image=cut,compound="left",command=cut_text)

def copy_text(event=None):
    text = text_area.get("sel.first", "sel.last")  # Get the selected text
    if text:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(text)  # Copy the selected text to the clipboard


edit.add_command(label="Copy",accelerator="ctrl+c",image=copy,compound="left")

def paste_text(event=None):
    text_to_paste = root.clipboard_get()  # Get the content from the clipboard
    text_area.insert(tk.INSERT, text_to_paste)  # Insert the content at the current cursor position

edit.add_command(label="Paste",accelerator="ctrl+v",image=paste,compound="left",command=paste_text)

def delete_text(event=None):
    # Get the current selection indices
    start_index = text_area.index("sel.first")
    end_index = text_area.index("sel.last")
    # Delete the selected text
    text_area.delete(start_index, end_index)

edit.add_command(label="Delete",accelerator="ctrl+d",image=delete,compound="left",command=delete_text)


root.bind("<Control-x>", cut_text)  # Ctrl+X for cut
root.bind("<Control-c>", copy_text)  # Ctrl+C for copy
root.bind("<Control-v>", paste_text)  # Ctrl+V for paste
root.bind("<Control-d>", delete_text)  # Delete key for delete

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

#add red color
def red_color():
    text_area.configure(bg=color_code['Red'])

color.add_command(label="Red",image=red,compound="left",command=red_color)

#add orange color
def orange_color():
    text_area.configure(bg=color_code['Orange'])
color.add_command(label="Orange",image=orange,compound="left",command=orange_color)

#add yellow color
def yellow_color():
    text_area.configure(bg=color_code['Yellow'])
color.add_command(label="Yellow",image=yellow,compound="left",command=yellow_color)

#add green color
def green_color():
    text_area.configure(bg=color_code['Green'])
color.add_command(label="Green",image=green,compound="left",command=green_color)

#add blue color
def blue_color():
    text_area.configure(bg=color_code['Blue'])
color.add_command(label="Blue",image=blue,compound="left",command=blue_color)

#add indigo color
def indigo_color():
    text_area.configure(bg=color_code['Indigo'])
color.add_command(label="Indigo",image=indigo,compound="left",command=indigo_color)

#add voilet color
def voilet_color():
    text_area.configure(bg=color_code['Voilet'])
color.add_command(label="Violet",image=violet,compound="left",command=voilet_color)

menu_bar.add_cascade(label="Background Color ",menu=color)

#edit menu with cascade
color_font = tk.Menu(menu_bar,tearoff=False)

color_code={"Red":"#FF0000",
            "Orange":"#FFA500",
            "Yellow":"#FFF200",
            "Green":"#008000",
            "Blue":"#0000FF",
            "Indigo":"#4b0082",
            "Voilet":"#7f00ff" }

#color images
red_font = tk.PhotoImage(file='icon\\color-mode-red.png',width=24,height=24)
orange_font = tk.PhotoImage(file='icon\\color-mode-orange.png',width=24,height=24)
yellow_font = tk.PhotoImage(file='icon\\color-mode-yellow.png',width=24,height=24)
green_font = tk.PhotoImage(file='icon\\color-mode-green.png',width=24,height=24)
blue_font = tk.PhotoImage(file='icon\\color-mode-blue.png',width=24,height=24)
indigo_font = tk.PhotoImage(file='icon\\color-mode-indigo.png',width=24,height=24)
violet_font = tk.PhotoImage(file='icon\\color-mode-violet.png',width=24,height=24)

#add red color
def red_color_font():
    text_area.configure(fg=color_code['Red'])
   
    

color_font.add_command(label="Red",image=red,compound="left",command=red_color_font)

#add orange color
def orange_color_font():
    text_area.configure(fg=color_code['Orange'])
    

color_font.add_command(label="Orange",image=orange,compound="left",command=orange_color_font)

#add yellow color
def yellow_color_font():
    text_area.configure(fg=color_code['Yellow'])
    

color_font.add_command(label="Yellow",image=yellow,compound="left",command=yellow_color_font)

#add green color
def green_color_font():
    text_area.configure(fg=color_code['Green'])
   

color_font.add_command(label="Green",image=green,compound="left",command=green_color_font)

#add blue color
def blue_color_font():
    text_area.configure(fg=color_code['Blue'])
   

color_font.add_command(label="Blue",image=blue,compound="left",command=blue_color_font)

#add indigo color
def indigo_color_font():
    text_area.configure(fg=color_code['Indigo'])
    

color_font.add_command(label="Indigo",image=indigo,compound="left",command=indigo_color_font)

#add voilet color
def voilet_color_font():
    text_area.configure(fg=color_code['Voilet'])
    

color_font.add_command(label="Violet",image=violet,compound="left",command=voilet_color_font)


menu_bar.add_cascade(label="Font Color ",menu=color_font)

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

#change font size
def change_size(root):
    global size_var
    size_var=font_size.get()
    text_area.configure(font=(font_var,size_var))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size_box.bind("<<ComboboxSelected>>",change_size)

#font style section

#bold
bold=tk.Button(toolbar,image=bold_img,width=15,height=15)
bold.grid(row=0,column=3,padx=5)


def change_bold():
    text_change = tk.font.Font(root,text_area['font'])
    if text_change.actual()['weight'] == 'normal':
        text_area.configure(font=(font_var,size_var,"bold"))
    elif text_change.actual()['weight'] == 'bold':
        text_area.configure(font=(font_var,size_var,"normal"))

bold.configure(command=change_bold)

#italic
italic=tk.Button(toolbar,image=italic_img,width=15,height=15)
italic.grid(row=0,column=4,padx=5)

def change_italic():
    text_change = tk.font.Font(root,text_area['font'])
    if text_change.actual()['slant'] == 'roman':
        text_area.configure(font=(font_var,size_var,"italic"))
    elif text_change.actual()['slant'] == 'italic':
        text_area.configure(font=(font_var,size_var,"normal"))

italic.configure(command=change_italic)

#underline
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

start = "1.0"
end = "end"

#left alignment
align_left_btn=tk.Button(toolbar,image=align_left_img,width=15,height=15)
align_left_btn.grid(row=0,column=6,padx=5)


def align_left():
   
    start = "1.0"
    end = "end"
    text_area.tag_configure("center",justify='left')
    text_area.tag_add("center",start,end)
   
align_left_btn.configure(command=align_left)

#right alignment 
align_right_btn=tk.Button(toolbar,image=align_right_img,width=15,height=15)
align_right_btn.grid(row=0,column=7,padx=5)

def align_right():
   start = "1.0"
   end = "end"
   text_area.tag_configure("center",justify='right')
   text_area.tag_add("center",start,end)
align_right_btn.configure(command=align_right)

#center alignment
align_center_btn=tk.Button(toolbar,image=align_center_img,width=15,height=15)
align_center_btn.grid(row=0,column=8,padx=5)

def align_center():
   start = "1.0"
   end = "end"
   text_area.tag_configure("center", justify='center')
   text_area.tag_add("center",start,end)

align_center_btn.configure(command=align_center)


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
