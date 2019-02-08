from random import *

class Bag():
	def __init__(self):
		self.data = []
		print('Creating bag...')

	def add(self,item):
		self.data.append(item)
		print('Added an item to the bag')

	def removeItem(self,item):
		if item in self.data:
			self.data.remove(item)
			print('Removed an item from the bag')
		else:
			print('Could not remove, item not found in bag')

	def contains(self,item):
		if item in self.data:
			return True
		else:
			return False

	def numItems(self):
		return len(self.data)

	def grab(self):
		if self.data:
			print('Pulled an item from the bag')
			index = randrange(len(self.data))
			return self.data[index]
		else:
			print('Bag is empty, cannot pull an item')

	def __str__(self):
		if self.data:
			return ', '.join(map(str,self.data))

def main():
	#creating bag
	bag = Bag()
	#testing functions on empty bag
	bag.removeItem('h')
	bag.contains('h')
	bag.grab()
	print(bag.numItems())
	#adding items to bag, then testing functions
	bag.add('h')
	bag.add(19)
	print(bag.numItems())
	bag.contains('h')
	bag.__str__()
	print(bag.grab())
	bag.removeItem(19)
	bag.contains(19)
	bag.__str__()

if __name__ == '__main__':
	main()
