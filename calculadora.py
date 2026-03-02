#Function 
def sumar(a,b) :
    resultado= a + b
    return resultado
#Funcion para dividir dos numeros
def dividir(a,b):
    if b== 0 :
        raise ValueError("You cannot divide by zero")
    return a / b

