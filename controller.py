import os
from xml.etree.ElementTree import PI

rootPath = "./"
extName  = ".tsv"

fileWalking = os.walk('./sourceData')
splitedTmp = None
fileUrl  = ''
pId      = ''
language = ''

for path, dir_list, file_list in fileWalking:  
    for file_name in file_list: 
        fileUrl = os.path.abspath(path + '/' + file_name)
        if os.path.splitext(fileUrl)[1] == extName:
            splitedTmp = fileUrl.split("/")
            pId        = splitedTmp[-1].split("-")[0]
            language   = splitedTmp[-2]
            
            outputFile = "./result/"+language+"/"+pId+"-simi.csv"
            logFile    = "./result/"+language+"/"+pId+"-simi.log"
            # os.system("java -jar codenetSimi.jar " + fileUrl + " 200 " + outputFile + " > " + logFile)

            print("java -jar codenetSimi.jar " + fileUrl + " 200 " + outputFile + " > " + logFile)
            # print(os.path.splitext(fileUrl))
        