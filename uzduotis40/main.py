# lunch?
def parseQ(q):
	if q.endswith("vnt"): return {"type":"unit","v":float(q[:-3])}
	if q.endswith("kg"): return {"type":"kg","v":float(q[:-2])} # meaningless qol feature
	if q.endswith("g"): return {"type":"g","v":float(q[:-1])}
	raise Exception("invalid amount "+q)

def parseFood(f):
	return {
		"name": f[0],
		"amnt": parseQ(f[1]),
		"carb": float(f[2]),
		"protein": float(f[3]),
		"fat": float(f[4]),
		"cal": float(f[5]),
	}

with open("maistine_verte.txt","r",encoding="utf8") as lIO:
	foods = [parseFood(a.rstrip("\n").split(" ")) for a in lIO.splitlines()]
	n = int(input("how much foods?"))
	print("available foods:\n\n"+"\n".join([f"{idx+1}: {a['name']}" for idx, a in enumerate(foods)]))
	inp = 