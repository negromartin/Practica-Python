def factorial(numero):
	factorial = 1
	while numero > 0:
		factorial *= numero
		numero -=1
	return factorial
	
def suma1(valor1,valor2,valor3):
	return valor1 + valor2 + valor3			#Se puede devolver un objeto compuesto por la operacion

def division(valor1,valor2):
	return valor1 / valor2

def multiplicacion(valor1,valor2 = 10):				#se puede asignar el valor a la entrada 2 para q sea constante
	return valor1 * valor2

def multiplesValores():
	return "String",1,True,25.6			#devuelve una tupla con esos elementos

def mostrarResultado(funcion):
	print(funcion(3,4))

def palindromo(frase):
	frase = frase.replace(' ','') # frase aca es una Variable Local
	return frase [::-1]

def valorglobal():							#Con estas 2 funciones modificamos 
	global variableglobal					#La variable Global		
	variableglobal = 'Cambiar valor' #Variable Local

def mostrarglobal():
	print(variableglobal)


def crearGlobal():
	global nuevaVariable
	nuevaVariable = 'Esto es una nueva variable global'



def suma2(*args):			#Esta funcion es una Suma de N elementos, toma una Tupla como argumento con el simbolo *
	resultado = 0			# se utiliza cuando no sabes cuantos parametros tendras q utilizar
	for valor in args:
		resultado = resultado + valor
	return resultado

def suma3(**kwargs):			#Esta funcion toma como parametro un diccionario con el simbolo **
	valor = kwargs.get('valor', 'x')
	print(valor)

def divison2(num1,num2):
	def validacion():
		return (num1 > 0 and num2 > 0)

	if validacion():
		return  num1/num2

#Funcion Closure : crea otra funcion
def crearFuncion(num1,num2):
	def validacion():
		print("Se ejecuta validacion")
		return num1 > 0 and num2 >0
	return validacion

def aplicarFuncion(func): # recibe una funcion
	resultado = func() #V o F
	print(resultado)

#Decorador : es una funcion q recibe otra funcion, para dar como salida otra funcion
def decorador(func): #A, B
	def nuevaFuncion():
		#Codigo Antes
		print("vamos a ejecutar la funcion")
		func()
		#Codigo Despues
		print("Se ejecuto la funcion \n")
	return nuevaFuncion #C

@decorador	
def saluda():
	print("Hola ÑEREEEE")

saluda()	


nuevaFuncion = crearFuncion(10,9)
aplicarFuncion(nuevaFuncion)



resultado = divison2(10,0)
print(resultado)

# estas son las funciones lambda
miFuncion = lambda valor1, valor2: valor1 + valor2		#Estas funciones Lambda tienen el formato lambda parameto:sentencia
formato = lambda sentencia: 'BlackPeople'.format(sentencia)
imprimirP = lambda: print('Imprimir por pantalla @Blackpeople')

resultado = miFuncion(2,3)
print('Suma con Funcion lambda: ', resultado)

resultado = formato('asdasd')
print('aca damos un formato al string con una funcion lambda: ',resultado)
resultado = imprimirP()
print('aca imprimimos por pantalla un string con una funcion lambda: ',resultado)



print('Aca hacemos la funcion suma con un diccionario de argumento')
resultado = suma3(valor='Negro',x=2,y=9,z=True)
print(resultado)


print('Aca hacemos una suma de n elementos, sin conocer la cantidad de n\n')
resultado = suma2(1,2,3,4,5,6,7,8,9)
print(resultado)


print('')
print('Aca mostramos como modificar una Variable Global\n')
variableglobal = 'Esto es una variable global'#Mostramos con estas lineas
mostrarglobal()								# como Modificar una Variable Global
valorglobal()				
print(variableglobal)

print('Aca Creamos con una Funcion la Variable Global\n')
crearGlobal()
print(nuevaVariable)


frase = 'anita lava la tina' #frase aca es una Variable Global
print(frase)

resultado = palindromo(frase)
print(frase)
print(resultado)

print(factorial(4))
print(factorial(7))
print(factorial(250))


variable1 = multiplicacion
mostrarResultado(variable1)	

print("La suma es: ", suma1(4,5,6))
print("La division es: ", division(10,2))
print("La tupla es: ",multiplesValores())
