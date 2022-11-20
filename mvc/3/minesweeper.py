from enum import Enum
from random import randrange as rr
from typing import Optional, Generator

import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter.constants import BOTTOM, RIGHT, LEFT, X, SUNKEN

# переменные для аннотации
CellsTable = list[list['Cell']]
ButtonsBoard = list[list[tk.Button]]


class CellState(Enum):
    CLOSE = ''
    FLAG = 'P'
    QUESTION = '?'
    OPEN = 'o'

    @classmethod
    def cycling_states(cls):
        q = list(cls)
        q.remove(cls.OPEN)
        return q


class Cell:
    """
    Описывает сущность одной клетки игрового поля.
    """
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.state: CellState = CellState.CLOSE
        self.mined: bool = False
        self.counter: int = 0

    mark_cycle: list[CellState] = CellState.cycling_states()
    def next_mark(self) -> None:
        """Циклически переключает состояния клетки."""
        if self.state in self.mark_cycle:
            i = self.mark_cycle.index(self.state)
            self.state = self.mark_cycle[(i+1) % len(self.mark_cycle)]

    def open(self) -> None:
        """Переключает клетку в состояние 'открыто'."""
        if self.state is not CellState.FLAG:
            self.state = CellState.OPEN


MIN_ROWS = 5
MAX_ROWS = 30

MIN_COLUMNS = 5
MAX_COLUMNS = 30

MIN_MINES = 1
MAX_MINES = 800


class Model:
    """
    Моделирует игровое поле и игровые действия.
    """
    def __init__(self):
        self.start_game()

    def start_game(self,
                   rows: int = 15,
                   columns: int = 15,
                   mines: int = 50) -> None:
        """Инициализирует клетки нового игрового поля.

        :param rows: количество строк игрового поля
        :param columns: количество столбцов игрового поля
        :param mines: количество мин на игровом поле
        """
        if MIN_ROWS <= rows <= MAX_ROWS:
            self.rows = rows
        if MIN_COLUMNS <= columns <= MAX_COLUMNS:
            self.columns = columns
        if MIN_MINES <= mines <= MAX_MINES:
            self.mines = mines

        self.first_step: bool = True
        self.game_over: bool = False

        self.table: CellsTable = []
        for i in range(self.rows):
            self.table += [[]]
            for j in range(self.columns):
                self.table[i] += [Cell(i, j)]

    def generate_mines(self) -> None:
        """Располагает заданное количество мин на случайных клетках игрового поля."""
        for _ in range(self.mines):
            while True:
                i = rr(self.rows)
                j = rr(self.columns)
                cell = self.table[i][j]
                if not cell.mined and cell.state is not CellState.OPEN:
                    cell.mined = True
                    break

    def is_win(self) -> bool:
        """Проверяет, достигнут ли выигрыш."""
        for row in self.table:
            for cell in row:
                op_or_fl = cell.state is CellState.OPEN \
                           or cell.state is CellState.FLAG
                if not cell.mined and not op_or_fl:
                    return False
        return True

    def is_game_over(self) -> bool:
        """Проверяет, случился ли проигрыш."""
        return self.game_over

    def get_cell(self, row: int, column: int) -> Optional[Cell]:
        """Возвращает клетку по заданным индексам, если индексы находятся в заданном диапазоне, иначе None."""
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.table[row][column]
        else:
            return None

    def get_cell_neighbours(self, row: int, column: int) -> Generator:
        """Возвращает список клеток, соседних с клеткой, заданной переданными индексами."""
        neighbours = []
        for i in range(row-1, row+2):
            neighbours += [self.get_cell(i, column-1)]
            if i != row:
                neighbours += [self.get_cell(i, column)]
            neighbours += [self.get_cell(i, column+1)]
        return (cell for cell in neighbours if cell is not None)

    def get_mines_around_cell(self, row: int, column: int) -> int:
        """Подсчитывает и возвращает количество заминированных клеток рядом с клеткой, заданной переданными индексами."""
        neighbours = self.get_cell_neighbours(row, column)
        return sum(cell.mined for cell in neighbours)

    def next_cell_mark(self, row: int, column: int) -> None:
        """Переключает отметку на клетке."""
        cell = self.get_cell(row, column)
        if cell:
            cell.next_mark()

    def open_cell(self, row: int, column: int) -> None:
        """Открывает клетку, проверяет мину, подсчитывает количество мин рядом с открытой, рекурсивно открывает соседние пустые клетки."""
        cell = self.get_cell(row, column)
        if not cell:
            return

        cell.open()

        if cell.mined:
            self.game_over = True
            return

        if self.first_step:
            self.first_step = False
            self.generate_mines()

        cell.counter = self.get_mines_around_cell(row, column)

        if cell.counter == 0:
            neighbours = self.get_cell_neighbours(row, column)
            for n_cell in neighbours:
                if n_cell.state is CellState.CLOSE:
                    self.open_cell(n_cell.row, n_cell.column)



