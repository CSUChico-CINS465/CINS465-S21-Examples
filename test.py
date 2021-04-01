f = open("requirements.txt","r")
f2 = open("requirements2.txt","w+")

for line in f:
    line = line.split("=")
    f2.write(line[0]+"\n")

f2.close()