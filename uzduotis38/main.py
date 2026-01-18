# Duotas sąrašas m. Parašykite programą, kuri surikiuotų masyvą ir iš masyvo pašalintų pasikartojančius skaičius. Rezultatą įrašytų į failą. 
# Reikalavimai programai: funkcijomis aprašytas duomenų skaitymas, rikiavimas, panašių elementų šalinimas, masyvo išvedimas į failą.
def genM():
	return [3,2,2,5,6,4,4,1]

sortM = sorted # don't tell me i had to sort this thing out myself

eraseSimilarFromM = lambda m: list(dict.fromkeys(m).keys()) # pretty sure this'll keep the sort

def writeM(m):
	with open("output.txt","w",encoding="utf8") as mIO:
		mIO.write(str(len(m))+"\n"+(" ".join(m)))

writeM(eraseSimilarFromM(sortM(genM()))) # got inspired by concatenative languages