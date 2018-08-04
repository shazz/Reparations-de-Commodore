# Script to remove EXIF metadata from JPEG images
#
# Deps: pip install Image
#

from PIL import Image
from PIL.ExifTags import TAGS
import os, sys, glob

os.chdir("../photos")
files = glob.glob('./**/*.JPG', recursive=True)
for imgfile in files:
    print("Stripping EXIF metadata from {0}".format(imgfile))

    image = Image.open(imgfile)
    
    if image._getexif() is not None:
        for (k,v) in image._getexif().items():
                print("{0} = {1}".format(TAGS.get(k), v))
    else:
        print("No EXIF metadata found !")
        
    data = list(image.getdata())
    image_stripped = Image.new(image.mode, image.size)
    image_stripped.putdata(data)
    image_stripped.save(imgfile)