class Books :

	def __init__(self, name, price) :
		self.name = name
		self.price = price

	def getBooks(self) :
		return {"name": self.name, "price": self.price}
