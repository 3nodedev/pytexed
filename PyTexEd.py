#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

PROGRAM_NAME = "Python Text Editor (PyTexEd)"
root.title(PROGRAM_NAME)

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

root.config(menu=menu_bar)

root.mainloop()
