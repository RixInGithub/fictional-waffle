from functools import reduce
with open("./data.txt","r",encoding="utf8") as lIO, open("./2encode.txt","r",encoding="utf8") as dIO:
	letters = int(lIO.readline())
	letters = [a.split(" ") for a in lIO.readlines(letters)]
	l2Coded = dict(letters) # entries => dict (for ezier management)
	rawL = "".join([a[0] for a in letters])
	notL = "".join([a for a in "aąbcčdeęėfghiįyjklmnoprsštuųūvzž" if not a in rawL])
	toEncode = dIO.read().split(" ")
	print(toEncode, l2Coded)
	print("\n".join([" ".join([l2Coded[b] for b in a if l2Coded.get(a,None)!=None]) for a in toEncode]))