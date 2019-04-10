while True:
    numero = input("Ingrese un dato")
    print(numero)

    if numero.isnumeric() and int(numero) % 2 != 0:
        break
