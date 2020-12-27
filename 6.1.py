import time

class TrafficLight():
    def __init__(self, color):
        self.__color = color

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'Yellow'
        print(self.__color)
        time.sleep(3)
        self.__color = 'Green'
        print(self.__color)


trafficlight_1 = TrafficLight('Red')

trafficlight_1.running()


