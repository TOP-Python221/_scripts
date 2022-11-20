class Cell:
    """
    Описывает сущность одной клетки игрового поля.
    """
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.state: str = 'closed'
        self.mined: bool = False
        self.counter: int = 0

    mark_cycle: list[str] = ('closed', 'flagged', 'questioned')
    def next_mark(self) -> None:
        """Циклически переключает состояния клетки."""
        if self.state in self.mark_cycle:
            i = self.mark_cycle.index(self.state)
            self.state = self.mark_cycle[(i+1) % len(self.mark_cycle)]

    def open(self) -> None:
        """Переключает клетку в состояние 'открыто'."""
        if self.state != 'flagged':
            self.state = 'opened'


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

        self.first_step = True
        self.game_over = False

        self.table = []
        for i in range(self.rows):
            self.table += [[]]
            for j in range(self.columns):
                self.table[i] += [Cell(i, j)]


class View:
    pass


class Controller:
    pass


if __name__ == '__main__':
    m = Model()
    # v = View()
    # c = Controller(m, v)

