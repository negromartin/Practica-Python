diccionario = {'a':True,'s':100,'q':False,'r':"hola negro",'e':"ñere"}

diccionario['c'] = "IIIEIEIE"
diccionario['a']=False

valor = diccionario.get('a',(1,2))

print(valor)
print("")
print(diccionario)
print("")

llaves = tuple(diccionario.keys())
valor = tuple(diccionario.values())

diccionario2 = {'z':10,'x':3,'h':"saapee"}

diccionario.update(diccionario2)

print(diccionario)
