#Lista Comprehension

#Crear una lista en una sola linea

lista = [valor for valor in range(0,101) if valor % 2 == 0]


print(lista)
#Crear una tupla en una sola linea

tupla =tuple((valor for valor in range(0,101) if valor % 2 == 0))

print(tupla)

#Crear un diccionario en una sola linea

diccionario ={ indice:valor for indice, valor in enumerate(lista)}

print(diccionario)


#No es obligatorio los condicionales.. 
#es solo para q cree la lista segun ese criterio