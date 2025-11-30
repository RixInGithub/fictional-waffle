class Payer:
	name = ""
	heat = 0
	service = 0
	water = 0
	def __init__(self, name, heat, service, water):
		self.name = name
		self.heat = float(heat)
		self.service = float(service)
		self.water = float(water)
	def total(self):
		return sum([a for a in [self.heat,self.service,self.water] if a>0])

with open("data.txt","r",encoding="utf8") as payersIO:
	payers = [Payer(*a.split(" ")) for a in payersIO.read().split("\n")] # hehe
	totals = [sum([a.heat for a in payers if a.heat>0]), sum([a.service for a in payers if a.service>0]), sum([a.water for a in payers if a.water>0])]
	print("Už šilumą turi būti sumokėta:  ", totals[0])
	print("Už telefoną turi būti sumokėta:", totals[1])
	print("Už vandenį turi būti sumokėta: ", totals[2])
	print("-"*33)
	print("    Vardas"," "*8,"Turi mokėti")
	print("-"*33)
	longestName = max(payers, key=lambda p: len(p.name))
	for p in payers:
		print(" ",p.name+" "*(len(longestName.name)+18-len(p.name)),p.total())
	print("-"*33)