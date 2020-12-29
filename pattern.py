
def doStuff():
    n = int(input())
    numTimes = int(n)
    count = 0

    if (n == 1):
        print("+-+")
        print("| |")
        print("+-+")

    else:
        while numTimes>0:
            space = " " * count

            #if it is the first line we're printing
            if numTimes == 1:
                print(space + "| |")
                print(space + "+-+")

            #if it's the last line to print
            if numTimes == n:
                pass

            #if it's not the first nor the last line
            if (1 < numTimes < n):
                pass

            numTimes = numTimes - 1
            count = count + 2

doStuff()