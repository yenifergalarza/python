Deportistas = [
{"id":1,"name" : "Usain Bolt","edad" : 34 ,"talla" : 1.98, "peso" : 110},
{"id":2,"name" : "Juan","edad" : 15,"talla" : 1.58,"peso" : 60},
{"id":3,"name" : "Lorena","edad" : 25 ,"talla" : 1.67 ,"peso" : 70},
{"id":4,"name" : "Roberto","edad" : 27,"talla" : 1.78,"peso" : 120},
{"id":5,"name" : "Maria","edad" : 32,"talla" : 1.70,"peso" : 80}
]

for deportista in Deportistas:
    peso = deportista[ 'peso' ]
    talla = deportista[ 'talla' ]
    edad = deportista[ 'edad' ]

    limiteAptoEdad= (edad >= 18 and edad <= 35)

    limiteAptoPeso = (peso >= 100 and peso <= 120)

    limiteInfantil = (edad < 18 )

    limiteNoApto= not (peso < 100 or talla > 1.60)

    print deportista["name"]

    if (limiteAptoEdad and limiteAptoPeso):
        deportista["apto"] = True
        print"deportista profesional"

    elif(limiteInfantil):

        deportista["infantil"] = True
        print "Infantil"

    elif(limiteNoApto) :
        deportista["apto"] = False
        print "deportista no apto"
    else :
        print "sin tipo"