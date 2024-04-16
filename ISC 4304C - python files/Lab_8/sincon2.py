#!/usr/bin/env python
#
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from trig_functions import cy_sin, cy_cos

def plot(mymap):
    fig = plt.figure()
    im = plt.imshow(mymap,cmap=plt.get_cmap('jet'), vmin=0, vmax=255)
    plt.savefig('sincon_plot.pdf')

def calc(x,y):
    z = 0.0
    for i in range(1,11):
        z += cy_sin(math.pow(x,1./i)) * cy_cos(math.pow(y,1./i))
    return z

if __name__ == '__main__':
    output=[]
    start = time.time()
    for x in range(1000):
        line=[]
        for y in range(1000):
            nx = x/100.
            ny = y/100.
            z = calc(nx,ny) * 255
            line.append(z)
        output.append(line)
    end = time.time()
    print("Time elapsed",end-start)
    plot(output)