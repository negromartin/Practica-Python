def decorador(func):
	def nuevaFuncion(*args,**kwargs):#*args y **kwargs son n parametros
		print("Empieza la funcion")	#codigo primero
		func(*args,**kwargs)
		print("Termino la funcion")#codigo segundo
	return nuevaFuncion
@decorador
def saluda():
	print("hola mundo")
@decorador
def suma(num1,num2):
	print(num1+num2)


saluda()
suma(5,6)

#Este siguiente decorador es mas complejo y muestra como agregarle parametros

def decorador1(valid): # en esta parte muestra q se puede agregar parametros al decorador

	def d_ecorador(func):
		def antes():
			print("Vamos a ejecutar la funcion")

		def despues():
			print("Se ejecuto la funcion")

		def nuevaFuncion1(*args,**kwargs):
			if valid:
				antes()
				resultado = func(*args,**kwargs)
				despues()
				return resultado

		return nuevaFuncion1

	return d_ecorador
	

@decorador1(True)
def saluda1():
	print("hola mundo")
@decorador1(True)
def suma1(num1,num2):
	print(num1+num2)

saluda1()
suma1(20,30)