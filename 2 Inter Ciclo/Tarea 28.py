with open("mbox.txt", "w") as f:
    lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
    f.writelines(lineas)