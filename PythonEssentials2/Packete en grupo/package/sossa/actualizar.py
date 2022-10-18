import json
def udpatefile(filename, content):
    try:
        with open(filename, "a") as f:
            f.write(content)
    except:
        print("Error al escribir el archivo")


def actaulizarProducto(filename):
    palabra=input("Ingrese el nombre del producto a actualizar: ")
    with open(filename, "r")as f:
        data = json.load(f)
        if palabra in data['name']:
            data['name']=input("Ingrese el nuevo nombre del producto: ")
            data['price']=input("Ingrese el nuevo precio del producto: ")
            data['quantity']=input("Ingrese la nueva cantidad del producto: ")
            udpatefile(filename,)
        

    


udpatefile("data.json", "Hola mundo")