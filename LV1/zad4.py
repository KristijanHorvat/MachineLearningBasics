file = open("song.txt")
num={}
count=0
lines = file.read().strip().split()

for word in lines:
    num [word] = lines.count(word)
print(num)