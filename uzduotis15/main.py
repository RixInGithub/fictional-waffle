import json
exists=False
try:
	with open("saveData.json","r",encoding="utf8") as chkIO: exists=True
except: pass
if not exists:
	nm = input("įveskite profilio vardą: ")
	logs = 0
	rox = 0
	with open("saveData.json","w",encoding="utf8") as startIO: json.dump([nm,logs,rox],startIO)
# look man, i genuinely have no excuse as to why am i doing this. i just suck at making games bruh. i just want good grade man
with open("saveData.json","r+",encoding="utf8") as dataIO:
	nm,logs,rox = dataIO.read()
	dataIO.seek(0)
	dataIO.truncate(0)
	running = True
	while running:
		print("0 - exit\n1 - keisti vardą\n2 - kapoti medžio\n3 - kasti akmens\n4 - rodyti medžio+akemns turį")
		try:
			opt = int(input("padarykite pasirinkimą: "))
		except: opt = 0 # stupid
		match opt:
			case 1:
				tmp = input("naujas vardas (spauskite enter, jei norite anuliuoti veiksmą): ")
				if tmp.strip()!="": nm = tmp
			case 2: logs+=5
			case 3: rox+=5
			case 4:
				print(f"{logs} med{"žiai" if logs!=1 else "is"}\n{rox} akmen{"y" if logs!=1 else "i"}s")
			case _: # if opt is 0 or smth invalid
				running = False