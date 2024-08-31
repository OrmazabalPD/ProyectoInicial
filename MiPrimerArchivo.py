
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

print("Bienvenido a la calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

eleccion = int(input("elija una opción: "))
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

else:
    print("Opción no válida")
 # dfasasdfads
 