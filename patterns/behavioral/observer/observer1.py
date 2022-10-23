"""Демонстратор Наблюдателя: базовая реализация."""

class Camera:
    """Камера наблюдения. (Наблюдатель)"""
    id_ = 0

    def __init__(self, name: str):
        self.id = self.id_
        self.__class__.id_ += 1
        self.name = name

    def make_photo(self):
        """Реакция наблюдателя на событие."""
        print(f'фото с камеры {self.name}')

    def __hash__(self):
        return self.id


class CameraSystem:
    """Пост управления камерами. (Субъект наблюдения)"""
    def __init__(self):
        self.cameras: set[Camera] = set()

    def connect(self, camera: Camera):
        """Подключает камеру к посту управления. (Подписка)"""
        self.cameras.add(camera)

    def disconnect(self, camera: Camera):
        """Отключает камеру от поста управления. (Отмена подписки)"""
        self.cameras.remove(camera)

    def certain_event_notify(self):
        """Оповещает наблюдателей о конкретном событии."""
        for camera in self.cameras:
            camera.make_photo()



control = CameraSystem()

c1 = Camera('Северная')
c2 = Camera('Северо-Восточная')
c3 = Camera('Восточная')

control.connect(c1)
control.connect(c2)
control.connect(c3)

control.certain_event_notify()
print()

control.disconnect(c2)

control.certain_event_notify()
print()
