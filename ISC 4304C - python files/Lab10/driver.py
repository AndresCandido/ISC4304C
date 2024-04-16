import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import time
import sys

import mandelbrot_basic as base
import mandelbrot_numba as numb

def mandelbrot_image(func, xmin,xmax,ymin,ymax,width=3,height=3,maxiter=80,cmap='hot_r',plotting=True):
    dpi = 72
    img_width = dpi * width
    img_height = dpi * height

    tic = time.process_time()    
    z = func(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    toc = time.process_time()
    
    print("run time:",toc-tic)
    if plotting:
        fig, ax = plt.subplots(figsize=(width, height),dpi=72)
        ticks = [0,img_width/2,img_width]
        x_ticks = [xmin, (xmax+xmin)/2, xmax]
        plt.xticks(ticks, x_ticks)
        y_ticks = [ymin , (ymax+ymin)/2,ymax]
        plt.yticks(ticks, y_ticks)
        norm = colors.PowerNorm(0.3)
        znew = [zi if zi<maxiter else 0 for zi in z]
        znew = np.array(znew).reshape(img_width,img_height)
        ax.imshow(np.array(znew).T,cmap=cmap,origin='lower',norm=norm)
        plt.show()
    return toc-tic

def magnifier(center, magnify):
  m = 1.0/magnify
  xl = center[0] - m 
  xu = center[0] + m
  yl = center[1] - m
  yu = center[1] + m
  print("Center:",center)
  print("Magnification:",magnify, "[",m,"]")
  print(xl,xu,yl,yu)
  return (xl,xu,yl,yu)


if __name__ == "__main__":
    mandelbrotset4 = base.mandelbrot_set
    mandelbrotset3 = numb.mandelbrot_set

    #width = 50
    #height = 50
    width = 5
    height = 5
    maxiter = 2048
    center = [-0.743,0.1264]
    #center = [-0.9889624648287648, -0.2547082228142221]
    magnify = 100.0
    if len(sys.argv) > 3:
        center = [float(sys.argv[1]),float(sys.argv[2])]
        magnify = float(sys.argv[3])

    xmin, xmax, ymin, ymax = magnifier(center,magnify)
    print("Pure python implementation")
    t4 = mandelbrot_image(mandelbrotset4,xmin,xmax,ymin,ymax,width,height,maxiter,cmap='hot',plotting=False)
    print(t4)

    print("Numba speed up")
    t3 = mandelbrot_image(mandelbrotset3,xmin,xmax,ymin,ymax,width,height,maxiter,cmap='hot',plotting=False)
    print(t4/t3)

    #mandelbrot_image(mandelbrotset1,xmin,xmax,ymin,ymax,width,height,maxiter,cmap='hot',plotting=True)

