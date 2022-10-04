from concurrent.futures import thread
import os, time
from xml.etree.ElementTree import PI

time_start = time.time()
rootPath = "./"
extName  = ".tsv"
language = "C++"
pIdListFile = "./problemList/" + language + "problemList(selected).txt"
# pIdListFile = "./problemList/" + language + "_notFinished.txt"
threadNum = 24
keywordsList = "./keywordsList/" + language + ".reserved"

for pIdLine in open(pIdListFile,"r").readlines():
    fileURL    = language + "/source/" + pIdLine[:-1] + "-tokens.tsv"
    outputFile = language + "/result/" + pIdLine[:-1] + "-simi.csv"
    outputlog  = language + "/result/" + pIdLine[:-1] + "-simi.log"  
    print("Opertaing: " + fileURL)
    os.system("java -jar codenetSimi_editDisOnly_faster.jar " + fileURL + " " + str(threadNum) + " " + outputFile + " " + keywordsList + " > " + outputlog)
    print("Over")

time_end = time.time()  
with open(language+'/over.txt',"w") as f:
    f.write("time: " + str(time_end-time_start))
    f.close()
    
# fileWalking = os.walk('./sourceData')
# splitedTmp = None
# fileUrl  = ''
# pId      = ''
# language = ''

# for path, dir_list, file_list in fileWalking:  
#     for file_name in file_list: 
#         fileUrl = os.path.abspath(path + '/' + file_name)
#         if os.path.splitext(fileUrl)[1] == extName:
#             splitedTmp = fileUrl.split("/")
#             pId        = splitedTmp[-1].split("-")[0]
#             language   = splitedTmp[-2]
            
#             outputFile = "./result/"+language+"/"+pId+"-simi.csv"
#             logFile    = "./result/"+language+"/"+pId+"-simi.log"
#             # os.system("java -jar codenetSimi.jar " + fileUrl + " 200 " + outputFile + " > " + logFile)

#             print("java -jar codenetSimi.jar " + fileUrl + " 200 " + outputFile + " > " + logFile)
#             # print(os.path.splitext(fileUrl))
        
