class pasajero:
    def __init__(self, dni, nombre, origen, destino):
        self.__dni = dni#int
        self.__nombre = nombre#string
        self.__origen = origen#string
        self.__destino = destino#string

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        try:
            n_dni = int(dni)
        except ValueError or TypeError:
             "Coloque un numero"
        else:
            self.__dni = n_dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def origen(self):
        return self.__origen

    @origen.setter
    def origen(self, origen):
        self.__origen = origen

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    #Funcion
    def dar_precio_pasaje(self,recorrido):
        i = 0
        total = 0
        while i != len(recorrido.recorrido):
            if (self.destino) == (recorrido.recorrido[i].destino):
                total = (recorrido.recorrido[i].precio) + total
                return total
            else:
                total = (recorrido.recorrido[i].precio) + total
                i = i + 1

#p1= pasajero(6452312,"Juan Perez","caba","lujan")
#p2 = pasajero(3654656,"Luis Lopez","misiones","concorida")
#p3 = pasajero(4546654,"Gimena DelMonte","escobar","parana")

