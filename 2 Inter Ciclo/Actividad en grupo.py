# Juego del número secreto
print("Bienvenido al juego Descifra el Misterio Numérico para continuar con el juego")
Nombre_del_participante=input("Ingresa su nombre : ")
print(f"Hola {Nombre_del_participante} listo para jugar ")
print("¿Quieres ver las reglas del juego?")
ver_reglas = input("Escribe 'si' para verlas o cualquier otra cosa para continuar: ").lower()
if ver_reglas == "si":
    print("\n REGLAS DEL JUEGO:")
    print("- Adivina el número secreto entre 1 y 100.")
    print("- El sistema te dirá si el número es mayor o menor.")
    print("- Ganas cuando aciertas el número exacto.")
    print("- ¡Suerte!\n")
print("LISTO AHORA QUE SABES LAS REGLAS DE JUEGO EMPREZEMOS")
print("\n")
def juego_numero_secreto():
    numero_secreto = 6
    num = int(input("Adivina el número secreto (entre 1 y 10): "))
    while num != numero_secreto:
        if num < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        num = int(input("Dame un número: "))
    print("¡Felicidades! ¡Ganaste!")
juego_numero_secreto()