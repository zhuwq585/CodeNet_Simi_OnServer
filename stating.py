

SOURCE = "./SimiRes/Java_All.csv"

# init similarity dict 
simiDict = {}

start  = 0.50
keyTmp = None
titleStr = ""
while start < 1.01:
    keyTmp = str(start)[:4]
    while len(keyTmp) < 4:
        keyTmp = keyTmp + "0"
    simiDict[keyTmp] = 0
    start += 0.01
    titleStr = titleStr + keyTmp + ","

count = 0
sourceLines = open(SOURCE,"r").readlines()

pairTarget = None
simiTmp    = None
splitTmp   = None
pairSum    = 0
for sourceIndex in range(len( sourceLines)):
    if sourceLines[sourceIndex] == "\n":
        pairTarget = None
    else:
        splitTmp = sourceLines[sourceIndex][:-1].split(",")
        if len(splitTmp) == 1:
            pairTarget = splitTmp[0]
        elif len(splitTmp) == 3:
            pairSum += 1
            simiTmp = splitTmp[2][:4]
            while len(simiTmp) < 4:
                simiTmp = simiTmp + '0'
            if simiTmp in simiDict:
                simiDict[simiTmp] += 1
                count += 1


with open("Java_SimiDivi.csv","w") as f:
    f.write(titleStr + "\n")
    f.write(str(pairSum) + "\n")
    for i in simiDict:
        f.write( str(simiDict[i]) + ",")