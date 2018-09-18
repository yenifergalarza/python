#objetos
from objetos.persona import persona
#capeta objetos hay un archivo perosna y dentro hay 


#a esto se le llama instanciar 
juan = persona("juan",10)
#aqui puedes poner la cantidad de argumentos que definistes (parametros)al inicio si son 3 p deben ser 3 pero al parametro puedes setearlo con 0 
juan.caminar()
print juan.Energia
juan.caminar()
juan.caminar()
print juan.Energia 
juan.tomarbebidaenergizante()
print juan.Energia
juan.tomarbebidaenergizante(5)
print juan.Energia
#a los metodos podemmos pasarle parametros