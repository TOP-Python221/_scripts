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



# мы так не хотим
div = HTMLElement('div')
div.elements.append(HTMLElement('ul'))
div.elements[0].elements.append(HTMLElement('li', 'first'))
div.elements[0].elements.append(HTMLElement('li', 'second'))

print(div)
