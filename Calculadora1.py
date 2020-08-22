print("CALCULADORA")

def Suma(n1, n2):
    result= n1 + n2
    print("El resultado de la Suma es: "+ str(result))

#RESTA
def Resta(n1, n2):
    result= n1 - n2
    print("El resultado de la Resta es: "+ str(result))

#MULTIPLICACION
def Multiplicacion(n1, n2):
    result= n1 * n2
    print("El resultado de la Multiplicacion es: "+ str(result))

#DIVISION
def Division(n1, n2):
    if n2>0:
       result= n1 / n2
       print("El resultado de la Division es: "+ str(result))
    else:
        print("Ningun numero es divisible entre cero ")
    

#MENU
def OperacionesM():
    opcion= int(input("Elegir la operacion: \n 1)Sumar \n 2)Restar \n 3)Multimplicar \n 4)Dividir \n 5)Salir: " ))
    while opcion==1 or opcion==2 or opcion==3 or opcion==4:
        n1=int(input("Ingresar primer numero: "))
        n2=int(input("Ingresar segundo numero: "))
        if opcion==1:
           v= Suma(n1,n2)
        if opcion==2:
           v = Resta(n1,n2)
        if opcion==3:
           v= Multiplicacion(n1,n2)
        if opcion==4:
           v = Division(n1,n2)
        if opcion==5:
            break
        opcion= int(input("Elegir la operacion: \n 1)Sumar \n 2)Restar \n 3)Multimplicar \n 4)Dividir \n 5)Salir: " ))
calcular=OperacionesM();