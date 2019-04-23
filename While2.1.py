import While2 as f
import suma_vectores as s
import Producto_punto as p
import mayor_elemento as e
import menor_elemento as c
vectores = {}

def ingresar_vector():
    """

    """
    vector = [input('¿Cual es el nombre de su vector?')]

    while True:
        num = input('Ingrese su vector o "s" para terminar')
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
        escalar = input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
        except:
            print(escalar, 'no es un escalar')
            break

        seleccion = input('Cual es el nombre del vector con el cual quiere trabajar: ')
        mostrar_vectores()
        print('\n El producto escalar es: ', f.producto_escalar(escalar, vectores[seleccion]))
        break

def suma_vectores():

    vector = [input('Ingrese el nombre del vector a sumar')]

    while True:
        num = input('Ingrese su vector o "s" para terminar')

        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print("No es un vector")
        else:
            break

        seleccion = input('Cual es el nombre del vector con el cual quiere trabajar: ')
        mostrar_vectores()
        print('\n La suma de los vectores es', s.s_vectores(vector, [seleccion]))

def producto_punto():

    vector = [input('Ingrese el vector para realizar el producto punto')]

    while True:
        num = input('Ingrese el vector para realizar el producto punto o "s" para terminar')

        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print("No es un vector")
        else:
            break

        seleccion = input('Cual es el nombre del vector con el cual quiere trabajar: ')
        mostrar_vectores()
        print('\n El producto punto de los vectores es', p.producto_punto(vector, [seleccion]))

def mayor_element(vector):

    mayor = max(vector)

    while True:
        for i in range(len(vector)):
            print('El numero mayor del vector es', e.mayor_elemento(mayor))

    #for mayor in vector:
     #   print('El numero mayor del vector es', vector[mayor])

def menor_elemento(vector):
    for menor in vector:
        print('El numero menor del vector es', vector[menor])



def principal():

    Mensaje = '''\n \n Selecciones una ocpion:
    0. Salir
    1. Ingresar vector
    2. Mostrar Vectores
    3. Producto escalar
    4. Sumar vectores
    5. Producto punto
    6. Mayor elemento
    7. Menor elemento
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
        elif opcion == '4':
            suma_vectores()
        elif opcion == '5':
            producto_punto()
        elif opcion == '6':
            mayor_element()
        elif opcion == '7':
            menor_elemento()
        else:
            print("Seleccione una opcion valida")

if __name__ == '__main__':
    principal()