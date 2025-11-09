with open("./data.txt","r",encoding="utf8") as lIO, open("./2encode.txt","r",encoding="utf8") as dIO:
	letters = int(lIO.readline())
	letters = [a.rstrip("\n").split(" ") for a in lIO.readlines()[:letters]]
	l2Coded = dict(letters) # entries => dict (for ezier management)
	toEncode = dIO.read().split(" ")
	print("\n".join([" ".join([l2Coded[b] for b in a if l2Coded.get(b,None)!=None]) for a in toEncode]))