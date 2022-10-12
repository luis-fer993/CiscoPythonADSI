
#opraciones 
#modulo de divicion
#exponeciacion 
#op, basicas


def moduloDiv():
    print('\nResiduo de divicion\n')
    val1=int(input('ingrese el valor 1 ->  '))
    val2=int(input('ingrese el valor 2 ->  '))
    print( 'El residuo de la division {} / {} es {}'.format(val1, val2,val1 % val2 )) 

def exponenciacion():
    print('\nExponeciacion\n')
    val1=int(input('ingrese el valor 1 ->  '))
    val2=int(input('ingrese el valor 2 ->  '))
    print( 'la exponenciacion de {}^{} es {}'.format(val1, val2,val1 ** val2 )) 

def mult():
    print('\nMultiplicacion\n')
    cant=int(input('Cuantos valores va a multiplicar:  '))
    total=1
    if cant != 0 or None : 
        for i in range(cant):  
            total=total*float(input('ingrese el valor {}:  '.format(i+1)))
        print('El total de la multiplicacion es: ',round(total,0))
    else:
        print('ningun valor ingresado') 

def suma():
    print('\nSuma\n')
    cant=int(input('Cuantos valores va a sumar:  '))
    if cant != 0 or None : 
        total=[]
        for i in range(cant):  
            total.append(float(input('ingrese el valor {}:  '.format(i+1))))
        print('El total de la suma es: ',round(sum(total),1))
    else:
        print('ningun valor ingresado') 
            
def rest():
    print('\nResta\n')
    cant=int(input('Cuantos valores va a restar:  '))
    list=[]
    if cant != 0 or None : 
        for i in range(cant):  
            list.append(float(input('ingrese el valor {}:  '.format(i+1))))
        print('El total de la resta es: ',round(list[0]-sum(list[1:]),1))
    else:
        print('ningun valor ingresado')
