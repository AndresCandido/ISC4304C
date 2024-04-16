from numba import jit
import numpy as np

@jit
def mandelbrot(c,maxiter):
    z = c
    for n in range(maxiter):
        if z.real * z.real + z.imag * z.imag > 4.0:
            return n
        z = z*z + c
    return 0

@jit
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width*height))
    for i in range(width):
        for j in range(height):
            n3[i*width + j] = mandelbrot(r1[i] + 1j*r2[j],maxiter)
    return n3
