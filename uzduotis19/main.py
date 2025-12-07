class Resource:
	def __init__(self, material, size):
		self.material = material
		self.size = size
	def __str__(self): return f"{self.size} {self.material}"

class Person:
	def __init__(self, name, age, favoriteFood="ravioli"):
		self.name=name
		self.age=age
		self.favoriteFood=favoriteFood
	def sleep(self): print("Snore...")
	def eat(self): print("I'm eating", self.favoriteFood, "and it's so good :)")
	def __str__(self): return f"Name: {self.name}, age: {str(self.age)}, favorite food: {self.favoriteFood}"

class Student(Person):
	def __init__(self, name, age, studies, favoriteFood="ravioli"):
		super().__init__(name,age,favoriteFood)
		self.studies=studies
	def sleep(self): print("I'm barely sleeping, snore...")

class Builder(Person):
	def __init__(self, name, age, resources, favoriteFood="ravioli"):
		super().__init__(name,age,favoriteFood)
		self.resources=resources
	def resources(self): print(f"{self.name} has {" ".join([str(r) for r in self.resources])}")

objs = []
with open("data.txt", "r", encoding="utf8") as pplIO:
	ppl = pplIO.read().split("\n")
	for p in ppl:
		pList = p.split(" ")
		pCls = globals()[pList[2]]
		pRest = pList[4:]
		if pList[2] == "Builder": pRest = [Resource(*r.split("-")) for r in pRest]
		pObj = pCls(pList[0], pList[1], pList[2], *pList[4:])
		objs.append(pObj)
for p in objs:
	print(p)