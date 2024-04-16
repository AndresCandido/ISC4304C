import sys
import math
import cmath
import random
import numpy as np
from juliapart import julia_loop  # import the Cythonized function

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
  julia = julia_loop(im_width, im_height, xwidth, yheight, xmin, ymin, nitmax)  # call the Cythonized function
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