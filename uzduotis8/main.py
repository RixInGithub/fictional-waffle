with open("./data.txt", "r", encoding="utf8") as cIO:
	cities = cIO.read()
	print(f"""
--------------------------------
Pradiniai duomenys
--------------------------------
{cities}
--------------------------------
Išrinkti miestai
--------------------------------
{'\n'.join([c for c in cities.split('\n') if ' ' in c])}

"""[1:])

# leaves that extra line at the end too btw