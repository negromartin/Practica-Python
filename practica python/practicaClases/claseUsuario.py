class Usuario:
	def __init__(self,username,password,email):
		self.username = username
		self.__password = self.__generarPassword(password)#el __atributo indica q es privado
		self.email = email
	
	def __generarPassword(self,password):#Simulamos la inscriptacion
		return password.upper()
	@property #pone como atributo primordial para leerlo
	def password(self):
		return self.__password
	
	@password.setter#setter para la variable password
	def password(self,valor):
		self.__password = self.__generarPassword(valor)


eduardo = Usuario("Negromartin11","Y eña??","Blackpeople@gmail.com")
print(eduardo.username)
print(eduardo.password)
print(eduardo.email)		