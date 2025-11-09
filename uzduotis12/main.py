moed=chr(119-(int(input())-1)*22) # 1 => 0 => 119 => "w", 2 => 1 => 102 => "f"
__import__("os").remove("output.txt") # this removes, but then we open file. file will be cleared!
with open("output.txt",moed,encoding="utf8") as oIO, open("data.txt","r",encoding="utf8") as dIO:
	oIO.write("\n\n".join([dIO]*(moed=="a"))) # i dont get it, was i supposed to call write twice with one arg being the string and the second one being \n\n + string?