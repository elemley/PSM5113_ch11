from math import *
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
from psm_plot import *
from random import *
from time_step_scrolling import *

start_time = time.time()

BETRAY = 0
COOP = 1
NOTHING = 2

T = 0
R = 1
P = 2
S = 3

def main():
    N = 50  #number of iterations of prisoner's dilemma

    prob_betray_A = 0.5
    prob_betray_B = 0.5

    if random() > prob_betray_A:
        A = COOP
    else:
        A = BETRAY
    if random() > prob_betray_B:
        B = COOP
    else:
        B = BETRAY

    prisoner = np.empty(shape=(N, 2))
    for i in range(0, N):
        for j in range(0, 2):
            prisoner[i, j] = NOTHING

    prisoner[0,0] = A
    prisoner[0,1] = B

    sumA = years_served(prisoner[0,0],prisoner[0,1])
    sumB = years_served(prisoner[0, 1], prisoner[0, 0])

    years_served_A = [sumA]
    years_served_B = [sumB]

    for i in range(1,N):
        newA = prisoner[i-1,1]
        newB = prisoner[i-1,0]
        prisoner[i,0]=newA
        prisoner[i, 1] = newB
        sumA += years_served(prisoner[i, 0], prisoner[i, 1])
        sumB += years_served(prisoner[i, 1], prisoner[i, 0])
        years_served_A.append(sumA)
        years_served_B.append(sumB)

    #print grids[1]

    #rectangle = plt.Rectangle((0.5, 0.5), n - 2, n - 2, fc='none')
    #plt.gca().add_patch(rectangle)
    axes = AxesSequence()
    cmap1 = colors.ListedColormap(['red', 'green', 'black'])
    bounds=[0,0.99,1.99,2.99]
    norm=colors.BoundaryNorm(bounds, cmap1.N)

    plt.imshow(prisoner, cmap=cmap1, interpolation='nearest', norm=norm)
    plt.show()

    title_base = "Number of Years Served"
    title = title_base
    filename = "mod112.png"
    xlabel = "Number of Iterations"
    ylabel = "Years Served"
    y1label = "Years Served A"
    y2label = "Years Served B"


    TwoLineColorsPlot111(range(N),years_served_A,y1label,years_served_B,y2label,xlabel,ylabel,title,filename)

    """
    #cmap1 = LinearSegmentedColormap.from_list("my_map", cdict1, 3)
    for i, ax in zip(range(N), axes):
        ax.imshow(prisoner[i], cmap=cmap1, interpolation='nearest',norm=norm)
        ax.set_title("Time Step "+ str(i))
    axes.show()
"""

def years_served(A,B):
    # this always returns A's state only... so swap arguments when sending to get B's years served
    if A == COOP and B==COOP:
        return R
    elif A == BETRAY and B == COOP:
        return T
    elif A == COOP and B == BETRAY:
        return S
    else:
        return P


if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))