#el compilado vuelve tu codigo a unos y ceros
#el lenguaje interpretado es multiplataforma
"""
Nombre=raw_input("cual es tu nombre\n")
print "hola",Nombre

"""
#formas de comentar codigo :)

""" o #
datos basicos
a =12
b=15
res=a+b

print type(a) 

a="12"
print type(a) 
a=True
print type(a) 

"""
"""
tipo de colecciones 

listas => son arrays => agergar valores ,cambiar valores, eliminar,buscar 
tuplas => son arrays no editables
Diccionario => 

"""
#colecciones 
l1=[1,3,4,5,5,6]
print type (l1)
print l1

l1.append(42)
print l1[2],l1[5]
print l1[2]
#como obtener sub arreglos 
print l1[2:4]
print l1[:4]
print"cantidad de elementos :",len(l1)

l1.append(True)
l1.append("emprende up")
l1.append([4,5,12,"hola",True,156,False])
print l1[8][3]

"""tuplas no editables"""
t=(1,3,4)
#t[2]=10
print t
"""lista si se puede editar """
empleados =[(1,"juan"),(2,"daniel"),(3,"gabriela")]
empleados.append((4,"paola"))
print type(empleados)
print type (empleados[1])
##append es para agregar datos dentro de la colecciones

#dicionarios
# no se busca u obtiene valor mediate indices sino mediante keys 
#puedo sobre escribir los valores, pero las keys nunca
#{'key ':'value'} 

#podemos definir las colecciones 
""" dic ={} o dic=dic()
list=[] o list =list()
tuple=()   sin embaargo para las tuplas no tiene sentido hacer eso """

Dic1={"msg1":"mensaje1","msg2":"mensaje2","msg3":"mensaje3"}
print Dic1
print type(Dic1)
Dic1["mensaje2"]="otro mensaje"

print Dic1
print type(Dic1)
#para traer todas esas llaves en  una lista 
print Dic1.keys()
print Dic1.values()
#lista de alumnos =[{},{},{}]
Alumnos = [{
            "name":"Daniel",
            "email":"dan123@gmail.com",
            "dni":"1234567",
            "id":1,		
            },

            {
            "name":"juan",
            "email":"juan123@gmail.com",
            "dni":"12322567",
            "id":2,		
            }, 

            {
            "name":"Daniela",
            "email":"danna123@gmail.com",
            "dni":"12123456734567",
            "id":3,		
            }]

juan = Alumnos[1]
print juan 
print juan ["email"]           
#para obtener el dni de daniela 
print Alumnos[2]["dni"]
#nunca olvides que python siempre diferencia mayusculas y minuscublas

a = raw_input("valor a: ")
b = raw_input("valor b: ")
if a>b:
	print"a es mayor que b"
else :
	print "a es menor o igual que b"
print "fin"
"""
= asignnacion 
== comparacion 
!= diferente
<=
=>
<
>
or : disyuncion debe haber por lo menos un verdadero
and : ambas tienen que ser verdaderas
not :Negacion
#estructura condicional simple
p=True
q=False
print p or q #true
print p and q#false
print not ( p and q)#true
 
 
peso= raw_input("ingrese el peso :")
talla = raw_input("ingrese la talla : ")
edad= raw_input("ingrese la edad : ")

peso = int(peso)
talla = float(talla)
edad = int(edad)

condicion_peso = (peso>=75 and peso <=85)
print "condicion peso",condicion_peso
condicion_talla =(talla>=1.75 and talla<=1.85)
 
condicion_edad = not (edad < 18 or edad > 65)

if (condicion_peso and condicion_talla and condicion_edad):
 		print"deportista apto"
elif condicion_talla or condicion_edad :
	print "talla o edad"
elif  condicion_peso and condicion_talla :
	print "peso o talla"
elif  condicion_peso:
	print "solo peso"
else:
 		print"deportista no apto"

#estructura iterativa
deportistas = [
{"id":1,"name":"usain bolt","edad":34,"talla":1.98, "peso":110},
{"id":2,"name":"juan","edad":15,"talla":1.58, "peso":60},
{"id":3,"name":"lorena","edad":25,"talla":1.67, "peso":70},
{"id":4,"name":"roberto","edad":27,"talla":1.78, "peso":120},
{"id":5,"name":"maria","edad":32,"talla":1.70, "peso":80}
 ]

for deportista in deportistas:
		peso =deportista["peso"]
		talla = deportista ["talla"]
		edad = deportista["edad"]


		condicion_peso = (peso>=75 and peso <=85)
		
		condicion_talla =(talla>=1.75 and talla<=1.85)
		 
		condicion_edad = not (edad < 18 or edad > 65)

		
		print deportista["name"]

		if (condicion_peso and condicion_talla and condicion_edad):
				deportista["apto"]= True
		 		print"deportista apto"
		else:
				deportista["apto"]= False		 		
		 		print"deportista no apto"
"""
X =[1,2,3,4,5]
X = [x**2 for x in X]

print X

