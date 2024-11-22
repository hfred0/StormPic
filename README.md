# StormPic
"Import" images into Stormworks using paintable signs

Requirements:
1. Python 3
2. Python Imaging Library

using the script:

(0. for every 9 pixels in height or width of the image a new block is created, so edit the image according to how big you want it to be in-game using something like gimp beforehand)
1. place script and desired image in a folder (optional, makes executing a bit easier)
2. execute the script with arg1 being the image file name (with file ending, e.g. .png, .jpg, ...) and arg2 being the background color as a hex value (without the '#' at the beginning if there)
3. place the output.xml file created in the same folder as the script in the stormworks vehicle folder (%appdata%/Stormworks/data/vehicles) and load it from within the game
4. copy it using the selection tool, load another vehicle, and paste it where neccessary