class View(tk.Frame):
    def __init__(self,
                 model_obj: Model,
                 controller_obj: 'Controller',
                 parent=None):
        super().__init__(parent)

        self.model = model_obj
        self.controller = controller_obj
        self.controller.set_view(self)

        self.create_board()
        self.create_panel()

    def create_board(self):
        try:
            self.board.pack_forget()
            self.board.destroy()

            self.rows.set(str(self.model.rows))
            self.columns.set(str(self.model.columns))
            self.mines.set(str(self.model.mines))
        except:
            pass

        self.board = tk.Frame(self)
        self.board.pack()

        self.buttons: ButtonsBoard = []
        for i in range(self.model.rows):
            row = tk.Frame(self.board)
            row.pack()
            self.buttons += [[]]
            for j in range(self.model.columns):
                btn = tk.Button(
                    row,
                    width=2, height=1,
                    font=('Corbel', 20),
                    command=lambda r=i, c=j: self.controller.on_left_click(r, c)
                )
                btn.pack(side=LEFT)
                btn.bind(
                    '<Button-3>',
                    lambda event, r=i, c=j: self.controller.on_right_click(r, c)
                )
                self.buttons[i] += [btn]

    def create_panel(self):
        panel = tk.Frame(self)
        panel.pack(side=BOTTOM, fill=X)

        tk.Button(
            panel,
            text='Новая игра',
            font=('Corbel', 16),
            command=self.controller.start_new_game
        ).pack(side=RIGHT)

        self.mines = tk.StringVar(value=str(self.model.mines))
        tk.Spinbox(
            panel,
            from_=MIN_MINES,
            to=MAX_MINES,
            textvariable=self.mines,
            width=4,
            font=('Corbel', 16),
        ).pack(side=RIGHT)
        tk.Label(
            panel,
            text='Количество мин: ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)

        self.columns = tk.StringVar(value=str(self.model.columns))
        tk.Spinbox(
            panel,
            from_=MIN_COLUMNS,
            to=MAX_COLUMNS,
            textvariable=self.columns,
            width=3,
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        tk.Label(
            panel,
            text=' x ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)

        self.rows = tk.StringVar(value=str(self.model.rows))
        tk.Spinbox(
            panel,
            from_=MIN_ROWS,
            to=MAX_ROWS,
            textvariable=self.rows,
            width=3,
            font=('Corbel', 16)
        ).pack(side=RIGHT)
        tk.Label(
            panel,
            text='Размер поля: ',
            font=('Corbel', 16)
        ).pack(side=RIGHT)

    @property
    def game_settings(self) -> tuple[int, int, int]:
        return int(self.rows.get()), int(self.columns.get()), int(self.mines.get())

    @staticmethod
    def show_win_message():
        showinfo('Поздравляем!', 'Вы победили!')

    @staticmethod
    def show_game_over_message():
        showinfo('Игра окончена', 'Вы проиграли')

    def sync_model(self):
        for i in range(self.model.rows):
            for j in range(self.model.columns):
                cell = self.model.get_cell(i, j)
                if cell:
                    btn = self.buttons[i][j]

                    if cell.mined and self.model.is_game_over():
                        btn.config(bg='black', text='')

                    if cell.state is CellState.CLOSE:
                        btn.config(text=CellState.CLOSE.value)
                    elif cell.state is CellState.FLAG:
                        btn.config(text=CellState.FLAG.value)
                    elif cell.state is CellState.QUESTION:
                        btn.config(text=CellState.QUESTION.value)
                    elif cell.state is CellState.OPEN:
                        btn.config(relief=SUNKEN, text='')
                        if cell.counter > 0:
                            btn.config(text=cell.counter)
                        elif cell.mined:
                            btn.config(bg='red')

    def block_button(self, row: int, column: int, block: bool = True):
        btn = self.buttons[row][column]
        if not btn:
            return

        if block:
            btn.bind('<Button-1>', 'break')
        else:
            btn.unbind('<Button-1>')



class Controller:
    def __init__(self, model_obj: Model):
        self.model = model_obj
        self.view = None

    def set_view(self, view_obj: View):
        self.view = view_obj

    def start_new_game(self):
        settings = self.view.game_settings
        try:
            self.model.start_game(*settings)
        except:
            self.model.start_game(
                self.model.rows,
                self.model.columns,
                self.model.mines
            )
        self.view.create_board()

    def on_left_click(self, row: int, column: int):
        self.model.open_cell(row, column)
        self.view.sync_model()
        if self.model.is_win():
            self.view.show_win_message()
            self.start_new_game()
        elif self.model.is_game_over():
            self.view.show_game_over_message()
            self.start_new_game()

    def on_right_click(self, row: int, column: int):
        self.model.next_cell_mark(row, column)
        self.view.block_button(
            row, column,
            self.model.get_cell(row, column).state is CellState.FLAG
        )
        self.view.sync_model()


if __name__ == '__main__':
    m = Model()
    c = Controller(m)
    v = View(m, c)

    v.pack()
    v.mainloop()
