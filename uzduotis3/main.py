pplIO = open("./ppl.txt","r",encoding="utf8")
linesArr = [a[:-1] for a in [(a:=int(pplIO.readline())),pplIO.readlines()[:a]][1]]
print(linesArr)