try:
	print(2/0)
except ZeroDivisionError as er: #Error en division por el cero
	print(er)
	print("No es posible dividir por cero")
	#Aca puden ejecutarse funciones o clases.
print("Se termino el primer try")	


try:	#Se pueden agregar todos los except q se necesiten
	lista=[1,2]
	print(lista[9])
except IndexError as er:# Este error es por el indice de la lista
	print("El error es:",er)
	print("No es posible obtener el valor en 9 de la lista")

print("Se termino el segundo try")


try:
	lista=[1,2,3,4]
	print(lista[9])
except Exception as er:#Esta es una excepcion general
	print("El error es:",er)
	print("No se sabe q paso, Exception general")
finally:#Siempre se ejecuta
	print("Se termino el tercer try")		