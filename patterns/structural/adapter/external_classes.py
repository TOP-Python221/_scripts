# найденный класс для работы с векторными изображениями
class VectorImage:
    def __init__(self, image_path: str):
        self.path = image_path

    @staticmethod
    def render() -> str:
        return 'svg'
