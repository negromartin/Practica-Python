def generador(*args):
	""" Esta funcion recibe n cantidad de numeros y regresa elevado al cubo,
		junto con un string"""	
	for valor in args:
		yield valor **3, "Ñereee"

for valor1,valor2 in generador(7,4,6,11,23,87):
	print (valor1,valor2)		

nombre = generador.__name__ 		#Estos es acceder a los atributos de la clase generador
documentacion = generador.__doc__	#En python las funciones son clases
print(nombre,": ")
print(documentacion)
