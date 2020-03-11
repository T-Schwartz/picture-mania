
from PIL import Image
import numpy as np
import image
#import Exif#Tags as exif
from resizeimage import resizeimage
#from colorama import Fore, Back, Style 

picture = Image.open("castle.jpg")


pixlArray = np.asarray(picture)

size = pixlArray.shape

width, height = picture.size

screenChars=215 #how many charecters fit on my screen
w=1 #what you will enlarge the width of the image by
h=1 #what you will enlarge the length of the image by

while ((width>screenChars) and (w*width>screenChars)):
    w=w/1.2
    h=h/1.2
picture = resizeimage.resize_cover(picture, [width*w, height*h])

width, height = picture.size

brightArray = []

i=0

for x in range(height):
    for y in range(width):
        r,g,b = picture.getpixel((y,x))
        bright=(r + g + b) / 3
        brightArray.append(bright)
        i+=1

symblArray=["`","^","\\",'"',",",":",";","I","l","!","i","~","+","_","-","?","]",
            "[","}","{","1",")","(","|","\\\\","/","t","f",
            "j","r","x","n","u","v","c","z","X","Y","U",
            "J","C","L","Q","0","O","Z","m","w","q","p",
            "d","b","k","h","a","o","*","#","M","W","&","8","%","B","@","$"]
displayArray=[]
j=0
f=0
conversion=float((max(brightArray)/len(symblArray)-1))

while j<len(brightArray):
    symbolIndex=(brightArray[j])//(conversion)
    symbolIndex=int(symbolIndex)
    if (symbolIndex<0):
        symbolIndex=0
    elif (symbolIndex>len(symblArray)-1):
        symbolIndex=len(symblArray)-1

    displayArray.append(symblArray[symbolIndex])

  #  if (f>450):                  # this is so it fits my screen
   #         print("\nYour picture is to big")
    #        print ("F", f, "width", width, "height",height )
     #       break
        
    if (f<width-1):
        printy=(displayArray[j]*2)
        print(('\033[1m'+ printy), end="")
        f+=1
    else:
        print ()
        f=0
    
    j+=1


        
