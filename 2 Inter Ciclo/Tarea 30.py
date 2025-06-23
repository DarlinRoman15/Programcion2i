with open("mbox.txt", "r") as origen, open("copia.txt", "w") as copia:
    copia.write(origen.read())