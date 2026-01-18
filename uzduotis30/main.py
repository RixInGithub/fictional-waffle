# Parašykite programą, kuri išspausdintų visus 3-ženklius skaičius, kurių vidurinysis skaitmuo yra 3.

# math based solution, 0 strings
count = 130
while count/1e3 < 1:
	while ((count % 100) // 10) == 3:
		print(count)
		count += 1
	count += 90