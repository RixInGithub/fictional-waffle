import re as regex

class Album:
	name = ""
	year = 0
	mins = 0
	listens = 0
	def __init__(self, name, year, hrs, mins, listens):
		self.name = name
		self.year = year
		self.mins = (hrs*60)+mins
		self.listens = listens

with open("DuomAlbumai.txt","r",encoding="utf8") as alIO:
	als = regex.findall(r"^([^\d]+) (.+)$", alIO.read(), regex.MULTILINE)
	print(als)