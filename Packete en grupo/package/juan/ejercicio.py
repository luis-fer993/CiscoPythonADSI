import math
def gcd():
    a=int(input("Introduzca su primer número:"))
    b=int(input("Introduzca su segundo número:"))
    print("El máximo común divisor de los dos números es:",math.gcd(a,b))


def radio():
    radio = float(input("Escribe el radio del circulo: "))
    area=math.pi*radio**2
    print("El area del circulo es:",area)
