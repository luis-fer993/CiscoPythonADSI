from math import hypot, ceil, factorial 
def hypotenusa():
    print("Hallar la hipotenusa")
    x = float(input("ingresa el primer numero: "))
    y = float(input("ingresa el segundo numero: "))
    return 'La hypotenusa es: {}'.format(hypot(x,y))


def cei():
    print("Hallar el redondeo")
    x = float(input("ingresa un numero: "))
    return "El redondeo del numero es: {}".format(ceil(x))


def fac():
    print("Hallar el factorial")
    x = int(input("ingresa un numero: "))
    return "El factorial es: {} ".format(factorial(x))