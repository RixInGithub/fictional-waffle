# Parašykite programą, kuri suformuotų du n elementų masyvus A ir B (skaičiai renkami klaviatūra). Masyvus išspausdinkite. Formuokite trečią masyvą C: jeigu A ir B atitinkamų elementų suma didesnė už 10, įrašykite raidę D, priešingu atveju - raidę M. Masyvą C išspausdinkite.
n = 5
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(n)]
c = ["M"] * n # preset
count = 0
while count<n:
	if a[count]+b[count] > 10: c[count] = "D"
	count += 1
print(c)