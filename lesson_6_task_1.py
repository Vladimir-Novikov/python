from time import sleep


class TrafficLight:
    __color = 'Красный', 'Желтый', 'Зеленый'

    def running(self):
        while True:
            print(self.__color[0], end='')
            sleep(7)
            print('\r', end='')
            print(self.__color[1], end='')
            sleep(2)
            print('\r', end='')
            print(self.__color[2], end='')
            sleep(4)
            print('\r', end='')


light = TrafficLight()
print(light.running())
