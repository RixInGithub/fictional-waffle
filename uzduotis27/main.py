# Klaviatūra įvedami n skaičių. Atskirai skaičiuojama lyginių ir nelyginių skaičių suma. Rezultatas parodomas ekrane.
res = [0,0] # 0 => even, 1 => odd
n = 5
count = 0
while count < n:
	num = int(input())
	res[num%2] += num
	count += 1
print(" ".join([str(a) for a in res]))