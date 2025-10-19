pplIO = open("./ppl.txt","r",encoding="utf8")
linesArr = [b[:-1] for b in [(a:=int(pplIO.readline())),pplIO.readlines()[:a]][1]]
print(linesArr)