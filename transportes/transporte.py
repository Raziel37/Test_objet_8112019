from personas import pasajero

class transporte:
    def __init__(self, patente, capacidad, consumo, vel_max, *args):
        self.__patente = patente#string
        self.__capacidad = capacidad#int
        self.__consumo = consumo#float
        self.__vel_max = vel_max#float
        self.__pasajeros = [*args]#obj

    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, patente):
        try:
            n_patente = str(patente)
        except ValueError or TypeError:
             "Coloque la patente como string"
        else:
            self.__patente = n_patente

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, capacidad):
        try:
            n_capacidad = int(capacidad)
        except ValueError or TypeError:
             "Debe ser un numero sin coma"
        else:
            self.__capacidad = n_capacidad

    @property
    def consumo(self):
        return self.__consumo

    @consumo.setter
    def consumo(self, consumo):
        try:
            n_consumo = float(consumo)
        except ValueError or TypeError:
             "Se debe colocar un numero"
        else:
            self.__consumo = n_consumo

    @property
    def vel_max(self):
        return self.__vel_max

    @vel_max.setter
    def vel_max(self, vel_max):
        try:
            n_vel_max = float(vel_max)
        except ValueError or TypeError:
             "Se debe colocar un numero"
        else:
            self.__vel_max = n_vel_max

    @property
    def pasajeros(self):
        return self.__pasajeros

    #Agrgar-remover pasajeros
    def agregar_pasajero(self, pasajero):
        if self.__pasajeros.count(pasajero) == 1:
            return "Pasajero ya esta agregado"
        else:
            self.__pasajeros.append(pasajero)
            return "Pasajero agregado exitosamente"

    def remover_pasajero(self, pasajero):
        if self.__pasajeros.count(pasajero) == 1:
            self.__pasajeros.remove(pasajero)
            return "Pasajero Removido"
        else:
            return "Pasajero no figura en el transporte"

    #Transporte_detalles
    def dar_porcentaje_ocupacion(self):
        disponible = self.__capacidad-len(self.__pasajeros)
        print("Ocupado: ", len(self.__pasajeros))
        print("Disponible: ", disponible)
        return#float

    def dar_ingreso_viaje(self,recorrido):
        i = 0
        total = 0
        while i != len(self.pasajeros):
            total = self.pasajeros[i].dar_precio_pasaje(recorrido) + total
            i = i + 1
        return total

#t1 = transporte("abol4500",60,40,110)
#t2 = transporte("csrl7485",70,50,140)


