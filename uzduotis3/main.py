# x%2 == 0 => dešinė (what is it in english again? fiddlesticks!!!)
# x%2 == 1 => kairė (someone help)

pplIO = open("./data.txt","r",encoding="utf8")
ppl = [(a:=int(pplIO.readline())),[list(map(int, a.split(" "))) for a in pplIO.readlines()[:a]]][1]
pplIO.close()
desine = []
kaire = []
for a in ppl: (desine if (a[0]%2==0) else kaire).append(a[1])
print("\n".join(map(str,[(a:=sum(*desine))+(b:=sum(*kaire)), b, a, b/len(kaire), a/len(desine)])))