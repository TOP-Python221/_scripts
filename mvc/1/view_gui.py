"""View (MVC): GUI представление."""

from tkinter import Tk, Frame, Label, Entry, Button, Text, StringVar

import controller as ctrl


def start_view():
    lbl_text.set('Добро пожаловать в демонстратор MVC!')
    root.after(2000, ask_view)
    root.mainloop()


def ask_view():
    lbl_text.set('Вывести все записи из БД? [y/n]')
    ctrl.validate_answer()


def answer_view() -> str:
    return answer.get()


def show_all(people: tuple):
    lbl_text.set(f'В базе данных {len(people)} записей')
    people_str = '\n'.join(str(pers) for pers in people)
    bot_txt.insert('1.0', people_str)
    root.after(10000, ctrl.end)


def end_view():
    lbl_text.set('Пока!')
    root.after(2000, exit)


root = Tk()
root.title('Демонстратор MVC')
root.geometry('500x1100-50-50')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

mframe = Frame(root)
mframe.grid(
    row=0,
    column=0,
    sticky='nsew',
    padx=5,
    pady=5
)

mframe.rowconfigure(0, weight=0)
mframe.rowconfigure(1, weight=0)
mframe.rowconfigure(2, weight=1)
mframe.columnconfigure(0, weight=1)
mframe.columnconfigure(1, weight=0)

lbl_text = StringVar()
Label(
    mframe,
    textvariable=lbl_text,
    font=22
).grid(
    row=0,
    column=0,
    columnspan=2,
    sticky='nsw'
)

answer = StringVar()
Entry(
    mframe,
    textvariable=answer,
    font=('Courier New', 18, 'bold')
).grid(
    row=1,
    column=0,
    sticky='nsew',
    padx=(0, 5),
    pady=5
)

Button(
    mframe,
    text='\u2193',
    font=20,
    command=ask_view
).grid(
    row=1,
    column=1,
    sticky='nsew',
    pady=5
)

bot_txt = Text(mframe, font=('Arial', 16))
bot_txt.grid(
    row=2,
    column=0,
    columnspan=2,
    sticky='nsew'
)


if __name__ == '__main__':
    lbl_text.set('Welcome!')
    root.mainloop()
