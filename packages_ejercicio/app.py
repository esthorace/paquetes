from clientes.busqueda import buscar_cliente


def main():
    nombre = input("Ingrese el nombre del cliente: ")
    cliente = buscar_cliente(nombre)
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente no encontrado")


main()
