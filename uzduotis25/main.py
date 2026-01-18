# Parašykite programą, kuri apskaičiuotų n klaviatūra įvedamų skaičių sumą. Naudokite funkciją input()
s = 0
n = 5
count = 0
while count < n:
	s += int(input())
	count += 1
print(s)