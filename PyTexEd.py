#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

PROGRAM_NAME = "Python Text Editor (PyTexEd)"
root.title(PROGRAM_NAME)

# Menu Items
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='(Ctrl + N)', compound='left', underline=0)
file_menu.add_separator()
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='(Ctrl + Z)', compound='left')
menu_bar.add_cascade(label='Edit', menu=edit_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)

# Top and line number bars
shortcut_bar = tk.Frame(root, height=25, background='light blue')
shortcut_bar.pack(expand='no', fill='x')

line_number_bar = tk.Text(root, width=4, padx=3, takefocus=0, border=0, background='blue', state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

# Main Text adn Scrollbar widgets
content_text = tk.Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')
root.config(menu=menu_bar)

root.mainloop()
