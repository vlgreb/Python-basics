class Road():
    def __init__(self, length, widht):
        self._length = length
        self._width = widht

    def mass(self):
        mass_asphalt = self._length * self._width * 25 * 5
        print(f'Необходимая масса асфальта: {mass_asphalt/1000} т')


highway = Road(10000, 20)
highway.mass()

