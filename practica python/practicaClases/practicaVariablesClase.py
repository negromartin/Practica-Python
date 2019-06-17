class Circulo:#pi es una variable de clase
	_pi = 3.1416 #el caracter _ solo es una señal q pertenece a la clase
				#Es convencional al programador
	def __init__(self,radio):
		self.radio = radio

	def area(self):
		return (self.radio**2) * self._pi

circulo1 = Circulo(4)
circulo2 = Circulo(11)

print(Circulo._pi)
print("Area del circulo 1: ", circulo1.area())
print("Area del circulo 2: ", circulo2.area())
