""" demanarà que insereixin un nom dels 5 que es proposin. 
Depenent del nom que indiqui s’hi mostrarà, per consola, 
un missatge diferent."""

def nombres():

    MyList = ['Marta', 'Maria', 'Sofia', 'Manuel', 'Andreu']

    print("Inserta un nombre de la lista {llista}".format(llista = MyList))
    nombre = input()

    if (nombre == 'Marta'):
        print("El nombre se encuentra en la lista, en la posicion {posicio}".format(posicio = MyList.index('Marta')))

    elif (nombre == 'Maria'):
        print("El nombre se encuentra en la lista, en la posicion  {posicio}".format(posicio = MyList.index('Maria')))

    elif (nombre == 'Sofia'):
        print("El nombre se encuentra en la lista, en la posicion  {posicio}".format(posicio = MyList.index('Sofia')))

    elif (nombre == 'Manuel'):
        print("El nombre se encuentra en la lista, en la posicion  {posicio}".format(posicio = MyList.index('Manuel')))

    elif (nombre == 'Andreu'):
        print("El nombre se encuentra en la lista, en la posicion  {posicio}".format(posicio = MyList.index('Andreu')))

    else:
        print("El nombre no se encuentra en la lista.")