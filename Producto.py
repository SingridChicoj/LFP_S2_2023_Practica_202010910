#Importaciones
import csv


#Creando la lista
lista_producto = []

jump = "------------------------------------------------------"


class Producto:
    def __init__(self, nombre, cantidad, precio, ubicacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.ubicacion = ubicacion
        self.total = 0


def inventario():
    #D:\Lenguajes1\Lenguajes 1.2\Lab\Practicas\LFP_S2_2023_Practica_202010910\Pruebas\inventario
    nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practicas\LFP_S2_2023_Practica_202010910\Pruebas\inventario.inv"
    with open(nombre_archivo, "r") as archivo:
        lector = csv.reader(archivo, delimiter=";")
        for lista in lector:
        #Extrayendo objetos del archivo
            nombre = lista[0]
            producto = nombre.replace("crear_producto ", "") #Reemplazamos el nombre
            try:
                cantidad = int(lista[1])
            except ValueError:
                print("Error, cantidad invalida")
            precio = float(lista[2])
            ubicacion = lista[3]
            #Agregando los atributos al objeto
            nuevo_producto = Producto(producto, cantidad, precio, ubicacion)
            #Agregamos el objeto a la lista
            lista_producto.append(nuevo_producto)
            total = precio * cantidad
            print(f"Producto; Nombre: {producto}  Cantidad: {cantidad}  Precio: {precio}  Total: {total}   Ubicacion: {ubicacion}")


def instrucciones():
    #D:\Lenguajes1\Lenguajes 1.2\Lab\Practicas\LFP_S2_2023_Practica_202010910\Pruebas\movimientos
    nombre_archivo = "D:\Lenguajes1\Lenguajes 1.2\Lab\Practicas\LFP_S2_2023_Practica_202010910\Pruebas\movimientos.mov"
    with open(nombre_archivo, "r") as archivo:
        lector = csv.reader(archivo, delimiter = ";")
        #Accedemos a la lista de Instrucciones
        for lista in lector:
            nombre = lista[0]
            cantidad = float(lista[1])
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
                        if cantidad > c.cantidad:
                            #Si la cantidad es mayor que
                            print("Error, producto insuficiente")
                if not existeU:
                    print("Error, no existe el producto en esa ubicacion", productov, ubicacion)

    #Imprime la lista con sus atributos
    for c in lista_producto:
        print(f"Nombre: {c.nombre}  Cantidad: {c.cantidad}  Ubicacion: {c.ubicacion}")   

def informe():
    #Ruta donde se guardara mi archivo .txt
    archivo = open('Informe.txt','w', encoding="utf-8") #Utf-8 para las tildes
    archivo.write('Informe de Inventario: \n')
    archivo.write(' \n') #Salto de linea
    archivo.write('Producto    Cantidad    Precio Unitario    Valor Total    Ubicación \n')
    archivo.write('-------------------------------------------------------------------------- \n')
    #Recorro mi lista para imprimir mis atributos
    for c in lista_producto:
        c.total = c.precio * c.cantidad
        #Creando/Escribiendo mi archivo .txt
        archivo.write(f"{c.nombre}      {c.cantidad}          {c.precio}                {c.total}            {c.ubicacion} \n")

def menu():
    print(jump)
    print("Practica 1 - Lenguajes formales y de programacion 1")
    print(jump)
    print("Sistema de Inventario")
    print()
    print("1. Cargar Inventario inicial ")
    print("2. Cargar Instrucciones de movimientos ")
    print("3. Crear Informe de Inventario ")
    print("4. Salir")
    print()
    entrada = input("Ingrese una opcion: ")
    print()
    print(jump)
    if entrada == "4":
        print("Adios, regresa pronto")
        quit()
    else:
        while entrada != "4":
            if entrada == "1":
                print("Cargando inventario")
                print()
                entrada = ""
                inventario()
                menu2()
            elif entrada == "2":
                entrada = ""
                instrucciones()
                menu2()
            elif entrada == "3":
                entrada = ""
                informe()
                menu2()
            else:
                print("Seleccione una opcion correcta")
                entrada = ""
                menu2()


def menu2():
    print(jump)
    print()
    print("Sistema de Inventario")
    print()
    print("1. Cargar Inventario inicial ")
    print("2. Cargar Instrucciones de movimientos ")
    print("3. Crear Informe de Inventario ")
    print("4. Salir")
    print()
    entrada = input("Ingrese una opcion: ")
    print()
    print(jump)
    if entrada == "4":
        print("Adios, regresa pronto")
        quit()
    else:
        while entrada != "4":
            if entrada == "1":
                print("Cargando Inventario")
                print()
                entrada = ""
                inventario()
                menu2()
            elif entrada == "2":
                print("Cargando Instrucciones de movimientos")
                print()
                entrada = ""
                instrucciones()
                menu2()
            elif entrada == "3":
                print("Creando Informe de Inventario")
                print()
                entrada = ""
                informe()
                menu2()
            else:
                print("Seleccione una opcion correcta")
                entrada = ""
                menu2()

menu()