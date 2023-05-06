word=0
wordh=0
words=0
spam=0
ham=0
uskl=0
file = open("SMSSpamCollection.txt")
for line in file:
    
    if(line.startswith("ham")):
        ham+=1
        wordh+=len(line.split())

    if(line.startswith("spam")):
        spam+=1
        words+=len(line.split())
        if(line.strip().endswith("!")):
            uskl+=1

print(wordh/ham)
print(words/spam)
print(uskl)
    