# Parašykite programą, kuri suformuotų n elementų masyvą iš klaviatūra įvedamų skaičių ir apskaičiuotų šių skaičių aritmetinį vidurkį. 
# Programa turi pirmojoje eilutėje išspausdinti suformuotą masyvą, antrojoje - vidurkį.
n = 5
count = 0
l = []
while count<n:
	l.append(int(input()))
	count += 1
print(repr(l)+"\n"+str(sum(l)/len(l))) # printing a list calls it's __repr__ method