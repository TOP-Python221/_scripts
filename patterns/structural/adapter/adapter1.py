"""Демонстратор адаптера: реализация для одного класса."""

from abc import ABC, abstractmethod


# собственная объектная модель для работы с растровыми изображениями
class RasterInterface(ABC):
    @abstractmethod
    def draw(self):
        pass

class RasterImage(RasterInterface):
    def __init__(self, image_path: str):
        self.path = image_path

    def draw(self) -> str:
        return 'Drawing ' + self.get_image()

    def get_image(self) -> str:
        return self.path.rsplit('.', 1)[-1]


# найденный класс для работы с векторными изображениями
class VectorImage:
    def __init__(self, image_path: str):
        self.path = image_path

    @staticmethod
    def render() -> str:
        return 'svg'


class VectorAdapter(RasterInterface):
    def __init__(self, img_obj: VectorImage):
        self.image = img_obj

    def rasterize(self):
        return 'rasterized ' + self.image.render()

    def draw(self):
        return 'Drawing ' + self.rasterize()


rast_img1 = RasterImage('image_top.png')
rast_img2 = RasterImage('image_left.png')
rast_img3 = RasterImage('background.jpg')

print(rast_img1.draw())
print(rast_img2.draw())
print(rast_img3.draw(), end='\n\n')

vect_img1 = VectorImage('figure1.svg')
vect_img2 = VectorImage('figure2.svg')

gallery = [rast_img1, rast_img2, rast_img3, vect_img1, vect_img2]
try:
    for img in gallery:
        print(img.draw())
except AttributeError:
    print()

vect_img1 = VectorAdapter(vect_img1)
vect_img2 = VectorAdapter(vect_img2)

gallery = [rast_img1, rast_img2, rast_img3, vect_img1, vect_img2]
for img in gallery:
    print(img.draw())
