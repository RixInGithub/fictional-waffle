import re as regex
with open("./data.txt", "r", encoding="utf8") as strIO:
	s = strIO.read()
	l = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
	most = ["nėviena", 0]
	for group in regex.findall(r".{5}|(?<=.{5}).+",l):
		print(" ".join([" ".join([(A:=a.upper()+a), str(c:=s.count(a)+s.count(a.upper()))]), most:=([A,c] if c>most[1] else most)][0] for a in group])) # surely noone will criticize my overly use of the walrus op, right?
	print("Dažniausiai kartojasi raidė", most[0])