import modulo


def main():

    productos = {
        "P101": ["Cuaderno", "Papelería", 2490, True],
        "P102": ["Lápiz", "Papelería", 590, True],
        "P103": ["Botella", "Accesorios", 6990, False],
        "P104": ["Mochila", "Accesorios", 24990, True]
    }

    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25]
    }

    while True:

        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por categoría")
        print("2. Buscar productos por rango de precio")
        print("3. Actualizar precio")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Mostrar productos")
        print("7. Salir")
        print("====================================")

        opcion = modulo.leer_opcion()

        if opcion == 1:

            categoria = input("Ingrese la categoría: ")

            modulo.stock_categoria(categoria, productos, inventario)

            input("\nPresione ENTER para continuar...")
#de aqui yo no se que estoy haciendo, toco improbisar sobre la marcha
        elif opcion == 2:

            while True:

                try:

                    precio_min = int(input("Precio mínimo: "))
                    break

                except ValueError:

                    print("Debe ingresar un número entero.")

            while True:

                try:

                    precio_max = int(input("Precio máximo: "))
                    break

                except ValueError:

                    print("Debe ingresar un número entero.")

            modulo.buscar_precio(precio_min,
                                 precio_max,
                                 productos,
                                 inventario)

            input("\nPresione ENTER para continuar...")
#improbisar, las pelotas, 2 horas estube
        elif opcion == 3:

            while True:

                codigo = input("Ingrese código: ").upper()

                if modulo.buscar_codigo(codigo, productos):

                    while True:

                        try:

                            nuevo_precio = int(input("Nuevo precio: "))

                            if modulo.validar_precio(nuevo_precio):

                                modulo.actualizar_precio(codigo,
                                                         nuevo_precio,
                                                         productos)

                                print("Precio actualizado correctamente.")
                                break

                            else:

                                print("Precio inválido.")

                        except ValueError:

                            print("Debe ingresar un número entero.")

                    break

                else:

                    print("Código inexistente.")

                continuar = input("¿Desea intentar nuevamente? (S/N): ").lower()

                if continuar != "s":
                    break

            input("\nPresione ENTER para continuar...")

        elif opcion == 4:

            while True:

                codigo = input("Código: ").upper()

                if modulo.validar_codigo(codigo, productos):
                    break

                print("Código inválido o existente.")

            while True:

                nombre = input("Nombre: ")

                if modulo.validar_nombre(nombre):
                    break

                print("Nombre inválido.")

            while True:

                categoria = input("Categoría: ")

                if modulo.validar_categoria(categoria):
                    break

                print("Categoría inválida.")

            while True:

                try:

                    precio = int(input("Precio: "))

                    if modulo.validar_precio(precio):
                        break

                    print("Precio inválido.")

                except ValueError:

                    print("Debe ingresar un número entero.")

            while True:

                disponible = input("Disponible (S/N): ")

                if modulo.validar_disponible(disponible):

                    disponible = disponible.lower() == "s"
                    break

                print("Debe ingresar S o N.")

            while True:

                try:

                    stock = int(input("Stock: "))

                    if modulo.validar_stock(stock):
                        break

                    print("Stock inválido.")

                except ValueError:

                    print("Debe ingresar un número entero.")

            while True:

                try:

                    vendidos = int(input("Vendidos: "))

                    if modulo.validar_vendidos(vendidos):
                        break

                    print("Cantidad inválida.")

                except ValueError:

                    print("Debe ingresar un número entero.")

            modulo.agregar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponible,
                stock,
                vendidos,
                productos,
                inventario
            )

            print("Producto agregado correctamente.")

            input("\nPresione ENTER para continuar...")

        elif opcion == 5:

            codigo = input("Ingrese el código a eliminar: ").upper()

            if modulo.eliminar_producto(codigo,
                                        productos,
                                        inventario):

                print("Producto eliminado correctamente.")

            else:

                print("Código inexistente.")

            input("\nPresione ENTER para continuar...")

        elif opcion == 6:

            modulo.mostrar_productos(productos,
                                     inventario)

            input("\nPresione ENTER para volver al menú...")

        elif opcion == 7:

            print("Programa finalizado.")
            break


if __name__ == "__main__":

    main()

    #SON LAS 4 DE LA MAÑANA PORFAVOR FUNCIONAAAAAAAAAAAAAAAAAAAAAAAAAA

    #Profe una disculpa por el lenguaje no sabia que se veria el commit