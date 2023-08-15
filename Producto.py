#Importaciones
from nodo import nodo

#Librerias
import csv

class Producto:
    def __init__(self, nombre, cantidad, precio, ubicacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.total = 0

nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practica\LFP_S2_2023_Practica_202010910\lista.inv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=";")
    #Creando la lista
    lista_producto = []
    for lista in lector:
    #Extrayendo objetos del archivo
        nombre = lista[0]
        producto = nombre.replace("crear_producto ", "")
        cantidad = int(lista[1])
        precio = float(lista[2])
        ubicacion = lista[3]
        nuevo_producto = Producto(producto, cantidad, precio, ubicacion)
        lista_producto.append(nuevo_producto)
        print(f"Producto; Nombre: {producto}  Cantidad: {cantidad}  Precio: {precio}  Ubicacion: {ubicacion}")

#Probando la lista
#for c in lista_producto:
    #print(c.nombre)
    #print(c.precio)


def instrucciones():
    nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practica\LFP_S2_2023_Practica_202010910\Instrucciones.mov"
    with open(nombre_archivo, "r") as archivo:
        lector = csv.reader(archivo, delimiter = ";")
        for lista in lector:
            nombre = lista[0]
            cantidad = int(lista[1])
            ubicacion = lista[2]
            if "agregar_stock" in nombre:
                producto = nombre.replace("agregar_stock ", "")
                for c in lista_producto:
                    if c.ubicacion == ubicacion and c.nombre == producto:
                        c.cantidad += cantidad
                        print("sumado")
                if c.nombre != producto and c.ubicacion != ubicacion:
                    print("Error, no existe el producto en esa ubicacion", ubicacion)
                    

            elif "vender_producto" in nombre:
                producto = nombre.replace("vender_producto ", "")
                existeC = False
                existeU = False
                for c in lista_producto:
                    if c.ubicacion == ubicacion:
                        if cantidad >= c.cantidad:
                            c.cantidad -= cantidad
                            print("restado")
                            existeC = True
                        else:
                            print("Error, producto insuficiente")
                if c.nombre != producto or c.ubicacion != ubicacion:
                    print("Error, no existe el producto en esa ubicacion", ubicacion)
                
                '''if not existeC:
                    print("Error, producto insuficiente ", cantidad)
                if not existeU:
                    print("Error, no existe el producto en esa ubicacin ", ubicacion)'''

    for c in lista_producto:
        print(f"Nombre: {c.nombre}  Cantidad: {c.cantidad}  Ubicacion: {c.ubicacion}")   


instrucciones()





