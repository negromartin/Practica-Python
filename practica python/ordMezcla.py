def ordMezcla(lista):
	print("Divide: ",lista)
	if(len(lista)>1):
		mitad = len(lista)//2
		mitadIzq = lista[:mitad]
		mitadDer = lista[mitad:]
		ordMezcla(mitadIzq)
		ordMezcla(mitadDer)
		i=0
		j=0
		k=0

		while i<len(mitadIzq) and j<len(mitadDer):
			if mitadIzq[i]<mitadDer[j]:
				lista[k]=mitadIzq[i]
				i+=1
			else:
				lista[k] = mitadDer[j]
				j+=1
			k+=1			

		while i<len(mitadIzq):
			lista[k]=mitadIzq[i]
			i+=1
			k+=1
		
		while j<len(mitadDer):
			lista[k]=mitadDer[j]
			j+=1
			k+=1
		print("Mezclar:", lista)	


lista=[4555,5777,23,41,5555,10,87,29,30,499,12,45,370,821,72,89,101,500,456,382590,22,999,1001]				
ordMezcla(lista)
print(lista)
