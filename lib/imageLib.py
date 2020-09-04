from PIL import Image

def calcDimensions(width, height, newWidth):
    #print("Size:" + str(width) + "x" + str(height))
    wpercent = (newWidth/float(width))
    newHeight = int((float(height)*float(wpercent)))
    return (newWidth,newHeight)

def imageResize(originalFile, newWidth):
    try:
        img=Image.open(originalFile)
        width, height = img.size
        newDimension = calcDimensions(int(width), int(height), newWidth)
        new_img = img.resize(newDimension, Image.ANTIALIAS)
        return new_img
    except Exception as e:
      print("Unable to process: " + str(originalFile) + " Exception: " + str(e))
      return None
      
def imageSave(imageObject,filename):
    try:
        imageObject.save(filename)
        return True
    except Exception as e:
      print("Unable to process: " + str(filename) + " Exception: " + str(e))
      return None
