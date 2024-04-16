#/usr/bin/env python
#
# shows the Julia set (see wikipedia)
import sys
import math
import cmath
import random
import numpy as np

def calcz(z,c,zabsmax):
    '''
    calculates the recurrsive function z=z^2 + c; and counts how many iterations are needed to
    reach the maximum nitmax or reach the maximum for z (zabsmax). 
    The ratio (iterations/maxiterations) [range 0..1] times 255 is returned; this 
    allows to use these return values as a color scale between 0...255.
    '''
    nit = 0
    nitmax = 1000
    while abs(z) < zabsmax and nit < nitmax:
        z = z**2 + c
        nit += 1
        ratio = (float(nit) / nitmax) * 255.0
    return ratio
        

def julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax):
    '''
    main loop that calculates recursive function for every pixel
    '''
    print "Calculate the 2D plane..."
    zabsmax = 10.0
    c = complex(-0.1,0.65)
    julia = np.zeros((im_width, im_height))
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = complex(float(ix) / im_width * xwidth + xmin,
                        float(iy) / im_height * yheight + ymin)
            # Do the iterations
            julia[ix][iy] = calcz(z,c,zabsmax)
    return julia

    
if __name__ == '__main__':
    if len(sys.argv)>1:
        file = sys.argv[1]
    else:
        file = 'juliadata.txt'

    print("Julia set fractal generator\n")
    im_width = 1000
    im_height = 1000
    xmin,xmax = -0.5, 0.5
    xwidth = xmax-xmin
    ymin, ymax = -0.5, 0.5
    yheight = ymax - ymin
    nitmax = 1000
    zabsmax = 10.0
    title="Julia set fractal generator"
    julia = julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax)
    with open(file,'w') as f:
        f.write(str(im_width)+'\n')
        f.write(str(im_height)+'\n')
        f.write(str(xmin)+'\n')
        f.write(str(xmax)+'\n')
        f.write(str(xwidth)+'\n')
        f.write(str(ymin)+'\n')
        f.write(str(ymax)+'\n')
        f.write(str(yheight)+'\n')
        #f.write(str(nitmax)+'\n')
        #f.write(str(zabsmax)+'\n')
        for i in julia:
            for j in i:
                f.write(str(j)+'\t')
        f.write('\n')
        

    
