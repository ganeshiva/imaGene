#!/usr/bin/python

codeHeader='''
title="Organise, Optimise Large Image and annotate info"
summary="Group Datewise, resize image and overlay text attributes"
author=Ganeshiva
created=20200829
updated=20200905
cmdLine="python"
dependancy="pip package PIL, datetime, inspect, os"
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
        index = 0
        # Search for .jpg files recursively through Source Directory
        for subdir, dirs, files in os.walk(srcDir):
            for file in files:
                if imageExtension in file:
                    currentFilePath = os.path.join(subdir, file)
                    # Open Image as Object
                    imgObject = imageOpen(currentFilePath)
                    # Get Image Exif Attributes
                    exifTag = imageExif(imgObject)
                    # Resize Image 
                    imgObject = imageResize(imgObject, newImgWidth)
                    
                    if exifTag != None:
                        newFilePath = buildExifBasedPath(currentFilePath, exifTag, dstDir)
                        imgObject = imagePrintAttribute(imgObject, exifTag)
                        if newFilePath == None:
                            newFilePath = buildDstPath(currentFilePath, srcDir, dstDir)
                    else:
                        newFilePath = buildDstPath(currentFilePath, srcDir, dstDir)
                    
                    if imgObject != None:
                        if imageSave(imgObject,newFilePath) != None:
                            index += 1
                            print(str(index) +": ImageSaved: " + str(newFilePath))
                        else:
                            print("Unable to Save Image: " + str(currentFilePath))
                    else:
                        print("Unable to Resize Image: " + str(currentFilePath))
    else:
        print("Invalid Arguments supplied!: " + str(argument))
        print("Try Supported Cmd: python <appName.py> <c:\\Source\With\Images\> <d:\\Destination\With\Images\> <resizedHeight> <printDate:{true/false}> <printLocation:{true/false}>")

print("### ~~~~~~ Exit: Script file: " + __file__ + " ~~~~~~~###")