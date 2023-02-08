
#funcion que te dice si el numero introducido por un usuario es par o impar 
def ParelloSenar():
    num = int(input("ponn num:"))

    if((num%2)==0):
        print('El numero {} es parell'.format(num))
      
    else:
         print('El numero {} es senar'.format(num))

ParelloSenar()