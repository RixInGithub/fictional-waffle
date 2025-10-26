# "how to obtain the data?????!?!???!?!"
# first of all, right click on the codeblock that has the text and go click on the funny "Inspect" option
# then go to the "Elements" option and make sure the blue background is on a <pre> element
# if so, go to the "Console" option and just type in |$0.innerText| (without the vertical pipes)
# you should see an orange text pop up with quotes around. right click on that, click "Copy string contents"
# and paste wherever you want
# if line 3 is false, just go to https://github.com/RixInGithub/fictional-waffle/blob/main/uzduotis6/data.txt and click on the button which shows a square on top of another square
with open("./data.txt", "r", encoding="utf8") as strIO:
	s = strIO.read()
	print("\n".join([" ".join([a, s.count(str(a))]) for a in range(10)]))