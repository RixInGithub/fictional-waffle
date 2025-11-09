with open("data1.txt","r+",encoding="utf8") as IO1, open("data2.txt","r+",encoding="utf8") as IO2:
	s1 = IO1.read()
	s2 = IO2.read()
	IO1.seek(0)
	IO1.truncate(0)
	IO2.seek(0)
	IO2.truncate(0)
	IO1.write(s2)
	IO2.write(s1)