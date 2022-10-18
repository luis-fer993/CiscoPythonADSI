import json


def writefile(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
    except:
        print("Error al escribir el archivo")

def nuevoProducto():
    data=dict()
    for i in range(int(input('Cuantos productos desea ingresar? '))):
        print('Producto ',i+1) 
            data['id']=input("Ingrese el id del producto: ")    

            data["nombre"]=input('Nombre del producto {} :'.format(i+1))
            data["precio"]=input("Precio del producto {} :".format(i+1))
            data["cantidad"]=input("Cantidad del producto {} : ".format(i+1))
            print('\n')     
    writefile("data.json",str(json.dumps(data) ))
    print("Archivo creado con exito")
    
    
nuevoProducto()

