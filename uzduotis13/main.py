from copy import deepcopy as cp

with open("data1.txt","r",encoding="utf8") as d1IO, open("data2.txt","r",encoding="utf8") as d2IO:
	oD1 = d1IO.read().lower().split(" ")
	oD2 = d2IO.read().lower().split(" ")
	d1 = [a for a in cp(oD1) if a in oD2]
	d2 = [a for a in cp(oD2) if a in oD1]
	needsCounted = [*set(cp(d1)+cp(d2))]
	res = ";".join([" - ".join([a, str(max(d1.count(a),d2.count(a)))]) for a in needsCounted])
	with open("output.txt","w",encoding="utf8") as oIO: oIO.write(res)