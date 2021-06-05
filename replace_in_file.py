#arushi

#replaces all instances of "default" with "default:" for correct verilog syntax

fileToOpen = input("file name please: ")
rFile = open(fileToOpen, "r")
lineList = []
replaceList = []

for line in rFile:
    lineList.append( line.strip() )
rFile.close()

for i in lineList:
    if i == "default":
        replaceList.append("default:")
    else:
        replaceList.append(i)

wFile = open(fileToOpen, "w")
for i in replaceList:
    wFile.write(i+"\n")
wFile.close()

