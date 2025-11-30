import re as regex
from copy import deepcopy as cp

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
	als = [Album(a[0], *[int(b) for b in a[1].split(" ")]) for a in als]
	totalMins = sum([a.mins for a in als])
	print(totalMins//60, totalMins%60)
	print("{:.2f}".format(sum([a.listens for a in als])/len(als)))
	longest = max([len(a.name) for a in als])+4
	als.sort(key=lambda a: a.listens, reverse=True)
	for a in als:
		print(a.name.ljust(longest, " "),a.year)