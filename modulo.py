def leer_opcion():

    while True:

        try:

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 7:
                return opcion

            print("Debe seleccionar una opción válida.")

        except ValueError:

            print("Debe ingresar un número entero.")


def stock_categoria(categoria, productos, inventario):

    total = 0

    for codigo in productos:

        if productos[codigo][1].lower() == categoria.lower():

            total += inventario[codigo][0]

    print(f"Stock total de {categoria}: {total}")


def buscar_precio(precio_min, precio_max, productos, inventario):

    lista = []

    for codigo in productos:

        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:

            lista.append(productos[codigo][0] + "--" + codigo)

    lista.sort()

    if len(lista) == 0:

        print("No existen productos en ese rango.")

    else:

        for producto in lista:

            print(producto)


def buscar_codigo(codigo, productos):

    return codigo.upper() in productos


def actualizar_precio(codigo, nuevo_precio, productos):

    codigo = codigo.upper()

    if codigo in productos:

        productos[codigo][2] = nuevo_precio
        return True

    return False


def validar_codigo(codigo, productos):

    codigo = codigo.strip().upper()

    if codigo == "":
        return False

    if codigo in productos:
        return False

    return True


def validar_nombre(nombre):

    return nombre.strip() != ""


def validar_categoria(categoria):

    return categoria.strip() != ""


def validar_precio(precio):

    return precio > 0


def validar_disponible(opcion):

    opcion = opcion.strip().lower()

    if opcion == "s" or opcion == "n":
        return True

    return False


def validar_stock(stock):

    return stock >= 0


def validar_vendidos(vendidos):

    return vendidos >= 0


def agregar_producto(codigo,
                     nombre,
                     categoria,
                     precio,
                     disponible,
                     stock,
                     vendidos,
                     productos,
                     inventario):

    codigo = codigo.upper()

    if codigo in productos:
        return False

    productos[codigo] = [
        nombre,
        categoria,
        precio,
        disponible
    ]

    inventario[codigo] = [
        stock,
        vendidos
    ]

    return True


def eliminar_producto(codigo, productos, inventario):

    codigo = codigo.upper()

    if codigo in productos:

        del productos[codigo]
        del inventario[codigo]

        return True

    return False


def mostrar_productos(productos, inventario):

    if len(productos) == 0:

        print("No existen productos registrados.")
        return

    for codigo in productos:

        print()
        print("CODIGO:", codigo)
        print("--------------------------")
        print("Nombre:", productos[codigo][0])
        print("Categoría:", productos[codigo][1])
        print("Precio: $", productos[codigo][2])
        print("Disponible:", productos[codigo][3])
        print("Stock:", inventario[codigo][0])
        print("Vendidos:", inventario[codigo][1])
        print("--------------------------")















        #Profe apiadese de mi