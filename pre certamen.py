def promedioIMC_por_estado_de_salud(nombre_archivo, estado_salud):
    
    archivo = open(nombre_archivo)
    d= {}#diccionario vacio
    for linea in archivo: #recorro el archivo
        lista = linea.strip().split(";")#tranformo cada linea en una lista y quito los espacio en blaco 
        es = lista[0]
        chequeo = lista[1]
        imc = float(lista[9])
        if es == estado_salud:# si estado es igual al segundo parametro que en este caso es EXCELLENT
            if chequeo not in d: #si chequeo no esta en el diccionario 
                d[chequeo] = [] #estoy creando una llave con el d[chequeo] una lista vacia como valor
            d[chequeo].append(imc)#estoy agregando a la lista el imc 
    
    
    #print(d)
    lista1 = []
    for i in d:#al recorrer un diccionario con un ciclo solo la guarda solo la llave
        
        
        prom_imc = round((sum(d[i])/len(d[i])),2)#d[cheque] me refiero al volor de la llave
        lista1.append([i,prom_imc])
    lista1.sort() 
    print(len(lista1))
                
    salida = open(estado_salud+"IMC.txt", "w")   

    dsalida = "{}: {}\n" 
    psalida = "{}:{}\n"
    for i, prom_imc in lista1:
        salida.write(dsalida.format(chequeo,imc)) 
        salida.write(psalida.format(chequeo,prom_imc))
print(promedioIMC_por_estado_de_salud("datos.csv","Excellent"))


