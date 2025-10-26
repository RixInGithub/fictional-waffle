import re as regex
with open("./data.txt", "r", encoding="utf8") as strIO:
	s = strIO.read()
	a = lambda b: len(list(regex.finditer(b, txt)))
	print(f"""
Raidžių yra {a(r'[A-Za-ząčęėįšųūĄČĘĖĮŠŲŪ]')}
Skaitmenų yra {a(r'[0-9]')}
Tarpo simbolių yra {a(r' ')}
Kitokių simbolių yra {a(r'[^A-Za-ząčęėįšųūĄČĘĖĮŠŲŪ0-9 ]')}
"""[1:-1])