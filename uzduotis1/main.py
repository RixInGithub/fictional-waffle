wordsIO = open("./data.txt","r",encoding="utf8")
print([sum(map(ord, a[:-1])) for a in wordsIO.readlines()]) # "i am 5 parellel universes ahead of you" ahh move 🥀
wordsIO.close()