ingredientes = ['']

while ingredientes:
    pizza = input("Ingrese los ingredientes de su pizza")
    ingredientes.append(pizza)

    if pizza == 'pare':
        break



print("Su pizza contiene los siguientes ingredientes", ingredientes)