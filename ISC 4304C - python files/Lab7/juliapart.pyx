import numpy as np
cimport numpy as np

def calcz(double complex z, double complex c, double zabsmax):
    cdef int nit = 0
    cdef int nitmax = 1000
    while abs(z) < zabsmax and nit < nitmax:
        z = z**2 + c
        nit += 1
        ratio = (float(nit) / nitmax) * 255.0
    return ratio

def julia_loop(int im_width, int im_height, double xwidth, double yheight, double xmin, double ymin, int nitmax):
    print("Calculate the 2D plane...")
    cdef double complex c = -0.1 + 0.65j
    cdef double zabsmax = 10.0
    cdef np.ndarray julia = np.zeros((im_width, im_height), dtype=np.float64)

    cdef int ix, iy, nit
    cdef double complex z, ratio
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = (ix / im_width * xwidth + xmin) + 1j * (iy / im_height * yheight + ymin)
            # Do the iterations
            julia[ix][iy] = calcz(z, c, zabsmax)
    return julia