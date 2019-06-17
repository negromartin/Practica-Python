class Lapiz: #Plantilla
	
#Metodos
	def __init__(self,color,contieneBorrador,usaGrafito): # es el SET de toda clase.
		self.color = color  #Estos 3 son los atributos
		self.contieneBorrador = contieneBorrador
		self.usaGrafito = usaGrafito

	def dibujar(self):#Variable self es la q va a tratar y devolver
		print("El lapiz esta dibujando...")

	def borrar(self):
		if self.validarB():
			print("El lapiz esta borrando")
		else:
			print("No es posible borrar")
	
	def validarB(self):
		return self.contieneBorrador	

#Esti es un objeto
lapizGenerico = Lapiz("Verde",True,True)
print("El lapiz es de color: ",lapizGenerico.color)
print("Contiene Borrador?: ",lapizGenerico.contieneBorrador)
print("Es de Grafito?:",lapizGenerico.usaGrafito)
lapizGenerico.dibujar()
lapizGenerico.borrar()

