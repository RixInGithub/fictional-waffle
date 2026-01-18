# Parašykite programą, kuri išspausdintų skaičių nuo 1 iki 10 daugybos lentelę.

count1 = 0
while count1 < 10:
	print(str(count1)+":\n****")
	count2 = 0
	while count2 < 10:
		print(count2+1, "*", count1+1, "=", (count2+1)*(count1+1))
		count2 += 1
	count1 += 1