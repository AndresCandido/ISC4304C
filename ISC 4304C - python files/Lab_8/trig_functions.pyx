cdef extern from "math.h": # Use the sine and cosine functions from the "math.h" C library instead of the python versions
    double sin(double x)
    double cos(double x)

def cy_sin(double x): 
    return sin(x)

def cy_cos(double x):
    return cos(x)