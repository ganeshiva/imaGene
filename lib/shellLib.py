import os
from datetime import datetime
import inspect 
import re

def buildDstPath(currentPath, srcDir, dstDir):
    try:
        parentDir = "unorganised"
        fileName = os.path.basename(currentPath)
        imgDateTime = datetime.fromtimestamp(os.stat(currentPath).st_mtime)
        modifiedBasedPath = str(imgDateTime.year) + os.sep + str(imgDateTime.month) + os.sep + str(imgDateTime.day)
        newBasePath = dstDir  + os.sep + parentDir  + os.sep + modifiedBasedPath
        newFilename = newBasePath + os.sep + fileName
        os.makedirs(newBasePath, exist_ok=True)
        return newFilename.replace("\x00","").replace("  ","")
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
    
def buildExifBasedPath(currentPath, exifTag, dstDir):
    try:
        exifTagDateTimeFormat = "%Y:%m:%d %H:%M:%S" #2018:01:10 11:33:28
        
        parentDir = charFilter((exifTag.get('Make','camera') + "-" + exifTag.get('Model',"unknown") ).replace("\x00","").replace("  ","")).strip()
        if parentDir == '-':
            parentDir = ""
        fileName = os.path.basename(currentPath)
        #imgDateTime = datetime.fromisoformat(exifTag['DateTime'])
        imgDateTime = exifTag.get('DateTime', None)
        if imgDateTime != None:
            imgDateTime = datetime.strptime(exifTag['DateTime'],exifTagDateTimeFormat)
            exifbasedPath = dstDir + os.sep + parentDir + os.sep + str(imgDateTime.year) + os.sep + str(imgDateTime.month) + os.sep + str(imgDateTime.day)
        else:
            exifbasedPath = dstDir + os.sep + parentDir
        newFilename = exifbasedPath + os.sep + fileName
        os.makedirs(exifbasedPath, exist_ok=True)
        return newFilename
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None

def charFilter(strInput):
    return re.sub('[^a-zA-Z0-9 \n\.\-_]', '', strInput)