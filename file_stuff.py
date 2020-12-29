
#myFile = open("testFile.txt", "w")
#myFile.write("Hello, this is a test file")

myFile = open("testingFile.txt", "w")
myFile.write("Hello, I have created and written to a file\n")
myFile.write("This is my second line\n")
myFile.write("And this is my last line\n")
myFile.close()

myFile = open("testingFile.txt", "r")
content = myFile.readlines()
for line in content:
    words = line.split()
    print(words)
myFile.close()