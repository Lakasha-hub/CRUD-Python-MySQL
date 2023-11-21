from database.connection import DAO
import functions
import os

def menu():

    # Limpieza de consola
    os.system("cls")

    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print(" ---- Menú Comercio ---- ")
            print(" 1) Listar Productos ")
            print(" 2) Agregar Productos ")
            print(" 3) Actualizar Producto ")
            print(" 4) Eliminar Producto ")
            print(" 5) Promedio de Precios ")
            print(" 6) Salir ")
            print(" ----------------------- ")

            # Solicito la opción al usuario
            opcion = int(input("Ingresa una opción: "))

            if opcion < 1 or opcion > 6:
                # Al ingresar una opción no valida el menú vuelve a ejecutarse 
                print("Opción no válida, ingrese nuevamente una opción\n")
            elif opcion == 6:
                # Al ingresar 6 el usuario no continuará utilizando el menú
                continuar = False
                break
            else:
                # Al ingresar una opcion correcta se ejecutá la opción y el menú finaliza
                opcion_correcta = True
                ejecutar_opcion(opcion)

def ejecutar_opcion(opt):

    os.system("cls")

    # Instancia del Data Access Object
    dao = DAO()

    if opt == 1:
        try:
            productos = dao.listar_productos()
            if len(productos) == 0:
                print("Aún no hay productos guardados\n")
            else:
                functions.imprimir_productos(productos)
        except:
            print("Ocurrió un error al intentar listar los productos\n")
    elif opt == 2:
        try:
            # Solicito al usuario los nuevos productos a agregar
            nuevos_productos = functions.registrar_productos()
            # Si el usuario no agrego ningún producto le notifico
            if len(nuevos_productos) == 0:
                print("No se agregó ningún producto\n")
            # Caso contrario los guardo en la base de datos 
            else:
                for prod in nuevos_productos:
                    dao.agregar_producto(prod)
        except:
            print("Ocurrió un error al intentar agregar los productos\n")
    elif opt == 3:
        try:
            productos = dao.listar_productos()
            if len(productos) == 0:
                print("No hay productos para actualizar\n")
            else:
                # Solicito al usuario los nuevos campos del producto a actualizar
                producto_actualizado = functions.solicitar_nuevos_valores_prod(productos)
                if producto_actualizado == "exit":
                    print("No se actualizó ningún producto\n")
                # Si se obtuvieron los nuevos valores correctamente 
                elif producto_actualizado:
                    # Se actualiza el producto
                    dao.actualizar_producto(producto_actualizado)
                    print("Producto actualizado correctamente\n")
                else:
                    print("No se encontró un producto con ese código\n") 
        except:
            print("Ocurrió un error al intentar actualizar el producto")
    elif opt == 4:
        try:
            productos = dao.listar_productos()
            if len(productos) == 0:
                print("No hay productos para eliminar\n")
            else:
                # Solicito al usuario el código del producto a eliminar
                codigo_prod = functions.solicitar_codigo(productos)
                if codigo_prod == "exit":
                    print("No se eliminó ningún producto\n")
                # Si el código existe, lo elimino
                elif not codigo_prod == "":
                    dao.eliminar_producto(codigo_prod)
                    print("Producto eliminado correctamente\n")
                else:
                    print("No se encontró un producto con ese código\n") 
        except:
            print("Ocurrió un error al intentar eliminar el producto")
    elif opt == 5:
        try:
            productos = dao.listar_productos()
            if len(productos) == 0:
                print("No hay productos para calcular el promedio de precios\n")
            else:
                promedio_precios = functions.calcular_promedio_precios(productos)
                print(f"El promedio de precios es: {promedio_precios}$\n")
        except:
            print("Ocurrió un error al intentar calcular el promedio de precios")
    else:
        # Al ingresar una opción no valida el menú vuelve a ejecutarse 
        print("Opción no válida, ingrese nuevamente una opción\n")

menu()