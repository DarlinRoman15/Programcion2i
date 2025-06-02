# Función para multiplicar dos números
def multiplicar(x, y):
    resultado = x * y
    return resultado
print(f"La multiplicacion es:" ,multiplicar(3, 4)) 


num1 = float(input("Ingrese un numero"))
num2 = float(input("Ingrese otro numero"))
producto = multiplicar(num1,num2)

print(f"La multiplicacion es:", multiplicar)
# Función para verificar si un número es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
print(es_par(6))  
print(es_par(7))  

# Función para presentarse
def presentarse(nombre, edad):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
presentarse("Darlin", 21)

