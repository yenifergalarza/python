
"""
Nombre=raw_input("cual es tu nombre\n")
print "hola",Nombre

"""
#formas de comentar codigo :)

"""
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
tuplas => 
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

empleados =[(1,"juan"),(2,"daniel"),(3,"gabriela")]
empleados.append((4,"paola"))
print type(empleados)
print type (empleados[1])