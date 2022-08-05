# To check if all the problem are calculated

from ast import Try


LANGUAGE = "Java"
outputFile = open(LANGUAGE+"_notFinished.txt","w")

resFile = None
for line in open("problemList/" + LANGUAGE + "problemList.txt",'r').readlines():
    problemId = line[:-1]
    
    
    try:
        resFile = open("SimiRes/" + LANGUAGE + "/" + problemId + "-simi.csv")    
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