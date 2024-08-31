
# Esta linea es de comentarios 
"""
Comentarios de texto largo 
no es necesario usar gato en cada linea para comentar

Ahora estamos programando una calculadora.
"""
def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

while True:
    print("Bienvenido a la calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    eleccion = int(input("elija una opción: "))
    

    if eleccion == 5:
        print("Saliendo de la calculadora...")
        break

    if eleccion < 1 or eleccion > 5:
        print("Opción no válida, por favor elija una opción entre 1 y 5.")
        continue
    
    num1 = int(input("Ingrese el primer número: ")) 
    num2 = int(input("Ingrese el segundo número: "))
    
    if eleccion == 1:
        print(num1, "+",num2, "=", sumar(num1,num2))

    elif eleccion == 2:
        print(num1, "-",num2, "=", restar(num1,num2))   

    elif eleccion == 3:
        print(num1, "*",num2, "=", multiplicar(num1,num2))

    elif eleccion == 4:
        print(num1, "/",num2, "=", dividir(num1,num2))