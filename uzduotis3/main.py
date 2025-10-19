pplIO = open("./data.txt","r",encoding="utf8")
linesArr = [(a:=int(pplIO.readline())),[a[:-1] for a in pplIO.readlines()[:a]]][1]
print(linesArr)