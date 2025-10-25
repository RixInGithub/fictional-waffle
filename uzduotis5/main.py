# uzduoties salyga:
"""
	Palyginkite skaičius:
		a) 0 ir -91
		b) 0.7 ir 0
		c) -2.5 ir -2.6
		d) 3.3 ir -2.8
		e) 1/15 ir 1/5
		f) 2 8/9 ir 2.5
		g) 3/4 ir 7/9
		h) 3 ** -5 ir 3 ** 0
		i) (-4) ** 3 ir (-2) ** 5
"""
# data.txt pvz: https://github.com/RixInGithub/fictional-waffle/blob/main/uzduotis5/data.txt
# NOTE: kai kuriuos supaprastinau, pvz "3 ** -5 ir 3 ** 0" => "1/243 ir 1"
with open("./data.txt") as nIO: print(f"{[(count:=97),(n:=[[a.rstrip('\n'),a.rstrip('\n').split(' ')] for a in nIO.readlines()]),''][2]}{[(n:=[[a[0],[float(b.split('/')[0])/float(b.split('/')[1]) if '/' in b else float(b) for b in a[1]]] for a in n]),''][1]}{'\n'.join([(' '*4)+chr((count:=count+1)-1)+') '+a[0].split(' ')[0]+' '+chr(60+(a[1][0]>a[1][1])+(a[1][0]>=a[1][1]))+' '+a[0].split(' ')[1] for a in n])}")