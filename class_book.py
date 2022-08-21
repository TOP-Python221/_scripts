

# Козырев
class Book:
    def __init__(self, pages: int, adoration: str, genre: str):
        self.pages = pages
        self.adoration = adoration
        self.genre = genre

b1 = Book(200, 'solid', 'Sci-Fi')


class FantasyBook:
    genre = 'Fantasy'
    def __init__(self, pages: int, adoration: str):
        self.pages = pages
        self.adoration = adoration

b2 = FantasyBook(252, 'solid')
b3 = FantasyBook(120, 'soft')



# Соколов
class BookObject:
    def __init__(self,
                 thickness: int,
                 height: int,
                 number_of_pages: int,
                 interesting: bool = True):
        self.thickness = thickness
        self.height = height
        self.number_of_pages = number_of_pages
        self.interesting = interesting


# Ульянов
class BookObject2:
    def __init__(self, height: int, width: int, pages: int, genre: str):
        self.height = height
        self.width = width
        self.pages = pages
        self.genre = genre

