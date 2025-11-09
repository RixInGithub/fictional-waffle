moed=chr(119-(int(input())-1)*22) # 1 => 0 => 119 => "w", 2 => 1 => 102 => "f"
__import__("os").remove("output.txt") # this removes, but then we open file. file will be cleared!
with open("output.txt",moed,encoding="utf8") as oIO, open("data.txt","r",encoding="utf8") as dIO:
	[dIO]*(moed=="a")