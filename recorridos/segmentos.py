class segmento:
    def __init__(self, origen ,destino, precio, precio_peajes, longitud):
        self.__origen = origen#string
        self.__destino = destino#string
        self.__precio = precio#float
        self.__precio_peajes = precio_peajes#float
        self.__longitud = longitud#float

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

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        try:
            n_precio = float(precio)
        except ValueError or TypeError:
            "Error coloque un numero"
        else:
            self.__precio = n_precio

    @property
    def precio_peajes(self):
        return self.__precio_peajes

    @precio_peajes.setter
    def precio_peajes(self, precios_peajes):
        try:
            n_precios_peajes = float(precios_peajes)
        except ValueError or TypeError:
            "Error coloque un numero"
        else:
            self.__precio_peajes = n_precios_peajes

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, longitud):
        try:
            n_longitud = float(longitud)
        except ValueError or TypeError:
            print("Error coloque un numero")
        else:
            self.__longitud = n_longitud

    #Funcion
    def dar_costo(self, transporte, precio_combustible):
        total = ((self.longitud * precio_combustible) / transporte.consumo) + self.precio_peajes
        return total  # float

#s1 = segmento("caba","escobar",300,150,250)
#s2 = segmento("escobar","misiones",200,300,240)
#s3 = segmento("misiones","parana",400,200,120)
#s4 = segmento("parana","concordia",400,300,150)
#s5 = segmento("concorida","lujan",300,200,150)
