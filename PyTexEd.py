#!/usr/bin/env python3

import tkinter as tk

PROGRAM_NAME = "Python Text Editor (PyTexEd)"

root = tk.Tk()
root.title(PROGRAM_NAME)
root.geometry('400x400')

# Text Widget Functionality

def cut():
    content_text.event_generate("<<Cut>>")
    return "break"

def copy():
    content_text.event_generate("<<Copy>>")
    return "break"

def paste():
    content_text.event_generate("<<Paste>>")
    return "break"

def undo():
    content_text.event_generate("<<Undo>>")
    return "break"

def redo(event=None):
    content_text.event_generate("<<Redo>>")
    return "break"


# Menu Items
new_file_icon = tk.PhotoImage(file='gif/New_File.gif')
open_file_icon = tk.PhotoImage(file='gif/Folder.gif')
save_file_icon = tk.PhotoImage(file='gif/Save.gif')
exit_icon = tk.PhotoImage(file='gif/Exit.gif')
undo_icon = tk.PhotoImage(file='gif/Undo.gif')
redo_icon = tk.PhotoImage(file='gif/Redo.gif')
cut_icon = tk.PhotoImage(file='gif/Cut.gif')
copy_icon = tk.PhotoImage(file='gif/Copy.gif')
paste_icon = tk.PhotoImage(file='gif/Paste.gif')
search_icon = tk.PhotoImage(file='gif/Search.gif')
about_icon = tk.PhotoImage(file='gif/About.gif')
help_icon = tk.PhotoImage(file='gif/Help.gif')

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S')
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', compound='left', image=exit_icon, underline=0)
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=undo_icon, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl+F', compound='left', image=search_icon)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', underline=7)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
show_line_number = tk.IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number)
show_cursor_info = tk.IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Show Cursor Location at Bottom', variable=show_cursor_info)
highlight_line = tk.IntVar()
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1, offvalue=0, variable=highlight_line)
themes_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

color_schemes = {
    'Default': '#000000.#FFFFFF',
    'Greygarious': '#83406A.#D1D4D1',
    'Aquamarine': '#5B8340.#D1E7E0',
    'Bold Beige': '#4B4620.#FFF0E1',
    'Cobalt Blue': '#ffffBB.#3333aa',
    'Olive Green': '#D1E7E0.#5B8340',
    'Night Mode': '#FFFFFF.#000000',
}

theme_choice = tk.StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k, variable=theme_choice)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', compound='left', image=about_icon, underline=0)
about_menu.add_command(label='Help', compound='left', image=help_icon, underline=0)
menu_bar.add_cascade(label='About', menu=about_menu)
root.config(menu=menu_bar)

# Top and line number bars
shortcut_bar = tk.Frame(root, height=25, background='light blue')
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = tk.Text(root, width=4, padx=3, takefocus=0, border=0, background='blue', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

# Main Text adn Scrollbar widgets
content_text = tk.Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')


# Redo binding issue
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-y>', redo)

root.mainloop()
