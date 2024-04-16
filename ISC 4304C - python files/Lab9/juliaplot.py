#/usr/bin/env python
#
#
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def read_julia(filename):
    with open(filename, 'r') as f:
        for line in f:
            #print line.rstrip()
            x = line.rstrip()
            yield x

def plot(julia):
    print("Plot Julia...")
    fig, ax = plt.subplots()
    ax.imshow(julia, interpolation='nearest', cmap=cm.cool)
    return fig, ax

def plotlabels(fig, ax, im_width, im_height, xmin,xmax,xwidth, ymin, ymax, yheight):    
    # Set the tick labels to the coordinates of z0 in the complex plane
    xtick_labels = np.linspace(xmin, xmax, int(xwidth / 0.25))
    ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
    ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
    ytick_labels = np.linspace(ymin, ymax, int(yheight * 4))
    ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
    ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

    
if __name__ == '__main__':
    if len(sys.argv)>1:
        file = sys.argv[1]
    else:
        file = 'juliadata.txt'
    generator = read_julia(file)
    im_width  = int(next(generator))
    im_height = int(next(generator))
    xmin = float(next(generator))
    xmax = float(next(generator))
    xwidth = float(next(generator))
    ymin = float(next(generator))
    ymax = float(next(generator))
    yheight = float(next(generator))
    x1 = next(generator)
    #print(im_width, im_height, xmin,xmax,xwidth, ymin, ymax, yheight)
    #print(x1)
    x2 = x1.split('\t')
    julia = np.array(x2,dtype=float)
    julia = julia.reshape(im_width,im_height)
    #print(julia.size)
    fig, ax = plot(julia)
    plotlabels(fig, ax, im_width, im_height, xmin,xmax,xwidth, ymin, ymax, yheight)    
    plt.savefig('test.pdf')
