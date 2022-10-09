# Converts images to a 2d array of ASCII characters
# Run it like so:
#   python imgtomap.py > f
# Type the image (ex: earth.png)
# Then, after the script is done you will have a file with
# the map 2d array that you can replace in index.html

from PIL import Image
import math 

imgpath = input()
def webSpaceFix(a):
    if a == " ":
        # nbsp works without the <pre> tag
        #return "&nbsp;"
        return a
    return a

# Charlist taken from  John Burkardt: https://people.sc.fsu.edu/~jburkardt/data/ascii_art_grayscale/ascii_art_grayscale.html
# 70 character sequence did not work for this
charset = " .:-=+*#%@" # Characters in ascending order (darkest is last)
#charset = charset[::-1]
charColorEnds = 255/len(charset)
def ctoascii(c):
    if c == 255: 
        return webSpaceFix(charset[len(charset)-1])
    k = math.floor(c/charColorEnds)
    return webSpaceFix(charset[k])

img = Image.open(imgpath)
img = img.convert('L').resize((200,100), Image.NEAREST)
width, height = img.size

print("var map = [\n",end="")
for y in range(height):
    print("[", end="")
    for x in range(width):
        print("['{}'],".format(ctoascii(img.getpixel((x, y)))), end="")
    print("],", end="")
print("]", end="")