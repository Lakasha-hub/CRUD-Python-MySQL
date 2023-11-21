import random
import string

# Función para imprimir los productos en pantalla
def imprimir_productos(productos):
    print(" ---- Productos ---- ")
    contador_productos = 1
    for prod in productos:
        # Agrego las propiedades del producto a la línea a imprimir (cada línea representa un producto)
        linea = " {0}) Título: {1} | Precio: {2}$ | Categoría: {3} | Código de Producto: {4} | Ult.Modificación: {5} "
        print(linea.format(contador_productos, prod[1], prod[2], prod[3], prod[4], prod[5]))
        contador_productos += 1
    print(" ")

# Función para registrar multiples productos
def registrar_productos():
    nuevos_productos = []
    print("Ingrese 'exit' para salir\n")
    titulo = input("Ingresa el titulo del nuevo producto: ")
    while titulo.lower() != "exit":

        precio_correcto = False
        while not precio_correcto:
            precio = input("Ingresa el precio del nuevo producto: ")
            # Verifico que el campo precio sea un número 
            if precio.isnumeric():
                if float(precio) > 0:
                    # Luego lo convierto a tipo de dato float
                    precio = float(precio)
                    precio_correcto = True
                else:
                    print("El precio debe ser mayor a 0 (cero)\n")
            else:
                print("El precio debe ser un número\n")
        
        categoria = input("Ingresa la categoria del nuevo producto: ")
        # Genera un código de producto automaticamente
        codigo_producto = generar_codigo()
        
        # Se crea el nuevo producto y se lo guarda en una tupla
        prod = (titulo, precio, categoria, codigo_producto)
        nuevos_productos.append(prod)
        print("Producto agregado correctamente\n")

        # Reinicio del ciclo
        titulo = input("Ingresa el titulo del nuevo producto: ")
    return nuevos_productos

# Función que genera un código único de 6 dígitos para un producto
def generar_codigo():
    # Almacena todas las letras y dígitos
    caracteres = string.ascii_letters + string.digits
    # Agrega a una cadena vacía los 6 caracteres alfanuméricos aleatorios
    codigo = ''.join(random.choices(caracteres, k=6))
    # Convierte las letras del código a mayúscula
    codigo = codigo.upper()
    return codigo

# Función que solicita los nuevos valores de un producto para su actualización
def solicitar_nuevos_valores_prod(productos):
    # Imprimo los productos para que el usuario visualice los códigos
    imprimir_productos(productos)

    print("Ingrese 'exit' para salir\n")
    codigo_prod = input("Ingresa el código del producto a actualizar: ").upper()
    codigo_existe = False
    while codigo_prod.lower() != "exit":
        # Valido que el código existe
        for prod in productos:
            if prod[4] == codigo_prod:
                codigo_existe = True
                break
        if codigo_existe:
            
            # Solicito el nuevo titulo
            titulo = input("Ingresa el nuevo titulo del producto: ")
            
            precio_correcto = False
            while not precio_correcto:
                # Solicito el nuevo precio
                precio = input("Ingresa el nuevo precio del producto: ")
                # Verifico que el campo precio sea un número 
                if precio.isnumeric():
                    if float(precio) > 0:
                        # Luego lo convierto a tipo de dato float
                        precio = float(precio)
                        precio_correcto = True
                    else:
                        print("El precio debe ser mayor a 0 (cero)\n")
                else:
                    print("El precio debe ser un número\n")

            # Solicito la nueva categoria
            categoria = input("Ingresa la nueva categoria del producto: ")
            # Se crea el producto con los nuevos valores y se lo guarda en una tupla
            prod_actualizado = (titulo, precio, categoria, codigo_prod)
        else:
            prod_actualizado = None
        
        return prod_actualizado
    
    if codigo_prod.lower() == "exit":
        return codigo_prod.lower()

# Función que solicita el código de un producto para su eliminación
def solicitar_codigo(productos):
    # Imprimo los productos para que el usuario visualice los códigos
    imprimir_productos(productos)

    print("Ingrese 'exit' para salir\n")
    codigo_prod = input("Ingresa el código del producto a eliminar: ")
    codigo_existe = False
    while codigo_prod.lower() != "exit":
        for prod in productos:
            if prod[4] == codigo_prod:
                codigo_existe = True
                break
        if not codigo_existe:
            codigo_prod = ""
        return codigo_prod 
    
    if codigo_prod.lower() == "exit":
        return codigo_prod.lower()

# Función que calcula el promedio de precios de los productos
def calcular_promedio_precios(productos):
    contador = 0
    suma_precios = 0
    for prod in productos:
        suma_precios += prod[2]
        contador += 1
    return suma_precios / contador