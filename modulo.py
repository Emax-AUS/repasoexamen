def leer_opcion():

    while True:

        try:

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 7:
                return opcion

            print("Debe seleccionar una opción válida")

        except:
            print("Debe ingresar un número.")

    def stock_categoria(categoria, productos, inventario):

        total = 0

    for codigo in productos:

        if productos[codigo][1].lower() == categoria.lower():

            total += inventario[codigo][0]

    print("Stock total:", total)