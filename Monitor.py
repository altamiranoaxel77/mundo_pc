class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio

    @property
    def id_monitor(self):
        return self.__id_monitor
    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self.__id_monitor = id_monitor

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def __str__(self):
        return f'[Monitor] ID: {self.id_monitor} - marca: {self.marca} - tamanio: {self.tamanio}'