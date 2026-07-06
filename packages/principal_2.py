from matematicas.calculo_areas import calcular_area_circulo, calcular_area_rectangulo
from matematicas.operaciones import sumar, restar


def main():
    area_circulo = calcular_area_circulo(5)
    area_rectangulo = calcular_area_rectangulo(4, 6)
    print(f"área círculo: {area_circulo}")
    print(f"área cuadrado: {area_rectangulo}")
    sumar(5, 3)
    restar(0, 10)


main()
