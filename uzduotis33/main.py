# Parašykite programą, kuri žvaigždutėmis pavaizduotų visus skaičiaus n skaitmenis (pradedant vienetais)
n = 321
while n>0:
	print("*"*(n%10))
	n//=10 # neato