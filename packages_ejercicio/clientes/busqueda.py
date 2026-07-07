from clientes.datos import base_datos


def buscar_cliente(nombre):
    for cliente in base_datos["clientes"]:
        if cliente["Nombre"].lower() == nombre.lower():
            return cliente["Nombre"]
    return None
