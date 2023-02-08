
#funcion que te dice cual es el mayor y menor de dos numeros introducidos por el usuario
def mesGran():
    num1 = int(input("Pon el numero 1"))
    num2 = int(input("Pon el numero 2"))
   
    
    if(num1<num2):
        print('El mas grande es {} y el mas pequeño es {}'.format(num2,num1))
       
        
    elif(num1>num2): 
        print('El mas grande es {} y el mas pequeño es {} '.format(num1,num2))
    
       
  


mesGran()