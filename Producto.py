#Importaciones
import csv

class Producto:
    def __init__(self, nombre, cantidad, precio, ubicacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.total = 0

nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practica\Practica1\lista.inv"
with open(nombre_archivo, "r") as archivo:
    lector = csv.reader(archivo, delimiter=";")
    #Creando la lista
    lista_producto = []
    for lista in lector:
    #Extrayendo objetos del archivo
        nombre = lista[0]
        #Reemplazamos el nombre
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
    nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practica\Practica1\Instrucciones.mov"
    with open(nombre_archivo, "r") as archivo:
        lector = csv.reader(archivo, delimiter = ";")
        #Accedemos a la lista de Instrucciones
        for lista in lector:
            nombre = lista[0]
            cantidad = int(lista[1])
            ubicacion = lista[2]
            #Si es agregar stock en la primera posicion se ejecutara
            if "agregar_stock" in nombre:
                productoa = nombre.replace("agregar_stock ", "")
                #Verifica si la ubicacion existe
                existe = False
                #Reccore la lista original
                for c in lista_producto:
                    if c.nombre == productoa and c.ubicacion == ubicacion:
                        #Agregamos cantidad
                        c.cantidad += cantidad
                        #Multiplicacion de precio por cantidad
                        c.total = c.precio * c.cantidad
                        print("sumado", productoa, ubicacion, c.precio, c.total)
                        existe = True
                if not existe:
                    print("Error, no existe el producto en esa ubicacion", productoa, ubicacion)

            #Si es vender_producto en la primera posicion se ejecutara
            elif "vender_producto" in nombre:
                productov = nombre.replace("vender_producto ", "")
                #Verifica si la ubicacion existe
                existeU = False
                for c in lista_producto:
                    if c.ubicacion == ubicacion and c.nombre == productov:
                        #Si existe la ubicacion es True
                        existeU = True
                        if cantidad <= c.cantidad:
                            c.cantidad -= cantidad
                            c.total = c.precio * c.cantidad
                            print("restado", productov, ubicacion, c.precio, c.total)
                        else:
                            #Si la cantidad es mayor que
                            print("Error, producto insuficiente")
                if not existeU:
                    print("Error, no existe el producto en esa ubicacion", productov, ubicacion)

    #Imprime la lista con sus atributos
    for c in lista_producto:
        print(f"Nombre: {c.nombre}  Cantidad: {c.cantidad}  Ubicacion: {c.ubicacion}")   

instrucciones()