class recorrido:
    def __init__(self, nombre, *args):
        self.__nombre = nombre#string
        self.__recorrido = [*args]#segmentos

    @property
    def nombre(self):
        return self.__nombre

    @property
    def recorrido(self):
        return self.__recorrido



    #Funciones_Transporte
    def dar_costo(self, transporte, precio_combustible):
        i = 0
        total = 0
        while i != (len(self.recorrido)):
            total = self.recorrido[i].dar_costo(transporte, precio_combustible) + total
            i = i + 1
        return total

    def dar_consumo(self, transporte):
        consumo_total = transporte.consumo * self.dar_longitud()
        return consumo_total  # float

    def dar_tiempo_minimo(self, transporte):
        total = self.dar_longitud()/transporte.vel_max
        return total#float


    #Segmentos manipulation
    def agregar_segmento(self, segmento):
        if self.__recorrido.count(segmento) == 1:
            return "Segmento ya esta agregado"
        else:
            self.__recorrido.append(segmento)
            return "Segmento agregado exitosamente"

    def eliminar_segmento(self, segmento):
        if self.__recorrido.count(segmento) == 1:
            self.__recorrido.remove(segmento)
            return "Segmento Removido"
        else:
            return "Segmento no figura en el recorrido"

    #Funciones_Locales
    def dar_longitud(self):
        i = 0
        total = 0
        while i != (len(self.recorrido)):
            # print(self.recorrido[i].longitud)
            total = self.recorrido[i].longitud + total
            i = i + 1
        return total

    def existe_localidad(self, localidad):
        i = 0
        while i != (len(self.recorrido)):
            # print(self.recorrido[i].destino)
            if self.recorrido[i].destino == localidad:
                return True
            else:
                i = i + 1

    def esta_completo(self):
        i = 0
        while i != (len(self.recorrido)):
            if self.recorrido[i].destino == self.recorrido[(len(self.recorrido) - 1)].destino:
                #print("Recorrido completo")
                return True
            if self.recorrido[i].destino != self.recorrido[(i + 1)].origen:
                #print("Error recorrido incompleto")
                return False
            if self.recorrido[i].destino == self.recorrido[(i + 1)].origen:
                i = i + 1