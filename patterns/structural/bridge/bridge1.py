# raster vector
# circle triangle square cat

# взрывной рост количества классов
# RasterCircle VectorCircle RasterTriangle VectorTriangle RasterSquare VectorSquare...

from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_square(self, side: float):
        pass

    # def render_triangle ...


class RasterRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f'pixels for the circle of the radius {radius}')

    def render_square(self, side: float):
        print(f'pixels for the square of the {side}')


class VectorRenderer(Renderer):
    def render_circle(self, radius: float):
        print(f'the circle of the radius {radius}')

    def render_square(self, side: float):
        print(f'the square of the {side}')



class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer: Renderer, side: float):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor: float):
        self.side *= factor


rr = RasterRenderer()
vr = VectorRenderer()

cr1 = Circle(rr, 5)
cr2 = Circle(vr, 9)

cr1.draw()
cr2.draw()

cr2.resize(1/3)
cr2.draw()
