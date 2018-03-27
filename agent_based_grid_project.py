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

# Due date = Monday April 16
# In-class presentation on April 17
# This project and the prisoner's dilemma constitute all of Ch. 11
# This project is to model changes in land use as a new highway is built near a town
# This program should run for several years to observe trends in movement


# Generate town (size of 40 blocks)
# generate streets - use a standard block size of 150 meters on a side -- to keep it simple make this a basic grid
# generate a railway that runs near town center
# generate some businesses - retail, industrial, restauraunts, convenience stores with fuel (add your own?) These should be near the town's center
# industrial businesses are concentrated by the rail line
# industrial businesses can occupy more than one block
# generate 4 elementary (uniform distribution), 2 middle (north and south), and 1 high school (near center)
# generate a small college campus that occupies 7 square blocks on edge of town
# generate a city park near the center of town
# generate residential housing (multi-family and single family)
#

# Generate new highway location - note it will cut through the town but not too close to town center
# Make it an average of 12 blocks from the town center with a standard deviation of 3 blocks
# Make it on the same side of town as the college campus

#Display the grid


# agents
# business owners (separate out by business type)
# residents (resident types you define)

# rules for agents
#













BETRAY = 0
COOP = 1
NOTHING = 2

T = 0
R = 1
P = 2
S = 3

def main():
    N = 50  #number of iterations of prisoner's dilemma

    prob_betray_A_mean = 0.4
    prob_betray_A_std = 0.2
    prob_betray_B_mean = 0.6
    prob_betray_B_std = 0.1

    if box_muller(prob_betray_A_mean, prob_betray_A_std) < 0.5:
        A = COOP
    else:
        A = BETRAY
    if box_muller(prob_betray_B_mean,prob_betray_B_std) < 0.5:
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
        #modify so that some fraction of time the game is altered...
        #if

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

def box_muller(mu,sigma):
    a = uniform(0, 2 * pi)  # a param of Box Muller
    tmp = random()  # rand 0-1
    b = sigma * sqrt(-2 * log(tmp))  # b param of Box Muller
    gauss_rand1 = b * sin(a) + mu  # sample from dist. (first of two)
    #gauss_rand2 = b * cos(a) + mu  # sample from dist. (second of two)
    return gauss_rand1

if __name__ == '__main__':
    main()
print ("--- %s seconds ---" % (time.time() - start_time))