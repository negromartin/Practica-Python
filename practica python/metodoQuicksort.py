def sort(lista):
	izquierda = []
	centro = []
	derecha=[]

	if len(lista)>1:
		pivote = lista[0]
		for i in lista:
			if i < pivote:
				izquierda.append(i)
			elif i == pivote:
				centro.append(i)
			elif i > pivote:
				derecha.append(i)
		print(izquierda+["-"]+centro+["-"]+derecha)
		return sort(izquierda)+centro+sort(derecha)
	else: 
		return lista					



milista=[23,44,566,77,88,99,0,22,4,3,2,34,66,200,50,1,45,1001,1002,3030]

print(milista)
print(sort(milista))