# To check if all the problem are calculated



LANGUAGE = "Java"
outputFile = open(LANGUAGE+"_notFinished____.txt","w")

def checkAll(outputFile):
    resFile = None
    for line in open("problemList/" + LANGUAGE + "problemList.txt",'r').readlines():
        problemId = line[:-1]
    
    
        try:    
            resFile = open(LANGUAGE + "/result/" + problemId + "-simi.csv")    
        except FileNotFoundError:
            outputFile.write(problemId + "\n")
            resFile = None
            continue
    
        count = 0
        for tmpLine in resFile.readlines():
            if len(tmpLine[:-1].split(",")) == 3:
                count += 1
    
        #1109
        fileNum = 0
        for tokenLine in open(LANGUAGE + "/source/" + problemId + "-tokens.tsv", "r").readlines():
            if tokenLine != "\n":
                fileNum += 1
            
        pairNum = 0
        while fileNum > 0:
            pairNum += fileNum - 1
            fileNum -= 1
    
        if count != pairNum:
            outputFile.write(problemId + "\n")


    outputFile.close() 

def checkOne(outputFile, problemId):
    resFile = None
    try:
        resFile = open(LANGUAGE + "/result/" + problemId + "-simi.csv")
    except FileNotFoundError:
        print("target problem not started")
        return 

    count = 0
    for tmpLine in resFile.readlines():
        if len(tmpLine[:-1].split(",")) > 1:
            count += 1

    fileNum = 0
    for tokenLine in open(LANGUAGE + "/source/" + problemId + "-tokens.tsv", "r").readlines():
            if tokenLine != "\n":
                fileNum += 1
    pairNum = 0
    while fileNum > 0:
        pairNum += fileNum - 1
        fileNum -= 1

    if count == pairNum:
        print("finished")
    else:
        print("needed: " + str(pairNum))
        print("finished: " + str(count))

import sys
if __name__ == "__main__":
    problemId = sys.argv[2]

    if sys.argv[1] == 'all':
        checkAll(outputFile)
    else:
        checkOne(outputFile, problemId)


