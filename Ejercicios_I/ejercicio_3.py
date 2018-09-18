capital = raw_input("ingrese tu capital :")
tiempoEA = raw_input("ingrese el tiempo en anos : ")
tasaAnual = raw_input("ingrese la tasa segun periodo: ")
periodo = raw_input("ingrese el periodo ")

capital= int(capital)
tasaAnual = float(tasaAnual)
tiempoEA = int(tiempoEA)


interesSimpleGeneral = capital * tiempoEA *tasaAnual


if (periodo == "diario"):
    interes = interesSimpleGeneral/(365*100)

elif (periodo == "semanal"):
    interes = interesSimpleGeneral/ (48*100)


elif (periodo == "quincenal"):
    interes = interesSimpleGeneral/ (24*100)

elif (periodo == "mensual"):
    interes = interesSimpleGeneral / (12*100)

elif (periodo == "bimestral"):
    interes = interesSimpleGeneral/ (6*100)

elif (periodo == "trimestral"):
    interes = interesSimpleGeneral/ (4*100)

elif (periodo == "semestral"):
    interes = interesSimpleGeneral / (2*100)
elif (periodo == "anual"):
    interes = interesSimpleGeneral / (1*100)

print interes