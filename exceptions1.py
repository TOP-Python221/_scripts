from string import ascii_letters


class NoSpaces(ValueError):
    def __init__(self, err_msg: str = ''):
        super().__init__(err_msg)


class FieldChecker:
    def __init__(self, text: str):
        self.text = text

    def get_words(self) -> list[str]:
        words = self.text.split()
        i = self.text.index('.')
        if len(words) > 1:
            return words, i
        else:
            # плохо!
            # raise ValueError("loaded text doesn't contain any space or eol")
            # хорошо!
            raise NoSpaces("loaded text doesn't contain any space or eol")


fc1 = FieldChecker('abc def.')
print(fc1.get_words())

# ... много кода

fc2 = FieldChecker(ascii_letters)
try:
    words, i = fc2.get_words()
# плохо!
# except ValueError:
# хорошо!
except NoSpaces:
    print('исключение перехвачено')

# ... много кода

print(i)
