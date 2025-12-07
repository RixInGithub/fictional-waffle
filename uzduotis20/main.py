class Animal:
	def __init__(self, snd="..."):
		self.snd=snd
	def makeSound(self):
		print(self.snd)

class Dog(Animal): pass

class Cat(Animal): pass

class Cow(Animal): pass

def playSound(a):
	a.makeSound()

animals = [Dog("woof"), Cat("meoww"), Cow("moooo")]
for a in animals: playSound(a)