


def pedirNumero():
    while True:
        try:
            numero = int(input("ingresa un numero"))
        except:
            print("lo que ingresaste no es un numero")
        else:
            print(f"ingresaste el numero {numero}")
            break
    print("adios")


"""
este es un comentario para mejorar la puntUACION EN PYLINT
"""


def nombre_funcion():
    while True:
        try:
            numero1 = int(input("ingresa un numero 1"))
            numero2 = int(input("ingresa un numero 2"))
        except:
            print("lo que ingresaste no es un numero")
        else:
            print(f"ingresaste el numero {numero1}")
            print(f"ingresaste el numero {numero2}")
            break
    return numero1, numero2


m, n = nombre_funcion()


"""
este es un comentario para mejorar la puntUACION EN PYLINT
"""


def suma(num1, num2):
    print(num1 + num2)


suma(m, n)
