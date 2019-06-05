import time 
import random
def busqBinaria(lista,dato):
	if(len(lista)==0):
		return False
	else:
		puntoMedio = len(lista)//2	
		if (lista[puntoMedio]== dato):
			return True
		elif(dato<lista[puntoMedio]):
			return busqBinaria(lista[:puntoMedio],dato)
		else:
			return busqBinaria(lista[puntoMedio+1:],dato)


lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20,30,44,55,56,57,58,59,70,80,100,1233,40000]

print("Inicia la busqueda birania")
print(busqBinaria(lista1,100))				



def exponenteDV(a,n):
	if(n==1):
		return a
	elif(n%2 == 0):
		return exponenteDV(a,n//2)**2
	else:
		return a*exponenteDV(a,n-1)		

print("Ahora haremos una exponenciacion de un numero con Divide y Venceras")
print(exponenteDV(5,2))		

def generador():
	listaG=[]
	for i in range(0,100000):
		listaG.append(random.randrange(100))
	return listaG


def sort(lista):
	izq=[]
	der=[]
	centro=[]
	if len(lista)>1:
		pivote = lista[0]
		for i in lista:
			if i < pivote:
				izq.append(i)
			elif i == pivote:
				centro.append(i)
			elif i > pivote:
				der.append(i)
			print(izq+["-"]+centro+["-"]+der)	
		return sort(izq)+centro+sort(der)
	else:
		return lista
print("Empieza")
print(time.time())
lista2 = generador()
print("ahora ordenamos una lista con quicksort")
print(sort(lista2))
print("Termina")
print(time.time())							









