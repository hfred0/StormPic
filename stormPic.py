from PIL import Image
import sys
import math
#using the script:
#   for every 9 pixels in height or width of the image a new block is created, so edit the image according to how big you want it to be in-game using something like gimp beforehand
#   place script and desired image in the same folder (optional, makes executing a bit easier)
#   execute the script with arg1 being the image file name (with file ending, e.g. .png, .jpg, ...) and arg2 being the background color as a hex value (without the '#' at the beginning if there)
#   place the output.xml file created in the same folder as the script and image in the stormworks vehicle folder (%appdata%/Stormworks/data/vehicles) and load it from within the game
# open image to be "imported", set color for pixels outside image bounds/fully tranparent pixels, create output xml
image = Image.open(sys.argv[1])
background = sys.argv[2]
output = open("output.xml", "w")
#ouputs hex string usable in the save file
def outputColorString(colors):
    string = ''
    for i in range(81):
        string += colors[i]
        if i < 80:
            string += ","
    return string

def setImage():
    #required xml string for save file part 1
    output.write('<?xml version="1.0" encoding="UTF-8"?><vehicle data_version="3" bodies_id="455"><authors/><bodies><body unique_id="455"><components>')
    #create bounds to combat game limitations (bounds having to be multiples of 9, having to be centered for most efficient use)
    hBlocks = math.ceil(image.size[0] / 9)
    vBlocks = math.ceil(image.size[1] / 9)
    offsetX = -math.floor(hBlocks/2)
    offsetZ = -math.floor(vBlocks/2)
    #create array containing the pixel colors of the image as a hex value for later use, set fully transparent pixels/pixels outside the image bounds to the desired background color
    colors = []
    for h in range(vBlocks * 9):
        for w in range(hBlocks * 9):
            temp = ""
            if w >= image.size[0] or h >= image.size[1]:
                temp = background
            else:
                color = image.getpixel((w, image.size[1] - h - 1))
                if color[3] != 0:
                    temp = '%02x%02x%02x' % (color[0], color[1], color[2])
                else:
                    temp = background
            colors.append(temp)
    #write the color values for each paintable block (9x9 grid) to the xml file
    for i in range(vBlocks * hBlocks):
        tempColors = []
        for h in range(9):
            for w in range(9):
                tempColors.append(colors[(w + i % hBlocks * 9) + (h + math.floor(i / hBlocks) * 9) * hBlocks * 9])
        #determine the position of each block
        pos = ""
        pos += 'x = "%s"' % str(i % hBlocks + offsetX)
        pos += ' z = "%s"' % str(math.floor(i / hBlocks) + offsetZ)
        pos = '<vp %s/>' % pos
        #"create" new block with desired color values of the image
        output.write('<c d="sign_na"><o r="1,0,0,0,1,0,0,0,1" sc="6" gc="%s">' % outputColorString(tempColors) + '%s<logic_slots><slot/></logic_slots></o></c>' % pos)
    #required xml string for save file part 2
    output.write('</components></body></bodies><logic_node_links/></vehicle>')

setImage()