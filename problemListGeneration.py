#####
# author: zhuwq585
# generate a unique problem list for each language.
# for each problem cluster, the minist one is reserved
####

from logging import root
import os , sys
from xml.etree.ElementTree import PI

PROBLEM_CLUSTER = "./identical_problem_clusters"
LANGUAGE_LIST   = ["Java", "Python", "C", "C++"]
ROOT            = "./"

class Cluster:
    def __init__(self):
        self.problemArr = []
        self.ifOver     = False
        
    def addProblemId(self, id):
        self.problemArr.append(id)

def getMinist(language, idArr):
    minTmp = sys.maxsize
    res    = None
    for id in idArr:
        size = len(open(ROOT + language + "/source/" + id + "-tokens.tsv", "r").readlines())
        if size <= minTmp:
            minTmp = size
            res = id
    
    return str(res)

def idFormat(idNum):
    res = str(idNum)
    
    while len(res) < 5:
        res = '0' + res
    
    return res

def checkSize(language, pId):
    return  len(open(ROOT+language+'/source/'+pId+"-tokens.tsv","r").readlines()) > 2


if __name__ == "__main__":
    ## create cluster dict 
    splitTmp    = None
    clusterTmp  = None
    clusterDic  = dict()
    with open(PROBLEM_CLUSTER,"r") as file:
        for clusterLine in file.readlines():
            clusterTmp = Cluster()
            splitTmp = clusterLine[:-1].split(",")
            for id in splitTmp:
                clusterDic[id] = clusterTmp
                clusterTmp.addProblemId(id)
                
    for language in LANGUAGE_LIST:
        outputFile = open("./" + language + "problemList.txt", "w")
        for idNum in range(0, 4053):
            id = "p" + idFormat(idNum)
            if id in clusterDic:
                if clusterDic[id].ifOver:
                    continue
                else:
                    minId = getMinist(language, clusterDic[id].problemArr)
                    if checkSize(language, minId):
                        outputFile.write( minId + "\n")
                        clusterDic[id].ifOver = True
            else:
                if checkSize(language, id):
                    outputFile.write(id + "\n")
        outputFile.close()  