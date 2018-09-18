capital = raw_input("ingrese tu capital :")
tiempoEA = raw_input("ingrese el tiempo en anos : ")
tasaAnual = raw_input("ingrese la tasa de interes anual : ")
capital= int(capital)
tasaAnual = (float(tasaAnual)/100)
tiempoEA = int(tiempoEA)

interes = (capital* tiempoEA *tasaAnual)

print interes