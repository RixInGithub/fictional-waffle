pplIO = open("./ppl.txt","r",encoding="utf8")
linesArr = [line.rstrip('\n') for line in pplIO.readlines()[:int(pplIO.readline())]]
print(linesArr)