# Parašykite programą kuri suformuotų n sveikųjų skaičių masyvą A. Po to šio masyvo elementus didesnius už N surašytų į masyvą B, o likusius į C.
a = [1,2,3,4,5,10,36]
N = 10
b = [_ for _ in a if _>10]
c = [_ for _ in a if _<=10]
print(b,c)