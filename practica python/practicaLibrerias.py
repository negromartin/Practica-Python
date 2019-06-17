import random
import sys
import datetime
import time

for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("TU HERMANA ")
	sys.stdout.flush()

for i in range(100)	
	time.sleep(0.3)
	sys.stdout.write("\r%d %%" %i)
	sys.stdout.flush()

print(datetime.datetime.now())

valor = random.randint(0,10) #Selecciona aleatoriamente entre 1 y 10
lista = [True,"Tu hermana",23,False]
valor2 = random.choices(lista)#Elije algun elemento de la lista
valor3 = random.shuffle(lista)# desordena la lista
print(valor)
print(valor2)

