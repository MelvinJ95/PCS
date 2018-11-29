class store_item(object): 

	def _init_(self, icon, name, stype, price, qty=0):
		# self.index = index
		self.icon = icon 
		self.name = name
		self.type = stype 
		self.price = price 
		self.qty = qty 

	def makeItem(self, icon, name, stype, price, qty=0):
		item = store_item()
		item.icon = icon
		item.name = name
		item.type = stype
		item.price = price
		item.price = qty
		return item

	def __str__(self):
		icon = str(self.icon)
		name = str(self.name)
		stype = str(self.type)
		price = str(self.price)
		string = icon + " " + name + " " + stype + " " + price
		return string