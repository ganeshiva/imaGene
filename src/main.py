#!/usr/bin/python

codeHeader='''
title="Optimise Large Image add annotate info"
summary="Resize image and overlay text attributes"
author=Ganeshiva
created=20200829
updated=20200904
cmdLine="python"
dependancy="pip package opencv-python"
license="(c)ganeshiva - freeToUse@yourOwnRisk - noGuaranty"
'''

import sys
sys.path.append("lib")
import os

from imageLib import *
from shellLib import *

imageExtension=".jpg"

if __name__ == '__main__':

    argument = sys.argv
    print("Input Argument(s): " + str(argument))
    
    if len(argument) == 6 :
        # Strip \n \r Characters in the Command line
        argument = [str(i).strip("\r\n") for i in argument]
        srcDir = argument[1]
        dstDir = argument[2]
        newImgWidth = int(argument[3])
        printDate = argument[4]
        printLocation = argument[5]
        
        for subdir, dirs, files in os.walk(srcDir):
            for file in files:
                if imageExtension in file:
                    currentFilePath = os.path.join(subdir, file)
                    newFilePath = buildNewPath(currentFilePath, srcDir, dstDir)
                    newImage = imageResize(currentFilePath, newImgWidth)
                    if newImage != None:
                        if imageSave(newImage,newFilePath) != None:
                            print("ImageSaved: " + str(newFilePath))
                        else:
                            print("Unable to Save Image: " + str(currentFilePath))
                    else:
                        print("Unable to Resize Image: " + str(currentFilePath))
    else:
        print("Invalid Arguments supplied!: " + str(argument))
        print("Try Supported Cmd: python <appName.py> <c:\\Source\With\Images\> <d:\\Destination\With\Images\> <resizedHeight> <printDate:{true/false}> <printLocation:{true/false}>")
    #import pdb; pdb.set_trace()
    print("Exit: Main")

print("### ~~~~~~ Exit: Script file: " + __file__ + " ~~~~~~~###")