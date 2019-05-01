import While2 as f
vectores = {}

def ingresar_vector():
    """

    """
    vector = [input('¿Cual es el nombre de su vector?')]

    while True:
        num = input('Ingrese su escalar p "s" para terminar')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, 'no es un escalar')
        else:
            break
    return vector

def mostrar_vectores():
    for nombre in vectores:
        print(nombre, 'contiene', vectores[nombre])

def op_producto_escalar():
    while True:
        # variable =input('Realizaremos producto escalar, quiere continuar? '
        #                 '\n s para continuar '
        #                 '\n n para salir ')
        # if variable == 'n':
        #     break
        # if variable == 's':
        escalar =input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
        except:
            print(escalar, 'no es un escalar')

        seleccion = input('Cual es el nombre del vector con el cual quiere trabajar: ')
        mostrar_vectores()
        print('\n El producto escalar es: ', f.producto_escalar(escalar, vectores[seleccion]))
        break

        # else:
        #     break


def principal():

    Mensaje = '''\n \n Selecciones una ocpion:
    0. Salir
    1. Ingresar vector
    2. Mostrar Vectores
    3, Producto escalar
    '''

    while True:
        opcion = input(Mensaje)

        if opcion == '0':
            print('Gracias')
            break
        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]
            print('Su vector', vector[0], 'es', vectores[vector[0]])
        elif opcion == '2':
            mostrar_vectores()
        elif opcion == '3':
            op_producto_escalar()
        else:
            print("Seleccione una opcion valida")

if __name__ == '__main__':
    principal()