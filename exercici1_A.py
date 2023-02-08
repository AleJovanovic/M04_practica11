"""demana a l’usuari que inserti 2 números i el programa li dirà quin és 
el més gran i quin el més petit. Si son iguals sortirà que son iguals."""


def numMayor ():

    num1 = input()
    num2 = input()

    if(num1 > num2):
        txt = "El numero {numGrande} és més gran que el {numPequeño}"
        print(txt.format(numGrande = num1, numPequeño = num2))

    elif(num2 > num1):
        txt = "El numero {numGrande} és més gran que el {numPequeño}"
        print(txt.format(numGrande = num2, numPequeño = num1))

    else:
        txt = "El numero {numero} i el numero {numeros} son iguals"
        print(txt.format(numero = num1, numeros = num2))

numMayor()