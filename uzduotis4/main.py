# NOTE: bug was with the gobble-gabbler'ing indexing
with open("./data.txt","r",encoding="utf8") as signalsIO:
	global rows, columns, rest
	rows, columns = list(map(int, signalsIO.readline().split(" ")))
	rest = [list(map(int, a.split(" "))) for a in signalsIO.readlines()]
for row in rest:
	newRow = []
	count = 0
	while count < columns:
		WE = row[max(count-1, 0):min(count+2,columns)] # yes, WE
		newRow+=[sum(WE)/len(WE)]
		count += 1
	print(" ".join(list(map(str, map(int, newRow))))) # float => int (to trim off decimal) => str (for joining)