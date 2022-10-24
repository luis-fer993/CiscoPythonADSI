
from sys import path
import os, platform

#path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\Packete en grupo\\package')
path.append(path[0]+'/package')
from luis.operations import moduloDiv, exponenciacion, mult, suma, rest
from eduard.moduloEduard import hypotenusa, fac, cei
from juan.ejercicio import radio, gcd
from jimmy.Jimmy import sin,porcentaje
from cristian.tangente import cosen_o, tan_0

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    clear()
    print('''
    --- MODULOS Y PAQUETES EN PYTHON ---
            
            --- Luis Fernando Ch.  ---

        Eliga una opcion: 
    ''')
    while True:
        print('''
        ------------------------------
        1. Residuo de divicion
        2. Exponenciacion
        3. Multiplicacion
        4. Suma
        5. Resta
        6. Radio
        7. Gcd
        8. Porcentaje
        9. Hipotenusa
        10.Factorial
        11.Ceil
        12.Seno
        13.Coseno
        14.Tangente
    ''')
        try:
            opcion=int(input('Eliga una opcion:  '))
            if opcion == 1:
                clear()
                moduloDiv()
            elif opcion == 2:
                clear()
                exponenciacion()
            elif opcion == 3:
                clear()
                mult()
            elif opcion == 4:
                clear()
                suma()
            elif opcion == 5:
                clear()
                rest()
            elif opcion == 6:
                clear()
                radio()
            elif opcion == 7:
                clear()
                gcd()
            elif opcion == 8:
                clear()
                porcentaje()
            elif opcion == 9:
                clear()
                print(hypotenusa())
            elif opcion == 10:
                clear()
                print(fac())
            elif opcion == 11:
                clear()
                print(cei())
            elif opcion == 12:
                sin()
            elif opcion == 13:
                clear()
                cosen_o()
            elif opcion == 14:
                clear()
                tan_0()
            else:
                print('Opción no válida')
        except:
            print('Opción no válida')
        finally:
            opc = input('Desea continuar? (s/n): ')
            if opc == 's':
                clear()
            else:
                clear()
                print('BYE')
                break


