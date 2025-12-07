class Animal:
	def __init__(self): pass
	def makeSound(self):
		print("...")

class Dog(Animal):
	def makeSound(self):
		print("woof")

class Cat(Animal):
	def makeSound(self):
		print("meoww")

class Cow(Animal):
	def makeSound(self):
		print("moooo")

def playSound(a):
	a.makeSound()

animals = [Dog(), Cat(), Cow()]
for a in animals:
	playSound(a)