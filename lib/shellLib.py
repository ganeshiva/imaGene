import os
def buildNewPath(currentPath, srcDir, dstDir):
    fileName = os.path.basename(currentPath)
    basePath = currentPath.replace(fileName,"")
    basePath = basePath.replace(srcDir,"")
    newFilename = dstDir + basePath + fileName
    os.makedirs(dstDir + basePath, exist_ok=True)
    return newFilename
