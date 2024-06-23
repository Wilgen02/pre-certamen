def estado_de_salud(nombre_archivo):
    arch = open(nombre_archivo)
    for linea in arch:
        lista = linea.strip().split(";")
        tipo = lista[0]
        ejercicio = lista[1]