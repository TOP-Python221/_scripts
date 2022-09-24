# <div>
#     <ul>
#         <li>...</li>
#         <li>...</li>
#     </ul>
# </div>

class HTMLElement:
    indent_size = 4

    def __init__(self, name: str, text: str = ''):
        self.name = name
        self.text = text
        self.elements: list['HTMLElement'] = []

    def __str__(self) -> str:
        return self.__str()

    def __str(self, indent_level: int = 0) -> str:
        indent = ' '*indent_level*self.indent_size
        opentag = f'{indent}<{self.name}>{self.text}'
        nesttags = ''
        if self.elements:
            for elem in self.elements:
                nesttags += f'\n{elem.__str(indent_level+1)}'
            nesttags += '\n'
        else:
            indent = ''
        closetag = f'{indent}</{self.name}>'
        return opentag + nesttags + closetag

    @staticmethod
    def create(name: str, text: str = ''):
        return HTMLBuilder(HTMLElement(name, text))


class HTMLBuilder:
    def __init__(self, root):
        if isinstance(root, str):
            self.root = HTMLElement(root)
        else:
            self.root = root

    def add_sibling(self, name: str, text: str = '') -> 'HTMLBuilder':
        child = HTMLElement(name, text)
        self.root.elements.append(child)
        return self

    def add_child(self, name: str, text: str = '') -> 'HTMLBuilder':
        child = HTMLElement(name, text)
        self.root.elements.append(child)
        return HTMLBuilder(child)

    def __str__(self):
        return str(self.root)


# мы так не хотим
# div = HTMLElement('div')
# div.elements.append(HTMLElement('ul'))
# div.elements[0].elements.append(HTMLElement('li', 'first'))
# div.elements[0].elements.append(HTMLElement('li', 'second'))

div = HTMLBuilder('div')
div.add_child('ul')\
    .add_sibling('li', 'first')\
    .add_sibling('li', 'second')
print(div)

body = HTMLElement.create('body')
menu = body.add_child('div').add_child('ul')
menu.add_sibling('li', 'File')\
    .add_sibling('li', 'Edit')\
    .add_sibling('li', 'View')\
    .add_sibling('li', 'Navigate')\
    .add_sibling('li', 'Code')\
    .add_sibling('li', 'Refactor')\
    .add_sibling('li', 'Run')\
    .add_sibling('li', 'Tools')\
    .add_sibling('li', 'Git')\
    .add_sibling('li', 'Window')\
    .add_sibling('li', 'Help')
print(body)

