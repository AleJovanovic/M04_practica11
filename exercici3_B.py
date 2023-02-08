
#funcion que te dice si has de hacer declaracion a hacienda introduciendo edad y sueldo 
def dHacienda():
    edad = int(input("Pon tu edad: "))
    ingresos = int(input("Pon tus ingresos: "))

    if(edad>=18 and ingresos>1200):
        print('Tu que tens {} i ganes {}, és necessari que facis la declaració d’hisenda'.format(edad,ingresos))
    else:
         print('Tu que tens {} i ganes {}, encara no pots fer la declaració'.format(edad,ingresos))

dHacienda()
