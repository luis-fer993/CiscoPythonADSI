from sys import path
import os, platform

#path.append('C:\\Users\\Aprendiz\\Documents\\CiscoPythonADSI\\PythonEssentials2\\Packete en grupo\\package')
path.append(path[0]+'/package')
from luis.operations import moduloDiv, exponenciacion, mult, suma, rest
#from eduard. import hipotenusa, factorial, ceil
#from jimmy. import seno, coseno, tangente

if platform.system() == "Windows":
    def clear():
        os.system('cls')
else:   
    def clear():
        os.system('clear')

def main():
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
        2. exponenciacion
        3. multiplicacion
        4. suma
        5. resta
        6. seno
        7. coseno
        8. tangente
        9. Hipotenusa
        10.Factorial
        11.Ceil
        12.
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
                seno()
            elif opcion == 7:
                clear()
                coseno()
            elif opcion == 8:
                clear()
                tangente()
            elif opcion == 9:
                clear()
                hipotenusa()
            elif opcion == 10:
                clear()
                factorial()
            elif opcion == 11:
                clear()
                ceil()
            elif opcion == 12:
                pass
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



if __name__ == "__main__":
    main()




