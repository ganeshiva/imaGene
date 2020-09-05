from PIL.ExifTags import TAGS
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import inspect 
from datetime import datetime

fontFile='C:\\Windows\\Fonts\\segoeuib.ttf'
fontSize = 10
txtColor =(255,255,255)
shadowcolor = "yellow"

exifTagDateTimeFormat = "%Y:%m:%d %H:%M:%S" #2018:01:10 11:33:28

def calcDimensions(width, height, newWidth):
    #print("Size:" + str(width) + "x" + str(height))
    wpercent = (newWidth/float(width))
    newHeight = int((float(height)*float(wpercent)))
    return (newWidth,newHeight)

def imageOpen(fileName):
    #print(fileName)
    try:
        imgOject=Image.open(fileName)
        #imgOject.verify()
        return imgOject
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None

def imageExif(imgOject):
    try:
        exifDict = imgOject._getexif() 
        exifTags = {}
        if exifDict == None:
            return None
        for (key, val) in exifDict.items():
            exifTags[TAGS.get(key)] = val
        return exifTags   
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None

def imageSetFont(fontFile,fontSize):
    try:
        font = ImageFont.truetype(fontFile, fontSize)
        return font
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None

def imageOverlayText(imageText, imgObject):
    try:
        font = imageSetFont(fontFile, fontSize)
        fontXDim, fontYDim = font.getsize(imageText)
        #print("FontFileSize: "+str(fontXDim)+"x"+str(fontYDim))
        xDim, yDim = imgObject.size
        xtxtPos = xDim - int(xDim / 100) - fontXDim 
        ytxtPos = yDim - int(yDim / 100) - fontYDim 
        #print("ImageFileSize: "+str(xDim)+"x"+str(yDim))
        txt=Image.new('L', (fontXDim,fontYDim))
        txtImg = ImageDraw.Draw(txt)
        
        # thicker border
        txtImg.text((xtxtPos-1, ytxtPos-1), imageText, font=font, fill=shadowcolor)
        txtImg.text((xtxtPos+1, ytxtPos-1), imageText, font=font, fill=shadowcolor)
        txtImg.text((xtxtPos-1, ytxtPos+1), imageText, font=font, fill=shadowcolor)
        txtImg.text((xtxtPos+1, ytxtPos+1), imageText, font=font, fill=shadowcolor)
        
        # Actual Text
        txtImg.text( (0, 0), imageText, font=font, fill=255)
        w=txt.rotate(0,  expand=1)

        imgObject.paste( ImageOps.colorize(w, (0,0,0), txtColor), (xtxtPos, ytxtPos),  w)
        return imgObject
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
        
def imagePrintAttribute(imgObject, exifTag):
    try:
        imgDateTime = datetime.strptime(exifTag['DateTime'],exifTagDateTimeFormat)
        imgTxt = imgDateTime.strftime("%Y%b%d")
        return (imageOverlayText(imgTxt,imgObject))
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
        
def imageResize(imgObject, newWidth):
    try:
        width, height = imgObject.size
        newDimension = calcDimensions(int(width), int(height), newWidth)
        resizedImg = imgObject.resize(newDimension, Image.ANTIALIAS)
        return resizedImg
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
        
def imageSave(imgObject,filename):
    try:
        imgObject.save(filename)
        return True
    except Exception as e:
        print( inspect.stack()[0][3] + " Exception: " + str(e))
        return None
