# Klaviatūra įvedami n skaičių — vidutinės n dienų temperatūros. Apskaičiuokite kelias dienas vidutinė temperatūra buvo teigiama.
res = 0
n = 5
count = 0
while count < n:
	if int(input()) > 0: res += 1
	count += 1
print(res)