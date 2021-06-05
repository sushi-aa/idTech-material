#arushi

#replaces all instances of "default" with "default:" for correct verilog syntax

rFile = open("dummy_verilog.py", "r")
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

wFile = open("dummy_verilog.py", "w")
for i in replaceList:
    wFile.write(i+"\n")
wFile.close()

