from pathlib import Path
from sys import path

import tkinter as tk
from tkinter import ttk
from tkinter.constants import SUNKEN, RAISED

open_icon_path = Path(path[0]) / 'open.png'


def read_and_insert_text():
    fp = Path(file_path.get())
    if fp.is_file():
        text = fp.read_text(encoding='utf-8')
        editor.delete('1.0', 'end')
        editor.insert('1.0', text)
    else:
        file_path.set('')


def editor_set_bold():
    cur_state = but_B['relief']
    cur_font = editor.cget('font')
    if cur_state == RAISED:
        but_B['relief'] = SUNKEN
        print(cur_font)
        print(type(cur_font))
    else:
        but_B['relief'] = RAISED


def editor_set_lower():
    cur_text = editor.get('1.0', 'end')
    cur_text = cur_text.strip().lower()
    editor.delete('1.0', 'end')
    editor.insert('1.0', cur_text)


def editor_set_upper():
    cur_text = editor.get('1.0', 'end')
    cur_text = cur_text.strip().upper()
    editor.delete('1.0', 'end')
    editor.insert('1.0', cur_text)


root = tk.Tk()
root.title('Пример простого графического интерфейса')
root.geometry('900x400-30+35')
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)


frame_path = ttk.Frame(
    root,
    padding=(10, 7, 10, 10),
)
frame_path.grid(
    row=0,
    column=0,
    sticky='nsew',
)
frame_path.columnconfigure(0, weight=1)

tk.Label(
    frame_path,
    text='Введите путь к текстовому файлу:',
    font=('Corbel', 20),
).grid(
    row=0,
    column=0,
    columnspan=5,
    sticky='sw'
)
file_path = tk.StringVar()
tk.Entry(
    frame_path,
    textvariable=file_path,
    font=('Corbel', 18, 'bold'),
).grid(
    row=1,
    column=0,
    columnspan=5,
    sticky='nsew',
    pady=5,
    ipady=4
)


frame_panel = ttk.Frame(
    root,
    padding=(10, 0),
)
frame_panel.grid(
    row=1,
    column=0,
    sticky='nsew',
)
frame_panel.columnconfigure(0, weight=1)
frame_panel.columnconfigure(1, weight=3)
frame_panel.columnconfigure(2, weight=3)
frame_panel.columnconfigure(3, weight=3)
frame_panel.columnconfigure(4, weight=5)
frame_panel.columnconfigure(5, weight=5)

open_icon = tk.PhotoImage(file=open_icon_path)
tk.Button(
    frame_panel,
    image=open_icon,
    command=read_and_insert_text
).grid(
    row=0,
    column=0,
    sticky='nsew',
    padx=(0, 10),
)
but_B = tk.Button(
    frame_panel,
    text='B',
    font=('Current', 22, 'bold'),
    command=editor_set_bold
)
but_B.grid(
    row=0,
    column=1,
    sticky='nsew',
    padx=(0, 5),
)
tk.Button(
    frame_panel,
    text='I',
    font=('Current', 22, 'bold'),
    # command=
).grid(
    row=0,
    column=2,
    sticky='nsew',
    padx=(0, 5),
)
tk.Button(
    frame_panel,
    text='U',
    font=('Current', 22, 'bold'),
    # command=
).grid(
    row=0,
    column=3,
    sticky='nsew',
    padx=(0, 5),
)
tk.Button(
    frame_panel,
    text='Lower',
    font=('Current', 22, 'bold'),
    command=editor_set_lower
).grid(
    row=0,
    column=4,
    sticky='nsew',
    padx=(0, 5),
)
tk.Button(
    frame_panel,
    text='Upper',
    font=('Current', 22, 'bold'),
    command=editor_set_upper
).grid(
    row=0,
    column=5,
    sticky='nsew',
)


frame_text = ttk.Frame(
    root,
    padding=10,
)
frame_text.grid(
    row=2,
    column=0,
    sticky='nsew'
)
frame_text.rowconfigure(0, weight=1)
frame_text.columnconfigure(0, weight=1)

editor = tk.Text(
    frame_text,
    font=('Fira Mono', 17),
)
editor.grid(
    row=0,
    column=0,
    columnspan=5,
    sticky='nsew',
    pady=(5, 0)
)

root.mainloop()
