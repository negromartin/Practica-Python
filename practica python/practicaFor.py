lista =[1,2,3,4,5,6,7,8,9,10,11]

for valor in lista:
	print(valor)

	print("")
	range(0,20,2)

for valor in range(0,20,2):
	print(valor)

indice = 0

for valor in lista:
	print(valor," Tiene indice: ", indice)
	indice += 1

for indice,valor in enumerate(lista):
	print(valor," Tiene indice: ",indice)


for valor in range(0, len(lista)):
	print(valor)

for valor in 'Hola Negro':
	print(valor)

diccionario = {'Negro':10,'Ñere':20,'Nae':30,'PeladoHomo':500}

for llave,valor in 	diccionario.items():
	print("La llave: ",llave," Tiene un valor: ",valor)	


