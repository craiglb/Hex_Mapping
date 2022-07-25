#! /usr/bin/python3

import math
import os
import pyvips

#pip3 install pyvips
#sudo apt install libvips

###---------------------------------------------------------

baseScaleFactor = 10

xCanvusSize = 2048
yCanvusSize = 2048

hexScaleFactor = 3
haxLayers = 4

###---------------------------------------------------------

class Point:
    def __init__(point, x, y):
        point.x = x
        point.y = y

###---------------------------------------------------------

hexLineColors = ["lightgray", "darkgray", "lightslategray", "black"]

hexwidth = math.sqrt( 3 )
hexheight = 2.0 * 3.0 / 4.0

######################################################################

def hexPaper( hexScaleFactor, lineclour ):
    with open('hexmap.svg', 'a') as fout:
        for y in range( int( yCanvusSize / hexScaleFactor ) ):      # goes Top to Bottom
            for x in range( int( xCanvusSize / hexScaleFactor ) ): # goes Left to Right
                if (y % 2) == 0:
                    yOffSet = 0.0
                else:
                    yOffSet = hexwidth * hexScaleFactor / 2.0

                cirx = yOffSet + hexwidth  * hexScaleFactor * x
                ciry = 0 +        hexheight * hexScaleFactor * y

                a = Point( cirx + hexScaleFactor * 0.0,             ciry + hexScaleFactor * 1.0 )
                b = Point( cirx + hexScaleFactor * math.sqrt(0.75), ciry + hexScaleFactor * 0.5 )
                c = Point( cirx + hexScaleFactor * math.sqrt(0.75), ciry - hexScaleFactor * 0.5 )
                d = Point( cirx - hexScaleFactor * 0.0,             ciry - hexScaleFactor * 1.0 )
                e = Point( cirx - hexScaleFactor * math.sqrt(0.75), ciry - hexScaleFactor * 0.5 )
                f = Point( cirx - hexScaleFactor * math.sqrt(0.75), ciry + hexScaleFactor * 0.5 )

                fout.write('<polygon fill="none" stroke="%s" stroke-width="1" points="%f,%f  %f,%f %f,%f %f,%f %f,%f %f,%f" />\n' %(lineclour, a.x,a.y,b.x,b.y,c.x,c.y,d.x,d.y,e.x,e.y,f.x,f.y) )
#                f.write('<circle r="1" fill="black" stroke="black" stroke-width="1" cx="%f" cy="%f" />\n' %(cirx, ciry) )

##################################################################

with open('hexmap.svg', 'w') as f:
    f.write('<?xml version="1.0" standalone="no"?>\n')
    f.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"   "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
    f.write('<svg viewBox="0 0 %s %s" xmlns="http://www.w3.org/2000/svg" version="1.1">\n' %(xCanvusSize, yCanvusSize))
    f.write('<!-- Show outline of canvas using "rect" element -->\n')
    f.write('<rect x="0" y="0" width="%s" height="%s" fill="none" stroke="white" stroke-width="1" />\n' %(xCanvusSize, yCanvusSize))

for i in range( haxLayers ):
              hexPaper( pow(hexScaleFactor, i) * baseScaleFactor, hexLineColors[i] )

with open('hexmap.svg', 'a') as f:
    f.write('</svg>\n')

##################################################################

#image = pyvips.Image.new_from_file("hexmap.svg", dpi=300)
image = pyvips.Image.new_from_file("hexmap.svg" )
image.write_to_file("hex-grid-overlay-%s-%s.png"  %(xCanvusSize, yCanvusSize) )
os.remove("hexmap.svg")
