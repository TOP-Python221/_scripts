from abc import ABC, abstractmethod
from enum import Enum


class ListStrategy(ABC):
    """Стратегия формирования строкового представления списка с использованием различных языков разметки."""
    @abstractmethod
    def start(self, buffer: list):
        pass

    @abstractmethod
    def add_item(self, buffer: list, item: str):
        pass

    @abstractmethod
    def end(self, buffer: list):
        pass


class HtmlStrategy(ListStrategy):
    def start(self, buffer: list):
        buffer.append('<ul>')

    def add_item(self, buffer: list, item: str):
        buffer.append(f'\t<li>{item}</li>')

    def end(self, buffer: list):
        buffer.append('</ul>')


class MarkdownStrategy(ListStrategy):
    def start(self, buffer: list):
        pass

    def add_item(self, buffer: list, item: str):
        buffer.append(f' * {item}')

    def end(self, buffer: list):
        pass


class OutputFormat(Enum):
    HTML = 1
    MARKDOWN = 2


class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HtmlStrategy()):
        """
        :param list_strategy: экземпляр класса, определяющего стратегию формирования строкового представления списка с использованием языка разметки
        """
        self.strategy = list_strategy
        self.items: tuple = ()
        self.output_buffer: list[str] = []

    def set_output_format(self, output_format: OutputFormat):
        if output_format is OutputFormat.HTML:
            self.strategy = HtmlStrategy()
        elif output_format is OutputFormat.MARKDOWN:
            self.strategy = MarkdownStrategy()
        self.__generate_output()

    def set_items(self, item1: str, *items: str):
        self.items = (item1, ) + items
        self.__generate_output()

    def __generate_output(self):
        self.output_buffer.clear()
        self.strategy.start(self.output_buffer)
        for item in self.items:
            self.strategy.add_item(self.output_buffer, item)
        self.strategy.end(self.output_buffer)

    def __str__(self):
        return '\n'.join(self.output_buffer)


elements = ['File', 'Edit', 'View', 'Navigate', 'Code', 'Refactor', 'Run']

tp = TextProcessor()

tp.set_items(*elements)
print(tp)

print()

tp.set_output_format(OutputFormat.MARKDOWN)
print(tp)
