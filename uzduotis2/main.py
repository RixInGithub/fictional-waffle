namesIO = open("./data.txt","r",encoding="utf8")
print(sorted([sum(map(ord, a.split(" ")[0]))*int(a.split(" ")[1]) for a in namesIO.readlines()]))
namesIO.close()