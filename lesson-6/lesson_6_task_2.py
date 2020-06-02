class Road:

    def __init__(self, width, length):
        self._length = length
        self._width = width

    def total(self):
        return f'При длине {self._length}м и ширине {self._width}м понадобится ' \
               f'{int(self._length * self._width * 25 * 5) / 1000} тонн асфальта '


weight = Road(20, 5000)
print(weight.total())
weight = Road(25, 500)
print(weight.total())
