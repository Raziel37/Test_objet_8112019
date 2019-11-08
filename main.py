from personas import pasajero as pasajero
from transportes import transporte as transporte
from recorridos import recorridos as recorridos
from recorridos import segmentos as segmento

p1 = pasajero.pasajero(6452312,"Juan Perez","caba","lujan")
p2 = pasajero.pasajero(3654656,"Luis Lopez","misiones","concordia")
p3 = pasajero.pasajero(4546654,"Gimena DelMonte","escobar","parana")

t1 = transporte.transporte("abol4500",60,0.80,110)
t2 = transporte.transporte("csrl7485",70,1.01,140)
t1.agregar_pasajero(p1)
t1.agregar_pasajero(p2)
t1.agregar_pasajero(p3)

s1 = segmento.segmento("caba","escobar",300,150,250)
s2 = segmento.segmento("escobar","misiones",200,300,240)
s3 = segmento.segmento("misiones","parana",400,200,120)
s4 = segmento.segmento("parana","concordia",400,300,150)
s5 = segmento.segmento("concordia","lujan",300,200,150)

r1 = recorridos.recorrido("Recorrido1")
r1.agregar_segmento(s1)
r1.agregar_segmento(s2)
r1.agregar_segmento(s3)
r1.agregar_segmento(s4)
r1.agregar_segmento(s5)
#r1.eliminar_segmento(s2)

#print(r1.recorrido[(len(r1.recorrido)-1)].destino)



"""print(t1.consumo)
i = 0
total = 0
precio_combustible = 2
while i != (len(r1.recorrido)):
    total = r1.recorrido[i].dar_costo(t1,precio_combustible)+total
    i = i + 1
print(total)

print(r1.dar_costo(t1,2))"""

"""i = 0
total = 0
while i != len(r1.recorrido):
    if (p1.destino) == (r1.recorrido[i].destino):
        total = (r1.recorrido[i].precio) + total
        print(total)
        break
    else:
        total = (r1.recorrido[i].precio) + total
        i = i + 1"""


"""print(p1.dar_precio_pasaje(r1))
print(p2.dar_precio_pasaje(r1))
print(p3.dar_precio_pasaje(r1))
print(t1.pasajeros[0].dar_precio_pasaje(r1))
#print(t1.pasajeros[1].dar_precio_pasaje(r1))
#print(t1.pasajeros[2].dar_precio_pasaje(r1))
print(len(t1.pasajeros))
i = 0
total = 0
while i != len(t1.pasajeros):
    total = t1.pasajeros[i].dar_precio_pasaje(r1)+total
    i = i+1
print(total)"""
