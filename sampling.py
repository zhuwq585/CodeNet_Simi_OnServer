

SOURCE = "./SimiRes/Java_All.csv"

# init similarity dict 
simiDict = {}

start  = 0.50
keyTmp = None
while start < 1.01:
    keyTmp = str(start)[:4]
    while len(keyTmp) < 4:
        keyTmp = keyTmp + "0"
    simiDict[keyTmp] = None
    start += 0.01

count = 0
sourceLines = open(SOURCE,"r").readlines()

pairTarget = None
simiTmp    = None
splitTmp   = None
for sourceIndex in range(len( sourceLines)):
    if sourceLines[sourceIndex] == "\n":
        pairTarget = None
    else:
        splitTmp = sourceLines[sourceIndex][:-1].split(",")
        if len(splitTmp) == 1:
            pairTarget = splitTmp[0]
        elif len(splitTmp) == 3:
            simiTmp = splitTmp[2][:4]
            while len(simiTmp) < 4:
                simiTmp = simiTmp + '0'
            if simiTmp in simiDict:
                if simiDict[simiTmp] == None:
                    simiDict[simiTmp] = (pairTarget, splitTmp[0])
                    count += 1
    
    if count > len(simiDict):
        break

with open("Java_samplingResult.txt","w") as f:
    for i in simiDict:
        f.write(str(i) + ":" + str(simiDict[i]) + "\n")