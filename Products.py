class Products :

	def __init__(self, name, description, price, ownerName) :
		self.name = name
		self.description = description
		self.price = price
		self.ownerName = ownerName

	def getProducts(self) :
		return {"name": self.name, "description": self.description, "price": self.price, "ownerName": self.ownerName}
