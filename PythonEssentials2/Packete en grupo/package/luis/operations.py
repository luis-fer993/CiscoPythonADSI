
#opraciones 
#modulo de divicion
#exponeciacion 
#op, basicas


def moduloDiv():
    val1=int(input('ingrese el valor 1 ->  '))
    val2=int(input('ingrese el valor 2 ->  '))
    print( 'El residuo de la division {} / {} es {}'.format(val1, val2,val1 % val2 )) 

def exponenciacion():
    val1=int(input('ingrese el valor 1 ->  '))
    val2=int(input('ingrese el valor 2 ->  '))
    print( 'El residuo de la division {} / {} es {}'.format(val1, val2,val1 ** val2 )) 

def mult():
    cant=int(input('Cuantos valores va a multiplicar:'))
    total=0
    val=[]
    if cant != 0 or None : 
        for i in range(cant):  
            val.append(int(input('ingrese el valor {}:  '.format(i+1))))
        
        for i in range(len(val)):
            total3 = total * val[i]
        print('El total de la multiplicacion es: ',total3)
    else:
        print('ningun valor ingresado') 
            

