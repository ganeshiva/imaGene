import os
from datetime import datetime
import inspect 

def buildDstPath(currentPath, srcDir, dstDir):
    try:
        fileName = os.path.basename(currentPath)
        basePath = currentPath.replace(fileName,"")
        basePath = basePath.replace(srcDir,"")
        newFilename = dstDir + basePath + fileName
        os.makedirs(dstDir + basePath, exist_ok=True)
        return newFilename
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
    
def buildExifBasedPath(currentPath, exifTag, dstDir):
    try:
        exifTagDateTimeFormat = "%Y:%m:%d %H:%M:%S" #2018:01:10 11:33:28
        
        parentDir = exifTag.get('Make','camera') + "-" + exifTag.get('Model',"unknown")
        fileName = os.path.basename(currentPath)
        #imgDateTime = datetime.fromisoformat(exifTag['DateTime'])
        imgDateTime = datetime.strptime(exifTag['DateTime'],exifTagDateTimeFormat)
        exifbasedPath = dstDir + '\\' + parentDir + '\\' + str(imgDateTime.year) + '\\' + str(imgDateTime.month) + '\\' + str(imgDateTime.day)
        newFilename = exifbasedPath + '\\' + fileName
        os.makedirs(exifbasedPath, exist_ok=True)
        return newFilename
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None